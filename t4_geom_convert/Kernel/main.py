# -*- coding: utf-8 -*-
'''
Created on 6 févr. 2019

:author: Sogeti
:data : 06 february 2019
:file : main.py
'''
import argparse
import sys
from .FileHanlders.Writer.CWriteT4Geometry import CWriteT4Geometry
from .FileHanlders.Writer.CWriteT4Composition import CWriteT4Composition
from .FileHanlders.Writer.CWriteT4GeomComp import CWriteT4GeomComp
from .FileHanlders.Writer.CWriteT4BoundCond import CWriteT4BoundCond
from .Configuration.CConfigParameters import CConfigParameters

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f',"mcnp_file")
    args = parser.parse_args()
    sys.stdout.write(str(convert(args)))
    
def convert(args):
    CConfigParameters().setMCNPInputFile(args)
    CWriteT4Geometry().writeT4Geometry()
    CWriteT4Composition().writeT4Composition()
    CWriteT4GeomComp().writeT4GeomComp()
    CWriteT4BoundCond().writeT4BoundCond()
    return('File has been converted')

if __name__ == '__main__':
    main()
