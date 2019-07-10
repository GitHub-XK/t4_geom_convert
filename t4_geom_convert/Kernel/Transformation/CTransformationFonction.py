# -*- coding: utf-8 -*-
'''
Created on 6 févr. 2019
:author: Sogeti
:data : 06 february 2019
:file : CTransformationFonction.py
'''

from ...MIP import mip
from ...MIP.geom.forcad import translate
from ..Configuration.CConfigParameters import CConfigParameters
from ...MIP.geom.transforms import get_transforms
from ..Surface.ESurfaceTypeMCNP import ESurfaceTypeMCNP,\
    mcnp_to_mip
from ..Transformation.CSurfaceTransformed import CSurfaceTransformed
from ...MIP.geom.forcad import mcnp2cad, apply_transform
from ..Transformation.CTransformationQuad import CTransformationQuad

class CTransformationFonction(object):
    '''
    :brief: Class containing function to transform surface and volume
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def m_transformation(self,p_boundCond, trpl, p_typeSurface, l_paramSurface):
#         print('P_TYPESURFACE',p_typeSurface)
        if not trpl:
            return CSurfaceTransformed(\
                    p_boundCond, p_typeSurface, l_paramSurface)
        if p_typeSurface == ESurfaceTypeMCNP.GQ:
            p_typeSurface = 'gq'
        if p_typeSurface == 'gq':
            l_paramSurface = CTransformationQuad().m_transformationQuad(\
                                l_paramSurface, trpl)
        else:
#             print('typeSurface', type(p_typeSurface))
#             print('paramSurface', l_paramSurface)

            if isinstance(p_typeSurface, str):
                f = (l_paramSurface[0], l_paramSurface[1])
                p = (0,0,0)
                t = p_typeSurface
                s = l_paramSurface[2]
            else:
                t, f, s, p = mcnp2cad[mcnp_to_mip(p_typeSurface)](l_paramSurface)
            f, p = apply_transform(f, p, trpl)
            p_typeSurface, l_pparamSurface, l_complParam = t, f, s
#                     p_typeSurface, l_pparamSurface, l_complParam = \
#                     CTransformationFonction().m_transformation(k,surfaceParser)
            if p_typeSurface == 'k':
                new_complParam = list(l_complParam)
                if len(l_paramSurface) == 2 or len(l_paramSurface) == 4:
                    new_complParam.append(None)
                elif len(l_paramSurface) == 3 or len(l_paramSurface) == 5:
                    new_complParam.append(l_paramSurface[-1])
                else:
                    raise ValueError('Unexpected number of parameters for cone: %d' % len(l_paramSurface))
                l_paramSurface = l_pparamSurface[0], l_pparamSurface[1], tuple(new_complParam)
            else:
                l_paramSurface = l_pparamSurface[0], l_pparamSurface[1], l_complParam
#         print('CSurfaceTr', p_typeSurface, l_paramSurface)
        return CSurfaceTransformed(\
                    p_boundCond, p_typeSurface, l_paramSurface)
