"""User interface for static reconstruction using Adel modules
"""
import numpy
import pandas

import openalea.plantgl.all as pgl

from alinea.adel.geometric_elements import Leaves
from alinea.adel.Stand import AgronomicStand
from alinea.adel.newmtg import mtg_factory
from alinea.adel.mtg_interpreter import mtg_interpreter, plot3d

def blade_dimension(area = None, length=None , width=None, ntop=None, leaves=None,
                    plant=1, wl=0.1):
    """Estimate blade dimension and/or compatibility with leaf shapes form factors

    Args:
        area: (array) vector of blade area. If None, will be estimated using
         other args
        length: (array) vector of blade lengths. If None, will be estimated using
         other args
        width: (array) vector of blade widths. If None, will be estimated using
         other args
        ntop: (array) vector of leaf position (topmost leaf =1). If None
        (default), leaf dimensions are assumed to be from top to base.
        leaves: (object) a Leaves instance defining leaf shapes. If None (default)
        the adel default shape will be used
        plant: (int or array) vector of plant number
        wl: (float) the width / length ratio used to estimates dimensions in case
         of  uncomplete data

    Returns:
        a pandas dataframe with estimated blade dimensions

    """

    if area == length == width == None:
        area = (15, 20, 30)

    if leaves is None:
        leaves = Leaves()
    ff = leaves.form_factor()
    ff = {int(k): v for k, v in ff.iteritems()}

    if area is None:
        if length is None:
            width = numpy.array(width)
            length = width / numpy.array(wl)
        elif width is None:
            length = numpy.array(length)
            width = length * numpy.array(wl)
        else:
            length = numpy.array(length)
            width = numpy.array(width)
        if ntop is None:
            ntop = numpy.arange(1,len(length) + 1)
        else:
            ntop = numpy.array(ntop)
        ffn = numpy.array([ff[k] for k in ntop])
        area = ffn * length * width
    else:
        area = numpy.array(area)
        if ntop is None:
            ntop = numpy.arange(1,len(area) + 1)
        else:
            ntop = numpy.array(ntop)
        ffn = numpy.array([ff[k] for k in ntop])
        # adjust length/width if one is  None or overwrite width if all are set
        if length is None:
            if width is None:
                length = numpy.sqrt(area / ffn / wl)
                width = length * wl
            else:
                width = numpy.array(width)
                length = area / ffn / width
        else:
            length = numpy.array(length)
            width = area / ffn / length

    if isinstance(plant, int):
        plant = [plant] * len(ntop)

    return pandas.DataFrame({'plant': plant, 'ntop': ntop, 'L_blade': length,
                             'W_blade': width, 'S_blade': area})

def stem_dimension(h_ins=None, d_stem=None, internode=None, sheath=None,
                   d_internode=None, d_sheath=None, ntop=None, plant=1):
    """Estimate dimension of stem organs from stem measurements

    Args:
        h_ins: (array) vector of blade insertions height
        d_stem:(float or array) vector of stem diameter
        internode:(array) vector of internode lengths. If None, will be estimated using
         other args
        sheath: (array) vector of sheath lengths. If None, will be estimated using
         other args
        d_internode: (array) vector of intenode diameters. If None, will be estimated using
         other args
        d_sheath: (array) vector of sheath diameters. If None, will be estimated using
         other args
        ntop:(array) vector of leaf position (topmost leaf =1). If None
        (default), stem dimensions are assumed to be from top to base.
        plant: (int or array) vector of plant number

    Returns:
        a pandas dataframe with estimated sheath and internode dimension
    """

    if h_ins is None and h_ins == internode == sheath:
        h_ins = (60, 50, 40)

    if d_stem is None and d_stem == d_internode == d_sheath:
        d_stem = 0.3

    if h_ins is None:
        if sheath is None:
            sheath = numpy.array([0] * len(internode))
        else:
            sheath = numpy.array(sheath)
        if internode is None:
            internode = numpy.array([0] * len(sheath))
        else:
            internode = numpy.array(internode)
        if ntop is None:
            ntop = numpy.arange(1, len(h_ins) + 1)
        else:
            ntop = numpy.array(ntop)
        order = numpy.argsort(-ntop)
        reorder = numpy.argsort(order)
        h_ins = (internode[order].cumsum() + sheath[order])[reorder]
    else:
        h_ins = numpy.array(h_ins)
        if ntop is None:
            ntop = numpy.arange(1, len(h_ins) + 1)
        else:
            ntop = numpy.array(ntop)
        order = numpy.argsort(-ntop)
        reorder = numpy.argsort(order)

        if sheath is None:
            if internode is None:
                sheath = numpy.array([0] * len(h_ins))
                internode = numpy.diff([0] + list(h_ins[order]))[reorder]
            else:
                internode = numpy.array(internode)
                sheath = numpy.maximum(0, h_ins[order] - internode[order].cumsum())[reorder]
                internode = numpy.diff([0] + (h_ins[order] - sheath[order]).tolist())[reorder]
        else:
            sheath = numpy.array(sheath)
            internode = numpy.diff([0] + (h_ins[order] - sheath[order]).tolist())[reorder]

    if d_internode is None:
        if d_sheath is None:
            d_internode = [d_stem] * len(h_ins)
        else:
            d_internode = d_sheath
    if d_sheath is None:
        d_sheath = d_internode

    if isinstance(plant, int):
        plant = [plant] * len(ntop)

    return pandas.DataFrame({'plant': plant, 'ntop': ntop, 'h_ins': h_ins,
                             'L_sheath': sheath, 'W_sheath': d_sheath,
                             'L_internode': internode, 'W_internode': d_internode})


def ear_dimension(peduncle=None, ear=None, spike=None, d_peduncle=0.3, projected_area_ear=None, wl_ear=0.1, plant=1):
    """Estimate dimensions of ear cylinders from ear measuremenst

    Args:
        peduncle: length of the peduncle. If None, no peduncle is computed
        ear: length of the ear. If None, no ear is computed
        spike: length of the ear + awn. If None, no awn is computed
        d_peduncle: diameter of the peduncle
        projected_area_ear: projected area of the ear
        wl_ear: width/length ratio for ear. Used only if projected_ear_area is missing
        plant: (int or array) vector of plant number

    Returns:
        a pandas DataFrame with ear dimensions
    """
    if peduncle == ear == spike == None:
        return None

    dfl = []
    pos = 0

    if peduncle is not None:
        dfl.append(pandas.DataFrame({'plant': plant, 'ntop':pos,
                                     'L_internode':peduncle,
                                     'W_internode': d_peduncle}, index=[pos]))
        pos -= 1

    if ear is not None:
        if projected_area_ear is None:
            w_ear = wl_ear * ear
        else:
            w_ear = projected_area_ear / ear
        dfl.append(pandas.DataFrame(
            {'plant': plant, 'ntop': pos, 'L_internode': ear,
             'W_internode': w_ear}, index=[pos]))
        pos -= 1

        if spike is not None:
            dfl.append(pandas.DataFrame(
                {'plant': plant, 'ntop': pos, 'L_internode': spike - ear,
                 'W_internode': w_ear}, index=[pos]))

    return pandas.concat(dfl,axis=0)



def dimension_table(blades=None, stem=None, ear=None):
    if blades is None:
        blades = blade_dimension()
    if stem is None:
        stem = stem_dimension()

    if ear is None:
        return blades.merge(stem)
    else:
        stemear = pandas.concat([stem, ear]).set_index(['plant','ntop'])
        return pandas.concat([stemear, blades.set_index(['plant','ntop'])], axis=1).reset_index()


class AdelDress(object):
    """A class interface to Adel for static reconstruction"""
    conv_units = {'mm': 0.001, 'cm': 0.01, 'dm': 0.1, 'm': 1, 'dam': 10, 'hm': 100,
             'km': 1000}
    def __init__(self, scene_unit='cm', dim_unit='cm', dimT=None, leaves=None, nsect=1, classic=False, stand=None):
        """

        Args:
            scene_unit:
            dim_unit:
            dimT:
            leaves:
            nsect:
            classic:
            stand:
        """

        if leaves is None:
            leaves = Leaves()

        if stand is None:
            stand = AgronomicStand(sowing_density=250, plant_density=250,
                                   inter_row=0.15)

        if dimT is None:
            dimT = dimension_table()

        self.scene_unit = scene_unit
        self.dim_unit = dim_unit
        self.dimT = dimT.fillna(0)
        self.nsect = nsect
        self.leaves = leaves
        self.stand = stand
        self.dimT = dimT
        self.classic = classic


    def canopy_table(self, nplants=1):
        if nplants > 1:
            raise NotImplementedError()
        df = self.dimT.loc[:,
             ['plant', 'ntop', 'L_blade', 'W_blade', 'L_sheath', 'W_sheath', 'L_internode', 'W_internode']]
        df.rename(
            columns={'L_blade': 'Ll', 'W_blade': 'Lw_shape',
                     'L_sheath': 'Gl', 'W_sheath': 'Gd',
                     'L_internode': 'El', 'W_internode': 'Ed'}, inplace=True)
        # add mandatory topological info and sort from base to top
        df.loc[:, 'axe_id'] = 'MS'
        df.loc[:, 'ms_insertion'] = 0
        df.loc[:,
        'numphy'] = df.ntop.max() + 1 - df.ntop
        df = df.sort_values(['plant', 'numphy'])
        # compute visibility
        ht0 = 0
        hbase = df['El'].cumsum() - df['El']
        hcol = hbase + df['Gl'] + df['El']
        h_hide = [max([ht0] + hcol[:i].tolist()) for i in range(len(hcol))]
        htube = numpy.maximum(0, h_hide - hbase)
        df['Lv'] = numpy.minimum(df['Ll'], numpy.maximum(0, df['Ll'] + df['Gl'] + df['El']- htube))
        df['Gv'] = numpy.minimum(df['Gl'], numpy.maximum(0, df['Gl'] + df['El'] - htube))
        df['Ev'] = numpy.minimum(df['El'], numpy.maximum(0, df['El'] - htube))
        # add missing mandatory data  (does like adel)
        df.loc[:, 'Laz'] = [180 + (numpy.random.random() - 0.5) * 30 for i in
                            range(len(df))]  # leaf azimuth
        df.loc[:, 'LcType'] = numpy.where(df['ntop'] > 0, df['ntop'],
                                          1)  # selector for first level in leaf db
        df.loc[:,
        'LcIndex'] = 1  # selector for second level in leaf_db (ranging 1:max_nb_leaf_per_level)
        # fill other columns
        df.loc[:, 'Lr'] = 0
        df.loc[:, 'Lsen'] = 0
        df.loc[:, 'L_shape'] = df['Ll']
        df.loc[:, 'Linc'] = 1
        df.loc[:, 'Gsen'] = 0
        df.loc[:, 'Ginc'] = 0
        df.loc[:, 'Esen'] = 0
        df.loc[:, 'Einc'] = 0
        return df

    def canopy(self, nplants=1):
        df = self.canopy_table(nplants=nplants)
        nplants, domain, positions, domain_area = self.stand.smart_stand(nplants=nplants)
        stand = [(pos, 0) for pos in positions]
        g = mtg_factory(df.to_dict('list'), leaf_sectors=self.nsect, leaves=self.leaves, stand=stand)
        # add geometry
        g = mtg_interpreter(g, self.leaves, classic=self.classic)
        return g

    def plot(self, g):
        scene = plot3d(g)
        pgl.Viewer.display(scene)
