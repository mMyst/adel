# -*- python -*-
#
#       Adel.PlantGen
#
#       Copyright 2006-2012 INRIA - CIRAD - INRA
#
#       File author(s): Camille Chambon <camille.chambon@grignon.inra.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
'''
Front end for the generation of the input data expected by ADEL. User should 
look at this module first. One can then look at the other modules of :mod:`alinea.adel.plantgen` 
for additional information. 

Authors: Mariem Abichou, Camille Chambon, Bruno Andrieu 
'''

import numpy as np
import pandas
import warnings

from adel.plantgen import axeT, dimT, dynT, phenT, tools, params

warnings.simplefilter('always', tools.InputWarning)

class DataCompleteness:
    '''
    This enumerate defines the different degrees of completeness that the data 
    documented by the user can have.
    
    .. seealso:: :func:`gen_adel_input_data`  
    '''
    MIN=1
    SHORT=2
    FULL=3


def gen_adel_input_data_from_min(dynT_user={'a_cohort': 0.0102, 'TT_col_0': -0.771289027, 'n0': 4.871559739, 'n1': 3.24283148, 'n2': 5.8,
                                            'TT_col_N_phytomer': {'MS': 1078.0, 'T1': 1148.0, 'T2': 1158.0, 'T3': 1168.0, 'T4': 1178.0}},
                                 dimT_user=None,
                                 plant_number=100, 
                                 decide_child_axis_probabilities={'T0': 0.0, 'T1': 0.900, 'T2': 0.983, 'T3': 0.817, 'T4': 0.117}, 
                                 MS_leaves_number_probabilities={'10': 0.145, '11': 0.818, '12': 0.037, '13': 0.0, '14': 0.0},
                                 TT_bolting=500.0,
                                 final_axes_density=250,
                                 GL_number={1117.0: 5.6, 1212.1:5.4, 1368.7:4.9, 1686.8:2.4, 1880.0:0.0}, 
                                 delais_TT_stop_del_axis=600,
                                 TT_col_break=0.0):
    '''
    Generate ADEL input data from a *MIN* set of data. This a convenience 
    function to be used from VisuAlea. 
    
    The *MIN* set of data is represented by *dynT_user*, *TT_col_N_phytomer* and *dimT_user*. 
    See :ref:`plantgen` for an example of how to set these parameters properly.
    
    :Parameters:
    
        - `dynT_user` (:class:`dict`) - the leaf dynamic parameters set by the user. See 
          :ref:`dynT_user_MIN <dynT_user_MIN>`
                      
          *dynT_user* must be a dict with the following content:: 
        
              {'a_cohort': a_cohort, 
               'TT_col_0': TT_col_0, 
               'n0': n0, 
               'n1': n1, 
               'n2': n2,
               'TT_col_N_phytomer': {'MS': TT_col_N_phytomer_MS, 
                                     'T1': TT_col_N_phytomer_T1, 
                                     'T2': TT_col_N_phytomer_T2,
                                     ...}}
        
          where ``a_cohort``, ``TT_col_0``, ``n0``, ``n1``, ``n2``, 
          ``TT_col_N_phytomer_MS``, ``TT_col_N_phytomer_T1`` and ``TT_col_N_phytomer_T2`` 
          are floats.
                
        - `dimT_user` (:class:`pandas.DataFrame`) - the dimensions of the organs set by 
          the user. See :ref:`dimT_user_MIN <dimT_user_MIN>`.
          
          *dimT_user* must be a pandas.Dataframe with the 
          following columns: *index_phytomer*, *L_blade*, *W_blade*, *L_sheath*, 
          *W_sheath*, *L_internode*, *W_internode*.
          The values can be either integers or floats.
              
        - `plant_number` (:class:`int`) - the number of plants to be generated.
        
        - `decide_child_axis_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          for each child axis the probability of emergence of an axis when the parent 
          axis is present. The keys are the identifiers of the child axes ('T0', 'T1', 
          'T2', ...) and the values are the probabilities.
        
        - `MS_leaves_number_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          the probability distribution of the final number of main stem leaves. 
          The keys are the final numbers of main stem leaves, and the values are 
          the probability distribution.
          
        - `TT_bolting` (:class:`int`) - date in thermal time at which the bolting starts.
        
        - `final_axes_density` (:class:`int`) - the final number of axes which have an 
          ear, per square meter.
        
        - `GL_number` (:class:`dict` of :class:`float`::class:`float`) - the GL 
          decimal numbers measured at several thermal times (including the 
          senescence end). The keys are the thermal times, and the values are 
          the GL decimal numbers.
        
        - `delais_TT_stop_del_axis` (:class:`int`) - This variable represents the time in 
          thermal time between an axis stop growing and its disappearance (it 
          concerns only the axes that do not regress and which do not produce any 
          cob).
        
        - `TT_col_break` (:class:`float`) - the thermal time when the rate of Haun Stage 
          is changing. If phyllochron is constant, then *TT_col_break* is null.
        
    :Returns:
        Return the following dataframes: :ref:`axeT <axeT>`, :ref:`dimT <dimT>`, 
        :ref:`phenT <phenT>`, :ref:`phenT_abs <phenT_abs>`, :ref:`dimT_abs <dimT_abs>`, 
        :ref:`dynT <dynT>`, :ref:`phenT_first <phenT_first>`, 
        :ref:`HS_GL_SSI_T <HS_GL_SSI_T>`, :ref:`tilleringT <tilleringT>`, 
        :ref:`cardinalityT <cardinalityT>`
    
    :Returns Type:
        tuple of :class:`pandas.DataFrame`
        
    .. seealso:: :ref:`plantgen`
                 :func:`gen_adel_input_data`
                 :mod:`alinea.adel.plantgen.axeT`
                 :mod:`alinea.adel.plantgen.dimT`
                 :mod:`alinea.adel.plantgen.dynT`
                 :mod:`alinea.adel.plantgen.params`
                 :mod:`alinea.adel.plantgen.phenT`
                 :mod:`alinea.adel.plantgen.tools`
                 
    '''
    id_axis_array = np.array(dynT_user['TT_col_N_phytomer'].keys())
    TT_col_N_phytomer_array = np.array(dynT_user['TT_col_N_phytomer'].values())
    dynT_user_dataframe = pandas.DataFrame(index=range(id_axis_array.size),
                                           columns=['id_axis', 'a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2'],
                                           dtype=float)
    dynT_user_dataframe['id_axis'] = id_axis_array
    dynT_user_dataframe['TT_col_N_phytomer'] = TT_col_N_phytomer_array
    MS_index = dynT_user_dataframe[dynT_user_dataframe['id_axis'] == 'MS'].index
    for key, value in dynT_user.iteritems():
        if key == 'TT_col_N_phytomer':
            continue
        dynT_user_dataframe[key][MS_index] = value
    
    return gen_adel_input_data(dynT_user_dataframe, dimT_user, plant_number, decide_child_axis_probabilities, MS_leaves_number_probabilities, TT_bolting, final_axes_density, GL_number, delais_TT_stop_del_axis, TT_col_break, DataCompleteness.MIN, DataCompleteness.MIN)


def gen_adel_input_data_from_short(dynT_user,
                                   dimT_user,
                                   plant_number=100, 
                                   decide_child_axis_probabilities={'T0': 0.0, 'T1': 0.900, 'T2': 0.983, 'T3': 0.817, 'T4': 0.117}, 
                                   MS_leaves_number_probabilities={'10': 0.145, '11': 0.818, '12': 0.037, '13': 0.0, '14': 0.0},
                                   TT_bolting=500.0,
                                   final_axes_density=250,
                                   GL_number={1117.0: 5.6, 1212.1:5.4, 1368.7:4.9, 1686.8:2.4, 1880.0:0.0}, 
                                   delais_TT_stop_del_axis=600,
                                   TT_col_break=0.0):
    '''
    Generate ADEL input data from a *SHORT* set of data. This a convenience 
    function to be used from VisuAlea. 
    
    The *SHORT* set of data is represented by *dynT_user* and *dimT_user*.
    See :ref:`plantgen` for an example of how to set these parameters properly.
    
    :Parameters:
    
        - `dynT_user` (:class:`pandas.DataFrame`) - the leaf dynamic parameters 
          set by the user. See :ref:`dynT_user_SHORT <dynT_user_SHORT>`.
               
          *dynT_user* must be a pandas.Dataframe with the 
          following columns: *id_axis*, *a_cohort*, *TT_col_0*, *TT_col_N_phytomer*, *n0*, *n1*, *n2*.
          The values can be either integers or floats.
        
        - `dimT_user` (:class:`pandas.DataFrame`) - the dimensions of the organs set by 
          the user. See :ref:`dimT_user_SHORT <dimT_user_SHORT>`
          
          *dimT_user* must be a pandas.Dataframe with the 
          following columns: *id_axis*, *index_phytomer*, *L_blade*, *W_blade*, 
          *L_sheath*, *W_sheath*, *L_internode*, *W_internode*.
          The values of *id_axis* are strings like 'MS', 'T0', 'T1.2',... The 
          values of the other columns can be either integers or floats.
              
        - `plant_number` (:class:`int`) - the number of plants to be generated.
        
        - `decide_child_axis_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          for each child cohort the probability of emergence of an axis when the parent 
          axis is present. The keys are the identifiers of the child axes ('T0', 'T1', 
          'T2', ...) and the values are the probabilities.
        
        - `MS_leaves_number_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          the probability distribution of the final number of main stem leaves. 
          The keys are the final numbers of main stem leaves, and the values are 
          the probability distribution.
          
        - `TT_bolting` (:class:`int`) - date in thermal time at which the bolting starts.
        
        - `final_axes_density` (:class:`int`) - the final number of axes which have an 
          ear, per square meter.
        
        - `GL_number` (:class:`dict` of :class:`float`::class:`float`) - the GL decimal numbers measured at 
          several thermal times (including the senescence end). The keys are the 
          thermal times, and the values are the GL decimal numbers.
        
        - `delais_TT_stop_del_axis` (:class:`int`) - This variable represents the time in 
          thermal time between an axis stop growing and its disappearance (it 
          concerns only the axes that do not regress and which do not produce any 
          cob).
        
        - `TT_col_break` (:class:`float`) - the thermal time when the rate of Haun Stage 
          is changing. If phyllochron is constant, then *TT_col_break* is null.
        
    :Returns:
        Return the following dataframes: :ref:`axeT <axeT>`, :ref:`dimT <dimT>`, 
        :ref:`phenT <phenT>`, :ref:`phenT_abs <phenT_abs>`, :ref:`dimT_abs <dimT_abs>`, 
        :ref:`dynT <dynT>`, :ref:`phenT_first <phenT_first>`, 
        :ref:`HS_GL_SSI_T <HS_GL_SSI_T>`, :ref:`tilleringT <tilleringT>`,
        :ref:`cardinalityT <cardinalityT>`
    
    :Returns Type:
        tuple of :class:`pandas.DataFrame`
        
    .. seealso:: :ref:`plantgen`
                 :func:`gen_adel_input_data`
                 :mod:`alinea.adel.plantgen.axeT`
                 :mod:`alinea.adel.plantgen.dimT`
                 :mod:`alinea.adel.plantgen.dynT`
                 :mod:`alinea.adel.plantgen.params`
                 :mod:`alinea.adel.plantgen.phenT`
                 :mod:`alinea.adel.plantgen.tools`
                 
    '''    
    return gen_adel_input_data(dynT_user, dimT_user, plant_number, decide_child_axis_probabilities, MS_leaves_number_probabilities, TT_bolting, final_axes_density, GL_number, delais_TT_stop_del_axis, TT_col_break, DataCompleteness.SHORT, DataCompleteness.SHORT)
    

def gen_adel_input_data_from_full(dynT_user,
                                  dimT_user,
                                  plant_number=100, 
                                  decide_child_axis_probabilities={'T0': 0.0, 'T1': 0.900, 'T2': 0.983, 'T3': 0.817, 'T4': 0.117}, 
                                  MS_leaves_number_probabilities={'10': 0.145, '11': 0.818, '12': 0.037, '13': 0.0, '14': 0.0},
                                  TT_bolting=500.0,
                                  final_axes_density=250,
                                  GL_number={1117.0: 5.6, 1212.1:5.4, 1368.7:4.9, 1686.8:2.4, 1880.0:0.0}, 
                                  delais_TT_stop_del_axis=600,
                                  TT_col_break=0.0):
    '''
    Generate ADEL input data from a *FULL* set of data. This a convenience 
    function to be used from VisuAlea. 
    
    *FULL* set of data is represented by *dynT_user* and *dimT_user*.
    See :ref:`plantgen` for an example of how to set these parameters properly.
    
    :Parameters:
    
        - `dynT_user` (:class:`pandas.DataFrame`) - the leaf dynamic parameters 
          set by the user. See :ref:`dynT_user_FULL <dynT_user_FULL>`.
               
          *dynT_user* must be a pandas.Dataframe with the 
          following columns: *id_axis*, *N_phytomer*, *a_cohort*, *TT_col_0*, *TT_col_N_phytomer*, *n0*, *n1*, *n2*.
          The values can be either integers or floats.
        
        - `dimT_user` (:class:`pandas.DataFrame`) - the dimensions of the organs set by 
          the user. See :ref:`dimT_user_FULL <dimT_user_FULL>`.
          
          *dimT_user* must be a pandas.Dataframe with the 
          following columns: *id_dim*, *index_phytomer*, *L_blade*, *W_blade*, 
          *L_sheath*, *W_sheath*, *L_internode*, *W_internode*.
          The values can be either integers or floats.
              
        - `plant_number` (:class:`int`) - the number of plants to be generated.
        
        - `decide_child_axis_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          for each child cohort the probability of emergence of an axis when the parent 
          axis is present. The keys are the identifiers of the child axes ('T0', 'T1', 
          'T2', ...) and the values are the probabilities.
        
        - `MS_leaves_number_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          the probability distribution of the final number of main stem leaves. 
          The keys are the final numbers of main stem leaves, and the values are 
          the probability distribution.
          
        - `TT_bolting` (:class:`int`) - date in thermal time at which the bolting starts.
        
        - `final_axes_density` (:class:`int`) - the final number of axes which have an 
          ear, per square meter.
        
        - `GL_number` (:class:`dict` of :class:`float`::class:`float`) - the GL decimal numbers measured at 
          several thermal times (including the senescence end). The keys are the 
          thermal times, and the values are the GL decimal numbers.
        
        - `delais_TT_stop_del_axis` (:class:`int`) - This variable represents the time in 
          thermal time between an axis stop growing and its disappearance (it 
          concerns only the axes that do not regress and which do not produce any 
          cob).
        
        - `TT_col_break` (:class:`float`) - the thermal time when the rate of Haun Stage 
          is changing. If phyllochron is constant, then *TT_col_break* is null.
          
    :Returns:
        Return the following dataframes: :ref:`axeT <axeT>`, :ref:`dimT <dimT>`, 
        :ref:`phenT <phenT>`, :ref:`phenT_abs <phenT_abs>`, :ref:`dimT_abs <dimT_abs>`, 
        :ref:`dynT <dynT>`, :ref:`phenT_first <phenT_first>`, 
        :ref:`HS_GL_SSI_T <HS_GL_SSI_T>`, :ref:`tilleringT <tilleringT>`,
        :ref:`cardinalityT <cardinalityT>`.
    
    :Returns Type:
        tuple of :class:`pandas.DataFrame`
        
    .. seealso:: :ref:`plantgen`
                 :func:`gen_adel_input_data`
                 :mod:`alinea.adel.plantgen.axeT`
                 :mod:`alinea.adel.plantgen.dimT`
                 :mod:`alinea.adel.plantgen.dynT`
                 :mod:`alinea.adel.plantgen.params`
                 :mod:`alinea.adel.plantgen.phenT`
                 :mod:`alinea.adel.plantgen.tools`
                 
    '''    
    return gen_adel_input_data(dynT_user, dimT_user, plant_number, decide_child_axis_probabilities, MS_leaves_number_probabilities, TT_bolting, final_axes_density, GL_number, delais_TT_stop_del_axis, TT_col_break, DataCompleteness.FULL, DataCompleteness.FULL)


def gen_adel_input_data(dynT_user,
                        dimT_user,
                        plant_number=100, 
                        decide_child_axis_probabilities={'T0': 0.0, 'T1': 0.900, 'T2': 0.983, 'T3': 0.817, 'T4': 0.117}, 
                        MS_leaves_number_probabilities={'10': 0.145, '11': 0.818, '12': 0.037, '13': 0.0, '14': 0.0},
                        TT_bolting=500.0,
                        final_axes_density=250,
                        GL_number={1117.0: 5.6, 1212.1:5.4, 1368.7:4.9, 1686.8:2.4, 1880.0:0.0}, 
                        delais_TT_stop_del_axis=600,
                        TT_col_break=0.0,
                        dynT_user_completeness=DataCompleteness.MIN,
                        dimT_user_completeness=DataCompleteness.MIN                        
                        ):
    '''
    Create the dataframes which contain the plant data to be used as input for 
    generating plot with ADEL, and some other dataframes for debugging purpose.
    See :ref:`adel_input` for a description of the input tables expected by ADEL, 
    and :ref:`plantgen` for a description of the dataframes created for debug. 
    
    Different degrees of completeness of data provided by the user are acceptable. 
    The user must specify the degree of completeness selecting a value within the 
    enumerate :class:`DataCompleteness`.
    
    The dataframes are created as follows:
        * initialization of the following dataframes:
            * *axeT_tmp*, calling :func:`alinea.adel.plantgen.axeT.create_axeT_tmp`,
            * *dynT_tmp*, calling :func:`alinea.adel.plantgen.dynT.create_dynT_tmp`.
            * *dimT_tmp*, calling :func:`alinea.adel.plantgen.dimT.create_dimT_tmp`
            * :ref:`tilleringT <tilleringT>`, calling :func:`alinea.adel.plantgen.axeT.create_tilleringT`
            * :ref:`cardinalityT <cardinalityT>`, calling :func:`alinea.adel.plantgen.axeT.create_cardinalityT`
        * filling of the dataframes set by the user:
            * *dynT_user*, according to *dynT_user_completeness*
            * *dimT_user*, according to *dimT_user_completeness*
        * calculate the number of elongated internodes
        * construction of the following dataframes:
            * :ref:`dynT <dynT>`, calling :func:`alinea.adel.plantgen.dynT.create_dynT`,
            * :ref:`phenT_abs <phenT_abs>`, calling :func:`alinea.adel.plantgen.phenT.create_phenT_abs`,
            * :ref:`phenT_first <phenT_first>`, calling :func:`alinea.adel.plantgen.phenT.create_phenT_first`,
            * :ref:`phenT <phenT>`, calling :func:`alinea.adel.plantgen.phenT.create_phenT`,
            * :ref:`axeT <axeT>`, calling :func:`alinea.adel.plantgen.axeT.create_axeT`,
            * :ref:`dimT_abs <dimT_abs>`, calling :func:`alinea.adel.plantgen.dimT.create_dimT_abs`,
            * :ref:`dimT <dimT>`, calling :func:`alinea.adel.plantgen.dimT.create_dimT`,
            * :ref:`HS_GL_SSI_T <HS_GL_SSI_T>`, calling :func:`alinea.adel.plantgen.phenT.create_HS_GL_SSI_T`,

        These tables are returned to be used as ADEL input:
            * the :ref:`axeT <axeT>`, 
            * the :ref:`dimT <dimT>`, 
            * the :ref:`phenT <phenT>`.
          
        These tables are intermediate tables and are returned for debugging purpose:
            * the :ref:`tilleringT <tilleringT>`,
            * the :ref:`cardinalityT <cardinalityT>`,
            * the :ref:`phenT_abs <phenT_abs>`,
            * the :ref:`dimT_abs <dimT_abs>`,
            * the :ref:`dynT <dynT>`, 
            * the :ref:`phenT_first <phenT_first>`,
            * the :ref:`HS_GL_SSI_T <HS_GL_SSI_T>`,
        
    :Parameters:
    
        - `dynT_user` (:class:`pandas.DataFrame`) - the leaf dynamic 
          parameters set by the user.
          The content depend on the *dynT_user_completeness*.
          See :ref:`levels_of_completeness`.       
                
        - `dimT_user` (:class:`pandas.DataFrame`) - the dimensions of the organs 
          set by the user. 
          The content depends on the *dimT_user_completeness* argument. 
          See :ref:`levels_of_completeness`.
              
        - `plant_number` (:class:`int`) - the number of plants to be generated.
        
        - `decide_child_axis_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          for each child cohort the probability of emergence of an axis when the parent 
          axis is present. The keys are the identifiers of the child axes ('T0', 'T1', 
          'T2', ...) and the values are the probabilities.
        
        - `MS_leaves_number_probabilities` (:class:`dict` of :class:`str`::class:`float`) - 
          the probability distribution of the final number of main stem leaves. 
          The keys are the final numbers of main stem leaves, and the values are 
          the probabilities distribution.
          
        - `TT_bolting` (:class:`int`) - date in thermal time at which the bolting starts.
        
        - `final_axes_density` (:class:`int`) - the final number of axes which have an 
          ear, per square meter.
        
        - `GL_number` (:class:`dict` of :class:`float`::class:`float`) - the GL decimal numbers measured at 
          several thermal times (including the senescence end). The keys are the 
          thermal times, and the values are the GL decimal numbers.
        
        - `delais_TT_stop_del_axis` (:class:`int`) - This variable represents the time in 
          thermal time between an axis stop growing and its disappearance (it 
          concerns only the axes that do not regress and which do not produce any 
          cob).
        
        - `TT_col_break` (:class:`float`) - the thermal time when the rate of Haun Stage 
          is changing. If phyllochron is constant, then *TT_col_break* is null.
          
        - `dynT_user_completeness` (:class:`DataCompleteness`) - the level of 
          completeness of the *dynT_user* set by the user. 
        
        - `dimT_user_completeness` (:class:`DataCompleteness`) - the level of completeness of the 
          *dimT_user* set by the user. 
        
    :Returns:
        Return the following dataframes: :ref:`axeT <axeT>`, :ref:`dimT <dimT>`, 
        :ref:`phenT <phenT>`, :ref:`phenT_abs <phenT_abs>`, :ref:`dimT_abs <dimT_abs>`, 
        :ref:`dynT <dynT>`, :ref:`phenT_first <phenT_first>`, :ref:`HS_GL_SSI_T <HS_GL_SSI_T>`, 
        :ref:`tilleringT <tilleringT>`, :ref:`cardinalityT <cardinalityT>`.
    
    :Returns Type:
        tuple of :class:`pandas.DataFrame`
        
    .. seealso:: :class:`DataCompleteness`
                 :mod:`alinea.adel.plantgen.axeT`
                 :mod:`alinea.adel.plantgen.dimT`
                 :mod:`alinea.adel.plantgen.dynT`
                 :mod:`alinea.adel.plantgen.params`
                 :mod:`alinea.adel.plantgen.phenT`
                 :mod:`alinea.adel.plantgen.tools`
                 
    '''
    
    if dynT_user_completeness not in DataCompleteness.__dict__.values():
        raise tools.InputError("dynT_user_completeness is not one of: %s" % ', '.join(DataCompleteness.__dict__.values()))
    
    if dimT_user_completeness not in DataCompleteness.__dict__.values():
        raise tools.InputError("dimT_user_completeness is not one of: %s" % ', '.join(DataCompleteness.__dict__.values()))
    
    possible_axes = \
        set([id_axis for (id_axis, probability) in
             decide_child_axis_probabilities.iteritems() if probability != 0.0])
        
    possible_MS_N_phytomer = \
        set([MS_N_phytomer for (MS_N_phytomer, probability) in
             MS_leaves_number_probabilities.iteritems() if probability != 0.0])
        
    decide_child_cohort_probabilities = tools.calculate_decide_child_cohort_probabilities(decide_child_axis_probabilities)
        
    # check plant_number, decide_child_cohort_probabilities and final_axes_density validity
    theoretical_cohort_cardinalities = tools.calculate_theoretical_cardinalities(plant_number, 
                                                                                 decide_child_cohort_probabilities,
                                                                                 params.FIRST_CHILD_DELAY)
    theoretical_cardinalities_sum = sum(theoretical_cohort_cardinalities.values())
    if final_axes_density > int(theoretical_cardinalities_sum):
        raise tools.InputError("final_axes_density (%s) lesser than the sum of the theoretical cardinalities (%s)" % (final_axes_density, int(theoretical_cardinalities_sum)))
    
    available_axes_warning_message = "the probabilities defined in decide_child_axis_probabilities (%s) and \
the axes documented by the user (%s) in %s indicate that some of the possible axes (%s) \
are not documented by the user. After the generation of the axes, if not all generated axes are documented by the user, \
then this will lead to an error."

    available_MS_N_phytomer_warning_message = "the probabilities defined in MS_leaves_number_probabilities (%s) and \
the N_phytomer of the MS documented by the user (%s) in %s indicate that some of the N_phytomer of the MS (%s) \
are not documented by the user. After the generation of the phytomers of the MS, if not all generated phytomers \
of the MS are documented by the user, then this will lead to an error."
    
    # check dynT_user validity
    if dynT_user_completeness == DataCompleteness.MIN:
        expected_dynT_user_columns = ['id_axis', 'a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2']
        if dynT_user.columns.tolist() != expected_dynT_user_columns:
            raise tools.InputError("dynT_user does not have the columns: %s" % ', '.join(expected_dynT_user_columns))
        available_axes = set(dynT_user['id_axis'].tolist())
        if not possible_axes.issubset(available_axes):
            warnings.warn(available_axes_warning_message % (decide_child_axis_probabilities,
                                                            list(available_axes),
                                                            'dynT_user',
                                                            list(possible_axes)), 
                          tools.InputWarning)
    elif dynT_user_completeness == DataCompleteness.SHORT:
        expected_dynT_user_columns = ['id_axis', 'a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2']
        if dynT_user.columns.tolist() != expected_dynT_user_columns:
            raise tools.InputError("dynT_user does not have the columns: %s" % ', '.join(expected_dynT_user_columns))
        if dynT_user['id_axis'].unique().size != dynT_user['id_axis'].size:
            raise tools.InputError("dynT_user contains duplicated id_axis")
        available_axes = set(dynT_user['id_axis'].tolist())
        if not possible_axes.issubset(available_axes):
            warnings.warn(available_axes_warning_message % (decide_child_axis_probabilities,
                                                            list(available_axes),
                                                            'dynT_user',
                                                            list(possible_axes)),
                          tools.InputWarning)
    elif dynT_user_completeness == DataCompleteness.FULL:
        expected_dynT_user_columns = ['id_axis', 'N_phytomer', 'a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2']
        if dynT_user.columns.tolist() != expected_dynT_user_columns:
            raise tools.InputError("dynT_user does not have the columns: %s" % ', '.join(expected_dynT_user_columns))
        grouped = dynT_user.groupby(['id_axis', 'N_phytomer'])
        if len(grouped.groups) != dynT_user.index.size:
            raise tools.InputError("dynT_user contains duplicated (id_axis, N_phytomer) pair(s)")
        available_axes = set(dynT_user['id_axis'].tolist())
        if not possible_axes.issubset(available_axes):
            warnings.warn(available_axes_warning_message % (decide_child_axis_probabilities,
                                                            list(available_axes),
                                                            'dynT_user',
                                                            list(possible_axes)),
                          tools.InputWarning)
        available_MS_N_phytomer = set(dynT_user[dynT_user['id_axis'] == 'MS']['N_phytomer'].tolist())
        if not possible_MS_N_phytomer.issubset(available_MS_N_phytomer):
            warnings.warn(available_MS_N_phytomer_warning_message % (MS_leaves_number_probabilities,
                                                                     list(available_MS_N_phytomer),
                                                                     'dynT_user',
                                                                     list(possible_MS_N_phytomer)),
                          tools.InputWarning)
    
    # check dimT_user validity
    if dimT_user_completeness == DataCompleteness.MIN:
        expected_dimT_user_columns = ['index_phytomer', 'L_blade', 'W_blade', 'L_sheath', 'W_sheath', 'L_internode', 'W_internode']
        if dimT_user.columns.tolist() != expected_dimT_user_columns:
            raise tools.InputError("dimT_user does not have the columns: %s" % ', '.join(expected_dimT_user_columns))
        if dimT_user['index_phytomer'].unique().size != dimT_user['index_phytomer'].size:
            raise tools.InputError("dimT_user contains duplicated index_phytomer")
        max_available_MS_N_phytomer = dimT_user['index_phytomer'].max()
        if max(possible_MS_N_phytomer) > max_available_MS_N_phytomer:
            warnings.warn(available_MS_N_phytomer_warning_message % (MS_leaves_number_probabilities,
                                                                     ', '.join([str(max_available_MS_N_phytomer)]),
                                                                     'dimT_user',
                                                                     ', '.join([str(max(possible_MS_N_phytomer))])),
                          tools.InputWarning)
            
    elif dimT_user_completeness == DataCompleteness.SHORT:
        expected_dimT_user_columns = ['id_axis', 'index_phytomer', 'L_blade', 'W_blade', 'L_sheath', 'W_sheath', 'L_internode', 'W_internode']
        if dimT_user.columns.tolist() != expected_dimT_user_columns:
            raise tools.InputError("dimT_user does not have the columns: %s" % ', '.join(expected_dimT_user_columns))
        grouped = dimT_user.groupby(['id_axis', 'index_phytomer'])
        if len(grouped.groups) != dimT_user.index.size:
            raise tools.InputError("dimT_user contains duplicated (id_axis, index_phytomer) pair(s)")
        available_axes = set(dimT_user['id_axis'].tolist())
        if not possible_axes.issubset(available_axes):
            warnings.warn(available_axes_warning_message % (decide_child_axis_probabilities,
                                                            list(available_axes),
                                                            'dimT_user',
                                                            list(possible_axes)),
                          tools.InputWarning)
        max_available_MS_N_phytomer = dimT_user[dimT_user['id_axis'] == 'MS']['index_phytomer'].max()
        if max(possible_MS_N_phytomer) > max_available_MS_N_phytomer:
            warnings.warn(available_MS_N_phytomer_warning_message % (MS_leaves_number_probabilities,
                                                                     ', '.join([str(max_available_MS_N_phytomer)]),
                                                                     'dimT_user',
                                                                     ', '.join([str(max(possible_MS_N_phytomer))])),
                          tools.InputWarning)
    elif dimT_user_completeness == DataCompleteness.FULL:
        expected_dimT_user_columns = ['id_axis', 'N_phytomer', 'index_phytomer', 'L_blade', 'W_blade', 'L_sheath', 'W_sheath', 'L_internode', 'W_internode']
        if dimT_user.columns.tolist() != expected_dimT_user_columns:
            raise tools.InputError("dimT_user does not have the columns: %s" % ', '.join(expected_dimT_user_columns))
        grouped = dimT_user.groupby(['id_axis', 'N_phytomer', 'index_phytomer'])
        if len(grouped.groups) != dimT_user.index.size:
            raise tools.InputError("dimT_user contains duplicated (id_axis, N_phytomer, index_phytomer) triplet(s)")
        available_axes = set(dimT_user['id_axis'].tolist())
        if not possible_axes.issubset(available_axes):
            warnings.warn(available_axes_warning_message % (decide_child_axis_probabilities,
                                                            list(available_axes),
                                                            'dimT_user',
                                                            list(possible_axes)),
                          tools.InputWarning)
        available_MS_N_phytomer = set(dimT_user[dimT_user['id_axis'] == 'MS']['N_phytomer'].tolist())
        if not possible_MS_N_phytomer.issubset(available_MS_N_phytomer):
            warnings.warn(available_MS_N_phytomer_warning_message % (MS_leaves_number_probabilities,
                                                                     list(available_MS_N_phytomer),
                                                                     'dimT_user',
                                                                     list(possible_MS_N_phytomer)),
                          tools.InputWarning)
    
    # 2. first step of the fit process
    (axeT_tmp, 
     dimT_tmp, 
     dynT_tmp, 
     cardinalityT) = _gen_adel_input_data_first(plant_number, 
                                                decide_child_cohort_probabilities, 
                                                MS_leaves_number_probabilities, 
                                                theoretical_cohort_cardinalities)
     
    most_frequent_dynT_tmp = pandas.DataFrame(columns=dynT_tmp.columns)
    for id_axis, dynT_tmp_group in dynT_tmp.groupby('id_axis'):
        idxmax = dynT_tmp_group['cardinality'].idxmax()
        most_frequent_dynT_tmp = pandas.concat([most_frequent_dynT_tmp, dynT_tmp_group.ix[idxmax:idxmax]], ignore_index=True)
    most_frequent_dynT_tmp_grouped = most_frequent_dynT_tmp.groupby(['id_axis', 'N_phytomer'])
    
    # 3. complete dynT_tmp
    if dynT_user_completeness == DataCompleteness.MIN:
        dynT_user_grouped = dynT_user.groupby('id_axis')
        MS_dynT_user = dynT_user_grouped.get_group('MS')
        MS_TT_col_N_phytomer = MS_dynT_user['TT_col_N_phytomer'][MS_dynT_user.first_valid_index()]
        for id_axis, dynT_tmp_group in dynT_tmp.groupby('id_axis'):
            if not dynT_user['id_axis'].isin([id_axis]).any():
                id_axis = tools.get_primary_axis(id_axis, params.FIRST_CHILD_DELAY)
            dynT_user_group = dynT_user_grouped.get_group(id_axis)
            index_to_get = dynT_user_group.index[0]
            index_to_set = dynT_tmp_group.index[0]
            if id_axis == 'MS':
                for column in ['a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2']:
                    dynT_tmp[column][index_to_set] = dynT_user[column][index_to_get]
            dynT_tmp['TT_col_break'][index_to_set] = TT_col_break
            current_TT_col_N_phytomer = dynT_user_group['TT_col_N_phytomer'][index_to_get]
            current_dTT_MS_cohort = current_TT_col_N_phytomer - MS_TT_col_N_phytomer
            dynT_tmp['dTT_MS_cohort'][index_to_set] = current_dTT_MS_cohort
    elif dynT_user_completeness == DataCompleteness.SHORT:
        dynT_user_grouped = dynT_user.groupby('id_axis')
        MS_dynT_user = dynT_user_grouped.get_group('MS')
        MS_TT_col_N_phytomer = MS_dynT_user['TT_col_N_phytomer'][MS_dynT_user.first_valid_index()]
        for id_axis, dynT_tmp_group in dynT_tmp.groupby('id_axis'):
            if not dynT_user['id_axis'].isin([id_axis]).any():
                id_axis = tools.get_primary_axis(id_axis, params.FIRST_CHILD_DELAY)
            dynT_user_group = dynT_user_grouped.get_group(id_axis)
            index_to_get = dynT_user_group.index[0]
            index_to_set = dynT_tmp_group.index[0]
            for column in ['a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2']:
                dynT_tmp[column][index_to_set] = dynT_user[column][index_to_get]
            dynT_tmp['TT_col_break'][index_to_set] = TT_col_break
            current_TT_col_N_phytomer = dynT_user_group['TT_col_N_phytomer'][index_to_get]
            current_dTT_MS_cohort = current_TT_col_N_phytomer - MS_TT_col_N_phytomer
            dynT_tmp['dTT_MS_cohort'][index_to_set] = current_dTT_MS_cohort
    elif dynT_user_completeness == DataCompleteness.FULL:
        dynT_user_grouped = dynT_user.groupby(['id_axis', 'N_phytomer'])
        MS_N_phytomer = dynT_tmp['N_phytomer'][dynT_tmp[dynT_tmp['id_axis'] == 'MS']['cardinality'].idxmax()]
        MS_dynT_user = dynT_user_grouped.get_group(('MS', MS_N_phytomer))
        MS_TT_col_N_phytomer = MS_dynT_user['TT_col_N_phytomer'][MS_dynT_user.first_valid_index()]
        for (id_axis, N_phytomer), dynT_tmp_group in dynT_tmp.groupby(['id_axis', 'N_phytomer']):
            if not dynT_user['id_axis'].isin([id_axis]).any():
                if most_frequent_dynT_tmp_grouped.groups.has_key((id_axis, N_phytomer)):
                    id_axis = tools.get_primary_axis(id_axis, params.FIRST_CHILD_DELAY)
                else:
                    continue
            if not dynT_user_grouped.groups.has_key((id_axis, N_phytomer)):
                if most_frequent_dynT_tmp_grouped.groups.has_key((id_axis, N_phytomer)):
                    raise tools.InputError("Dynamic of %s not documented" % ((id_axis, N_phytomer),))
                else:
                    most_frequent_dynT_tmp_id_axis = most_frequent_dynT_tmp[most_frequent_dynT_tmp['id_axis'] == id_axis]
                    N_phytomer = most_frequent_dynT_tmp_id_axis['N_phytomer'][most_frequent_dynT_tmp_id_axis.first_valid_index()]
                    if not dynT_user_grouped.groups.has_key((id_axis, N_phytomer)):
                        raise tools.InputError("Dynamic of %s not documented" % ((id_axis, N_phytomer),))
            dynT_user_group = dynT_user_grouped.get_group((id_axis, N_phytomer))
            index_to_get = dynT_user_group.index[0]
            index_to_set = dynT_tmp_group.index[0]
            for column in ['a_cohort', 'TT_col_0', 'TT_col_N_phytomer', 'n0', 'n1', 'n2']:
                dynT_tmp[column][index_to_set] = dynT_user[column][index_to_get]
            dynT_tmp['TT_col_break'][index_to_set] = TT_col_break
            current_TT_col_N_phytomer = dynT_user_group['TT_col_N_phytomer'][index_to_get]
            current_dTT_MS_cohort = current_TT_col_N_phytomer - MS_TT_col_N_phytomer
            dynT_tmp['dTT_MS_cohort'][index_to_set] = current_dTT_MS_cohort

    # 4. complete dimT_tmp
    organ_dim_list = ['L_blade', 'W_blade', 'L_sheath', 'W_sheath', 'L_internode', 'W_internode']
    if dimT_user_completeness == DataCompleteness.MIN:
        MS_dynT_tmp = dynT_tmp[dynT_tmp['id_axis'] == 'MS']
        MS_most_frequent_N_phytomer = MS_dynT_tmp['N_phytomer'][MS_dynT_tmp['cardinality'].idxmax()]
        dimT_tmp_grouped = dimT_tmp.groupby(['id_axis', 'N_phytomer'])
        dimT_tmp_indexes_to_set = dimT_tmp_grouped.groups[('MS', MS_most_frequent_N_phytomer)]
        N_phytomer_to_set = len(dimT_tmp_indexes_to_set)
        max_available_MS_N_phytomer = dimT_user['index_phytomer'].max()
        if N_phytomer_to_set > max_available_MS_N_phytomer:
            raise tools.InputError("Dimensions of index_phytomer=%s not documented" % N_phytomer_to_set)
        dimT_user_indexes_to_get = range(len(dimT_tmp_indexes_to_set))
        for organ_dim in organ_dim_list:
            dimT_tmp[organ_dim][dimT_tmp_indexes_to_set] = dimT_user[organ_dim][dimT_user_indexes_to_get]
    elif dimT_user_completeness == DataCompleteness.SHORT:
        dimT_user_grouped = dimT_user.groupby('id_axis')
        dynT_tmp_grouped = dynT_tmp.groupby('id_axis')
        for id_axis, dimT_tmp_group in dimT_tmp.groupby('id_axis'):
            dynT_tmp_group = dynT_tmp_grouped.get_group(id_axis)
            N_phytomer = dynT_tmp_group['N_phytomer'][dynT_tmp_group['cardinality'].idxmax()]
            indexes_to_set = dimT_tmp_group[dimT_tmp_group['N_phytomer'] == N_phytomer].index
            if not dimT_user['id_axis'].isin([id_axis]).any():
                id_axis = tools.get_primary_axis(id_axis, params.FIRST_CHILD_DELAY)
            dimT_user_group = dimT_user_grouped.get_group(id_axis)
            max_available_N_phytomer = dimT_user_group['index_phytomer'].max()
            N_phytomer_to_set = len(indexes_to_set)
            if N_phytomer_to_set > max_available_N_phytomer:
                raise tools.InputError("Dimensions of %s not documented" % ((id_axis, N_phytomer_to_set),))
            indexes_to_get = dimT_user_group.index[:N_phytomer_to_set]
            for organ_dim in organ_dim_list:
                dimT_tmp[organ_dim][indexes_to_set] = dimT_user[organ_dim][indexes_to_get]
    elif dimT_user_completeness == DataCompleteness.FULL:
        dimT_user_grouped = dimT_user.groupby(['id_axis', 'N_phytomer'])
        for (id_axis, N_phytomer), dimT_tmp_group in dimT_tmp.groupby(['id_axis', 'N_phytomer']):
            if not dimT_user['id_axis'].isin([id_axis]).any():
                if most_frequent_dynT_tmp_grouped.groups.has_key((id_axis, N_phytomer)):
                    id_axis = tools.get_primary_axis(id_axis, params.FIRST_CHILD_DELAY)
                else:
                    continue
            indexes_to_set = dimT_tmp_group.index
            if not dimT_user_grouped.groups.has_key((id_axis, N_phytomer)):
                raise tools.InputError("Dimensions of %s not documented" % ((id_axis, N_phytomer),))
            indexes_to_get = dimT_user_grouped.get_group((id_axis, N_phytomer)).index
            for organ_dim in organ_dim_list:
                dimT_tmp[organ_dim][indexes_to_set] = dimT_user[organ_dim][indexes_to_get]
    
    # 5. second step of the fit process    
    (axeT_, 
     phenT_abs, 
     phenT_,
     dimT_abs, 
     dynT_, 
     phenT_first,
     HS_GL_SSI_T, 
     dimT_,
     tilleringT) = _gen_adel_input_data_second(axeT_tmp, 
                                               dimT_tmp, 
                                               dynT_tmp, 
                                               plant_number,
                                               GL_number, 
                                               TT_bolting, 
                                               delais_TT_stop_del_axis, 
                                               final_axes_density)
    
    return axeT_, dimT_, phenT_, phenT_abs, dimT_abs, dynT_, phenT_first, \
           HS_GL_SSI_T, tilleringT, cardinalityT


def _gen_adel_input_data_first(plant_number, 
                               decide_child_cohort_probabilities, 
                               MS_leaves_number_probabilities,
                               theoretical_cohort_cardinalities):    
    '''Generate the input data: first step.'''
    # create axeT_tmp
    axeT_tmp = axeT.create_axeT_tmp(plant_number, decide_child_cohort_probabilities, MS_leaves_number_probabilities)
    # create dynT_tmp
    dynT_tmp = dynT.create_dynT_tmp(axeT_tmp)
    # create dimT_tmp
    dimT_tmp = dimT.create_dimT_tmp(axeT_tmp)
    # create cardinalityT
    cardinalityT = axeT.create_cardinalityT(theoretical_cohort_cardinalities, axeT_tmp['id_cohort'])

    return axeT_tmp, dimT_tmp, dynT_tmp, cardinalityT


def _gen_adel_input_data_second(axeT_tmp, 
                                dimT_tmp, 
                                dynT_tmp,
                                plant_number, 
                                GL_number, 
                                TT_bolting, 
                                delais_TT_stop_del_axis,
                                final_axes_density):
    '''Generate the input data: second step.'''
    # calculate decimal_elongated_internode_number
    decimal_elongated_internode_number = dynT.calculate_decimal_elongated_internode_number(dimT_tmp, dynT_tmp) 
    # create dynT
    dynT_ = dynT.create_dynT(dynT_tmp, dimT_tmp, GL_number, decimal_elongated_internode_number)
    # create phenT_abs
    phenT_abs = phenT.create_phenT_abs(axeT_tmp, dynT_, decimal_elongated_internode_number)
    # create phenT_first
    phenT_first = phenT.create_phenT_first(phenT_abs)
    # create phenT
    phenT_ = phenT.create_phenT(phenT_abs, phenT_first)
    # calculate TT_flag_leaf_ligulation
    TT_flag_leaf_ligulation = dynT_['TT_col_N_phytomer'][dynT_.first_valid_index()]
    # create tilleringT
    tilleringT = axeT.create_tilleringT(0, TT_bolting, TT_flag_leaf_ligulation, plant_number, axeT_tmp, final_axes_density)
    # create axeT
    axeT_ = axeT.create_axeT(axeT_tmp, phenT_first, dynT_, TT_bolting, TT_flag_leaf_ligulation, delais_TT_stop_del_axis, final_axes_density)
    # create dimT_abs
    dimT_abs = dimT.create_dimT_abs(axeT_, dimT_tmp, phenT_abs, dynT_)
    # create dimT
    dimT_ = dimT.create_dimT(dimT_abs)
    # create HS_GL_SSI_T 
    HS_GL_SSI_T = phenT.create_HS_GL_SSI_T(phenT_abs, axeT_tmp, dynT_)
    
    return axeT_, phenT_abs, phenT_, dimT_abs, dynT_, phenT_first, HS_GL_SSI_T, dimT_, tilleringT
