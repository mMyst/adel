
# This file has been generated at Fri Apr 27 12:51:19 2012

from openalea.core import *


__name__ = 'alinea.training'

__editable__ = True
__description__ = 'A set of example to train students '
__license__ = ''
__url__ = ''
__alias__ = ['training']
__version__ = ''
__authors__ = ''
__institutes__ = ''
__icon__ = ''


__all__ = ['sleep_sleep', 'sleep_leaf_sectors_by_number', 'sleep_compute_distance', 'sleep_get_distances', '_150448656', 'sleep_leaf_sectors']



sleep_sleep = Factory(name='sleep',
                authors=' (wralea authors)',
                description='',
                category='time',
                nodemodule='alinea.adel.training.sleep',
                nodeclass='sleep',
                inputs=[{'interface': None, 'name': 'obj', 'value': None, 'desc': 'Python object'}, {'interface': IFloat, 'name': 'seconds', 'value': 0.0, 'desc': 'delay execution for a given number of seconds'}],
                outputs=[{'interface': None, 'name': 'obj', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




sleep_leaf_sectors_by_number = Factory(name='filter leaf sectors by number',
                authors=' (wralea authors)',
                description='',
                category='time',
                nodemodule='alinea.adel.training.sleep',
                nodeclass='leaf_sectors_by_number',
                inputs=[{'interface': None, 'name': 'g', 'desc': 'MTG'}, {'interface': IInt, 'name': 'target leaf number', 'value': 1, 'desc': 'Target leaf number, counted from the top'}, {'interface': IInt, 'name': 'infectious leaf number', 'value': 4, 'desc': 'Infectious leaf number considered, counted from the top'}],
                outputs=[{'name': 'g', 'desc': 'MTG'}, {'interface': ISequence, 'name': 'target sectors', 'desc': 'target sectors that can be infected'}, {'interface': ISequence, 'name': 'source sectors', 'desc': 'source sectors of the infection'}],
                widgetmodule=None,
                widgetclass=None,
               )




sleep_compute_distance = Factory(name='compute distance',
                authors=' (wralea authors)',
                description='',
                category='time',
                nodemodule='alinea.adel.training.sleep',
                nodeclass='compute_distance',
                inputs=[{'interface': ISequence, 'name': 'target sectors'}, {'interface': ISequence, 'name': 'source sectors'}, {'interface': IFunction, 'name': 'distance'}],
                outputs=[{'name': 'g', 'desc': 'MTG'}],
                widgetmodule=None,
                widgetclass=None,
               )




sleep_get_distances = Factory(name='get distances',
                authors=' (wralea authors)',
                description='extract/reshape distance',
                category='Unclassified',
                nodemodule='alinea.adel.training.sleep',
                nodeclass='get_distances',
                inputs=[{'interface': None, 'name': 'obj', 'value': None, 'desc': 'mtg'}, {'interface': IFileStr, 'name': 'filename', 'value': None, 'desc': 'labels of the results computed by distance function'}],
                outputs=[{'interface': IFileStr, 'name': 'filename', 'desc': ''}, {'interface': ISequence, 'name': 'leaves', 'desc': ''}, {'interface': None, 'name': 'sectors', 'desc': ''}, {'interface': None, 'name': 'age', 'desc': ''}, {'interface': None, 'name': 'distance', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




_150448656 = CompositeNodeFactory(name='TD simple wheat',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('openalea.flow control', 'iter'),
   3: ('openalea.data structure.tuple', 'pair'),
   4: ('alinea.adel.leaf', 'curve discretizer'),
   5: ('alinea.adel.io', 'mtg (params)'),
   7: ('openalea.data structure', 'int'),
   8: ('openalea.flow control', 'pool reader'),
   9: ('openalea.flow control', 'pool writer'),
   10: ('alinea.adel.geometry', 'symbols'),
   11: ('alinea.adel.leaf', 'curve discretizer'),
   12: ('alinea.adel.fitting', 'fit'),
   13: ('openalea.file', 'start'),
   14: ('alinea.training', 'sleep'),
   15: ('openalea.data structure', 'int'),
   16: ('alinea.training', 'compute distance'),
   17: ('alinea.adel.geometry', 'MTG Interpreter time'),
   18: ('openalea.function operator', 'function'),
   19: ('openalea.plantgl.edition', 'Curve2D'),
   20: ('openalea.flow control', 'rendez vous'),
   21: ('alinea.training', 'filter leaf sectors'),
   22: ('openalea.flow control', 'annotation'),
   23: ('openalea.data structure', 'int'),
   24: ('alinea.adel.parameterisation', 'MonoAxeWheat'),
   25: ('openalea.function operator', 'function'),
   26: ('alinea.adel.macro', 'plot'),
   27: ('alinea.adel.io', 'update thermal time'),
   28: ('openalea.numpy.creation', 'arange'),
   29: ('openalea.data structure', 'int'),
   30: ('openalea.file', 'filename'),
   31: ('alinea.training', 'get distances'),
   32: ('openalea.plantgl.edition', 'Curve2D'),
   33: ('alinea.adel.parameterisation', 'simple sr'),
   34: ('alinea.adel.parameterisation', 'simple xy'),
   35: ('alinea.adel.io', 'PairAsDict'),
   36: ('openalea.pylab.plotting', 'PyLabPlot')},
                             elt_connections={  29781044: (25, 0, 17, 3),
   29781056: (31, 0, 13, 0),
   29781068: (9, 0, 26, 0),
   29781080: (33, 0, 32, 0),
   29781092: (20, 0, 9, 1),
   29781104: (30, 0, 31, 1),
   29781116: (18, 0, 16, 2),
   29781128: (31, 3, 36, 1),
   29781140: (27, 0, 17, 0),
   29781152: (12, 0, 3, 1),
   29781164: (7, 0, 12, 4),
   29781176: (21, 2, 16, 1),
   29781188: (34, 0, 19, 0),
   29781200: (29, 0, 3, 0),
   29781212: (4, 0, 12, 0),
   29781224: (3, 0, 35, 0),
   29781236: (28, 0, 2, 0),
   29781248: (8, 0, 31, 0),
   29781260: (5, 0, 27, 0),
   29781272: (23, 0, 5, 1),
   29781284: (11, 1, 12, 3),
   29781296: (10, 0, 17, 1),
   29781308: (17, 0, 21, 0),
   29781320: (32, 0, 11, 0),
   29781332: (21, 0, 20, 0),
   29781344: (15, 0, 28, 2),
   29781356: (21, 1, 16, 0),
   29781368: (35, 0, 10, 0),
   29781380: (24, 0, 5, 0),
   29781392: (16, 0, 20, 1),
   29781404: (19, 0, 4, 0),
   29781416: (31, 4, 36, 1),
   29781428: (11, 0, 12, 2),
   29781440: (2, 0, 14, 0),
   29781452: (31, 2, 36, 1),
   29781464: (14, 0, 17, 2),
   29781476: (4, 1, 12, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'iter',
         'delay': 1,
         'factory': '<openalea.core.node.NodeFactory object at 0x06AA6C50> : "iter"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -647.33725166078978,
         'posy': 91.445517705871538,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'pair',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x06A283B0> : "pair"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -264.61667837411221,
         'posy': 18.235695264082899,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'xy',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x06AA65F0> : "curve discretizer"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -133.81906942530145,
         'posy': -84.973067510462613,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'mtg (params)',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x06BA4430> : "mtg (params)"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -877.3322917735004,
         'posy': 63.031161668397033,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': '12',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x06A3FE50> : "int"',
         'hide': True,
         'id': 7,
         'is_in_error_state': False,
         'is_user_application': False,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': -280.33937538020911,
         'posy': -141.3137814336595,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'g',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x06AA6DB0> : "pool reader"',
         'hide': True,
         'id': 8,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -412.69185305852437,
         'posy': 375.68415971360236,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'g = MTG : nb_vertices=58, nb_scales=5\n\nScale 0\n/0\n\nScale 1\n/plant1\n\nScale 2\n/axe0\n\nScale 3\n/metamer1\n<metamer2\n<metamer3\n<metamer4\n<metamer5\n<metamer6\n<metamer7\n<metamer8\n<metamer9\n<metamer10\n<metamer11\n\nScale 4\n/StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement\n<StemElement\n\t+LeafElement\n\t<LeafElement\n\t<LeafElement',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x06AA6CF0> : "pool writer"',
         'hide': True,
         'id': 9,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -660.53125394421431,
         'posy': 423.90630558728861,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'symbols',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A286D0> : "symbols"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -432.58118028091036,
          'posy': 93.138373830018381,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'block': False,
          'caption': 'sr',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06AA65F0> : "curve discretizer"',
          'hide': True,
          'id': 11,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -83.684903971131789,
          'posy': -84.636056713762557,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': 'fit',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x067BE850> : "fit"',
          'hide': True,
          'id': 12,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -174.30275989038273,
          'posy': -29.375008838525986,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': 'start',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A28FD0> : "start"',
          'hide': True,
          'id': 13,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -404.84173628838943,
          'posy': 487.82868500124482,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': 'sleep',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08F7AA70> : "sleep"',
          'hide': True,
          'id': 14,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -646.95209757822283,
          'posy': 144.5570620962329,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   15: {  'block': False,
          'caption': '20',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A3FE50> : "int"',
          'hide': True,
          'id': 15,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -635.47791093364845,
          'posy': 0.63906075107892946,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   16: {  'block': False,
          'caption': 'compute distance',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08F7AA90> : "compute distance"',
          'hide': True,
          'id': 16,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -573.56299708990855,
          'posy': 340.93597326920951,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   17: {  'block': False,
          'caption': 'MTG Interpreter time',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A286F0> : "MTG Interpreter time"',
          'hide': True,
          'id': 17,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -702.12611755575961,
          'posy': 231.73008536616928,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   18: {  'block': False,
          'caption': 'my_distance',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x069549B0> : "function"',
          'hide': True,
          'id': 18,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -493.3760249421872,
          'posy': 221.64977132794871,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   19: {  'block': False,
          'caption': 'Curve2D',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06EDD410> : "Curve2D"',
          'hide': True,
          'id': 19,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -143.34879438495653,
          'posy': -131.56298631052479,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   20: {  'block': False,
          'caption': 'rendez vous',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06AA6CD0> : "rendez vous"',
          'hide': True,
          'id': 20,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -617.98247651656789,
          'posy': 377.83809240601823,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   21: {  'block': False,
          'caption': 'filter leaf sectors',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08F7AB50> : "filter leaf sectors"',
          'hide': True,
          'id': 21,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -681.84735400495879,
          'posy': 281.7039282854048,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   22: {  'factory': '<openalea.core.node.NodeFactory object at 0x06AA6A10> : "annotation"',
          'id': 22,
          'posx': -829.41464120135356,
          'posy': -39.437297313712264,
          'txt': 'Number of sectors / leaf'},
   23: {  'block': False,
          'caption': '3',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A3FE50> : "int"',
          'hide': True,
          'id': 23,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -784.45869367292312,
          'posy': 1.2037922647801071,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   24: {  'block': False,
          'caption': 'MonoAxeWheat',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08FD6490> : "MonoAxeWheat"',
          'hide': True,
          'id': 24,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -941.9363918301533,
          'posy': 13.527135298635303,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   25: {  'block': False,
          'caption': 'grow',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x069549B0> : "function"',
          'hide': True,
          'id': 25,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -548.51116369127533,
          'posy': 96.623694274316705,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   26: {  'block': False,
          'caption': 'plot',
          'delay': 0,
          'factory': '<openalea.core.compositenode.CompositeNodeFactory object at 0x06569EB0> : "plot"',
          'hide': True,
          'id': 26,
          'is_in_error_state': False,
          'is_user_application': False,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -605.62465564345712,
          'posy': 469.56427165392739,
          'priority': 0,
          'use_user_color': False,
          'user_application': False,
          'user_color': None},
   27: {  'block': False,
          'caption': 'update thermal time',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06BA44B0> : "update thermal time"',
          'hide': True,
          'id': 27,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -874.7587733467376,
          'posy': 120.96785766271395,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   28: {  'block': False,
          'caption': 'arange',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08CBA6B0> : "arange"',
          'hide': True,
          'id': 28,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -656.08116000608527,
          'posy': 53.621357307731415,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   29: {  'block': False,
          'caption': '1',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A3FE50> : "int"',
          'hide': True,
          'id': 29,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -285.09477082109731,
          'posy': -14.791873182544558,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   30: {  'block': False,
          'caption': 'filename',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06A28E50> : "filename"',
          'hide': True,
          'id': 30,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -365.59115243771453,
          'posy': 331.9477948514218,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   31: {  'block': False,
          'caption': 'get distances',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08F7AB30> : "get distances"',
          'hide': True,
          'id': 31,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -423.90630558728861,
          'posy': 435.12075811605285,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   32: {  'block': False,
          'caption': 'Curve2D',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06EDD410> : "Curve2D"',
          'hide': True,
          'id': 32,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -35.432269627069978,
          'posy': -144.73844039712225,
          'priority': 0,
          'use_user_color': False,
          'user_application': False,
          'user_color': None},
   33: {  'block': False,
          'caption': 'simple sr',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08FD6470> : "simple sr"',
          'hide': True,
          'id': 33,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -38.467270414011807,
          'posy': -179.83448918550513,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   34: {  'block': False,
          'caption': 'simple xy',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x08FD6550> : "simple xy"',
          'hide': True,
          'id': 34,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -144.25226405254418,
          'posy': -173.10271686305302,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   35: {  'block': False,
          'caption': 'PairAsDict',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x06BA4530> : "PairAsDict"',
          'hide': True,
          'id': 35,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -277.9260287412352,
          'posy': 54.815860339966768,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   36: {  'block': False,
          'caption': 'PyLabPlot',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x067BEE30> : "PyLabPlot"',
          'hide': True,
          'id': 36,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -328.58345909279251,
          'posy': 502.40747328863841,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'is_in_error_state': False,
                'is_user_application': False,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'is_in_error_state': False,
                 'is_user_application': False,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   4: [(1, '15')],
   5: [],
   7: [(0, '12')],
   8: [(0, "'g'")],
   9: [(0, "'g'")],
   10: [(1, 'None'), (2, 'False')],
   11: [(1, '15')],
   12: [],
   13: [],
   14: [(1, '0.02')],
   15: [(0, '20')],
   16: [],
   17: [],
   18: [  (  0,
             '\'from sys import maxint\\nfrom openalea.plantgl import all as pgl\\n\\nDISTANCE = \\\'BOX\\\'\\nDISTANCE = \\\'LOVEL\\\'\\nDISTANCE = \\\'MESH\\\'\\n\\ndef my_distance(n, sectors):\\n    """ Compute the distance with infectable sectors. """\\n    if \\\'distance\\\' not in n._g._properties:\\n        n._g.add_property(\\\'distance\\\')\\n    tesselator = pgl.Tesselator()\\n    bbc = pgl.BBoxComputer(tesselator)\\n\\n    def base(geom):\\n        if geom:\\n          pts = geom.pointList\\n          if pts:\\n            n = len(pts)\\n            assert n%2==0\\n            return 1/2*(pts[0]+pts[n/2])\\n\\n    def top(geom):\\n        if geom:\\n          pts = geom.pointList\\n          if pts:\\n            n = len(pts)\\n            assert n%2==0\\n            return 1/2*(pts[n/2-1]+pts[-1])\\n\\n    def bbox_distance(g1, g2):\\n\\n        bbc.process(pgl.Scene([g1]))\\n        bbox1 = bbc.result\\n        bbc.process(pgl.Scene([g2]))\\n        bbox2 = bbc.result\\n\\n        # TODO bbox.lowerLeftCorner, bbox.upperRightCorner\\n        return bbox1.distance(bbox2)\\n\\n    def mesh_distance(g1, g2):\\n        pts1 = g1.pointList\\n        pts2 = g2.pointList\\n        if pts1 and pts2:\\n            d = maxint\\n            for pt in pts2:\\n                p1, i = pts1.findClosest(pt)\\n                # TODO: To Fix\\n                d = pgl.norm(pt-p1)\\n                return d\\n        else:\\n            return maxint\\n\\n    def lovel_distance(g1,g2):\\n        p1 = base(g1)\\n        p2 = top(g2)\\n        return pgl.norm(p2-p1)\\n        \\n    def opt_distance(n1, n2):\\n        g1 = n1.geometry\\n        g2 = n2.geometry\\n        if not g1  or not g2:\\n            return maxint\\n        if DISTANCE == \\\'BOX\\\':\\n            return bbox_distance(g1, g2)\\n        elif DISTANCE== \\\'LOVEL\\\':\\n            return lovel_distance(g1, g2)\\n        elif DISTANCE == \\\'MESH\\\':\\n            return mesh_distance(g1,g2)\\n\\n    dists = [opt_distance(n, source) for source in sectors]\\n    dist = min(dists) if dists else maxint\\n\\n    if not n.distance:\\n        n.distance = []\\n    if dist != maxint:\\n        n.distance.append((n.age, dist))\\n\\n    print n, dist\\n    if dist<=1:\\n        n.color = 0,0,255\\n\\n\'')],
   19: [],
   20: [],
   21: [(1, '0'), (2, '350')],
   22: [],
   23: [(0, '3')],
   24: [  (  0,
             "{'Lamina_width': [0.29999999999999999, 0.32500000000000001, 0.40000000000000002, 0.45000000000000001, 0.55000000000000004, 0.75, 1, 1.2, 1.28, 1.425, 1.8], 'Lamina_length': [8.125, 9.25, 9.3499999999999996, 10, 11.4, 13.699999999999999, 16.550000000000001, 19.800000000000001, 25.175000000000001, 28.800000000000001, 24.100000000000001], 'Sheath_length': [3, 3.0499999999999998, 3.0499999999999998, 3.3999999999999999, 4.2000000000000002, 6.2249999999999996, 9.125, 12, 14.199999999999999, 17.199999999999999, 18.675000000000001], 'Stem_diameter': [0.14000000000000001, 0.17999999999999999, 0.20999999999999999, 0.23999999999999999, 0.28999999999999998, 0.34000000000000002, 0.35999999999999999, 0.40000000000000002, 0.47999999999999998, 0.54000000000000004, 0.72999999999999998], 'Internode_length': [0, 0, 0, 0, 0, 0.10000000000000001, 1.8999999999999999, 6.0999999999999996, 9.6750000000000007, 14.449999999999999, 16.949999999999999]}"),
          (1, '30'),
          (2, '1.0'),
          (3, '1.0'),
          (4, '1.0'),
          (5, '1.0')],
   25: [  (  0,
             '\'def grow(n, time):\\n    """\\n    This function is called on each node to compute its evolution with time\\n    The following properties available as parameters:\\n        - on metamer: final_length of the leaf, start_tt of the leaf, end_tt of the leaf, start_insertion, end_insertion, insertion_angle, frate(falling rate in degrees.dd-1)\\n        - LeafElement: start_tt of the sector, end_tt of the sector\\n\\n    The following properties are to be updated:\\n\\t- metamer: length of the leaf, start_tt, end_tt, insertion_angle\\n        - LeafElement: age, length( of the sector), color\\n\\t- StemElement : age,length,color\\n\\n    """\\n    # Detect type of node (stem or leaf) \\n    if \\\'Leaf\\\' in n.label:\\n        #update metamer parameters (not to be changed)\\n        metamer = n.complex()\\n        if metamer.final_length is None:\\n            metamer.final_length = n.final_length\\n        metamer.start_insertion = 0\\n        metamer.end_insertion = n.Linc\\n\\n        #compute age\\t    \\n        n.age = n.end_tt\\n\\n        #colorise element\\n        n.color = 0,180,0\\n\\n        #compute length of the entire leaf\\n        \\n        metamer.length = metamer.final_length\\n\\n        #compute length of the sector\\n        n.length = metamer.final_length * (n.end_tt -n.start_tt) / (metamer.end_tt -metamer.start_tt)\\n\\n        # Compute insertion angle of the leaf when passing on the first sector\\n        # dectect the first sector (not to be changed)\\n        if (n.start_tt <= time < n.end_tt) or ((time > metamer.end_tt) and n.edge_type()==\\\'+\\\') :\\n\\t    metamer.insertion_angle = metamer.end_insertion\\n\\n\\n\\t#fin  Leaf Element\\n\\t\\n    else:\\n        n.length = n.final_length\\n        n.age = 0 \\n        n.color = 0,90,0\\n\'')],
   26: [],
   27: [  (1, '110.0'),
          (2, '1.6000000000000001'),
          (3, '1.6000000000000001'),
          (4, '5')],
   28: [(0, '0'), (1, '1500.0'), (3, "'int64'")],
   29: [(0, '1')],
   30: [(0, "'C:/Users/fourniec/Desktop/distance.csv'")],
   31: [],
   32: [],
   33: [(0, '0.10000000000000001')],
   34: [  (0, '0.20000000000000001'),
          (1, '0.59999999999999998'),
          (2, '1.0'),
          (3, '0.69999999999999996')],
   35: [],
   36: [  (0, 'None'),
          (2, 'None'),
          (3, "'circle'"),
          (4, '10'),
          (5, "'solid'"),
          (6, "'blue'"),
          (7, 'True'),
          (8, 'True'),
          (9, "{'label': None}"),
          (10, '2')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-647.33725166078978, 91.445517705871538], 'userColor': None, 'useUserColor': False},
   3: {'position': [-264.61667837411221, 18.235695264082899], 'userColor': None, 'useUserColor': False},
   4: {'position': [-133.81906942530145, -84.973067510462613], 'userColor': None, 'useUserColor': False},
   5: {'position': [-877.3322917735004, 63.031161668397033], 'userColor': None, 'useUserColor': False},
   6: {  'position': [-426.3662957601191, -177.562239130855],
         'useUserColor': False,
         'userColor': None},
   7: {'position': [-280.33937538020911, -141.3137814336595], 'userColor': None, 'useUserColor': False},
   8: {'position': [-412.69185305852437, 375.68415971360236], 'userColor': None, 'useUserColor': False},
   9: {'position': [-660.53125394421431, 423.90630558728861], 'userColor': None, 'useUserColor': False},
   10: {'position': [-432.58118028091036, 93.138373830018381], 'userColor': None, 'useUserColor': False},
   11: {'position': [-83.684903971131789, -84.636056713762557], 'userColor': None, 'useUserColor': False},
   12: {'position': [-174.30275989038273, -29.375008838525986], 'userColor': None, 'useUserColor': False},
   13: {'position': [-404.84173628838943, 487.82868500124482], 'userColor': None, 'useUserColor': False},
   14: {'position': [-646.95209757822283, 144.5570620962329], 'userColor': None, 'useUserColor': False},
   15: {'position': [-635.47791093364845, 0.63906075107892946], 'userColor': None, 'useUserColor': False},
   16: {'position': [-573.56299708990855, 340.93597326920951], 'userColor': None, 'useUserColor': False},
   17: {'position': [-702.12611755575961, 231.73008536616928], 'userColor': None, 'useUserColor': False},
   18: {'position': [-493.3760249421872, 221.64977132794871], 'userColor': None, 'useUserColor': False},
   19: {'position': [-143.34879438495653, -131.56298631052479], 'userColor': None, 'useUserColor': False},
   20: {'position': [-617.98247651656789, 377.83809240601823], 'userColor': None, 'useUserColor': False},
   21: {'position': [-681.84735400495879, 281.7039282854048], 'userColor': None, 'useUserColor': False},
   22: {'visualStyle': 0, 'position': [-829.41464120135356, -39.437297313712264], 'color': None, 'text': 'Number of sectors / leaf', 'textColor': None, 'rectP2': (-1, -1)},
   23: {'position': [-784.45869367292312, 1.2037922647801071], 'userColor': None, 'useUserColor': False},
   24: {'position': [-941.9363918301533, 13.527135298635303], 'userColor': None, 'useUserColor': False},
   25: {'position': [-548.51116369127533, 96.623694274316705], 'userColor': None, 'useUserColor': False},
   26: {'position': [-605.62465564345712, 469.56427165392739], 'userColor': None, 'useUserColor': False},
   27: {'position': [-874.7587733467376, 120.96785766271395], 'userColor': None, 'useUserColor': False},
   28: {'position': [-656.08116000608527, 53.621357307731415], 'userColor': None, 'useUserColor': False},
   29: {'position': [-285.09477082109731, -14.791873182544558], 'userColor': None, 'useUserColor': False},
   30: {'position': [-365.59115243771453, 331.9477948514218], 'userColor': None, 'useUserColor': False},
   31: {'position': [-423.90630558728861, 435.12075811605285], 'userColor': None, 'useUserColor': False},
   32: {'position': [-35.432269627069978, -144.73844039712225], 'userColor': None, 'useUserColor': False},
   33: {'position': [-38.467270414011807, -179.83448918550513], 'userColor': None, 'useUserColor': False},
   34: {'position': [-144.25226405254418, -173.10271686305302], 'userColor': None, 'useUserColor': False},
   35: {'position': [-277.9260287412352, 54.815860339966768], 'userColor': None, 'useUserColor': False},
   36: {'position': [-328.58345909279251, 502.40747328863841], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='DiscreteTimeEvaluation',
                             )




sleep_leaf_sectors = Factory(name='filter leaf sectors',
                authors=' (wralea authors)',
                description='',
                category='time',
                nodemodule='alinea.adel.training.sleep',
                nodeclass='leaf_sectors',
                inputs=[{'interface': None, 'name': 'g', 'desc': 'MTG'}, {'interface': IInt, 'name': 'leaf number', 'value': 0, 'desc': '0: all, n: leaf numbre from the top'}, {'interface': IInt, 'name': 'latency', 'value': 350, 'desc': 'desease latency in degree.day'}],
                outputs=[{'name': 'g', 'desc': 'MTG'}, {'interface': ISequence, 'name': 'target sectors', 'desc': 'target sectors that can be infected'}, {'interface': ISequence, 'name': 'source sectors', 'desc': 'source sectors of the infection'}],
                widgetmodule=None,
                widgetclass=None,
               )



