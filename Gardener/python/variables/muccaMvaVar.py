from LatinoAnalysis.Gardener.gardening import TreeCloner


import optparse
import os
import sys
import ROOT
import numpy
import array
import re
import warnings
import os.path
from math import *
import math



#
#    \  |                                                                               _)         |      |       
#   |\/ |  |   |   __|   __|   _` |      __ `__ \ \ \   /  _` |     \ \   /  _` |   __|  |   _` |  __ \   |   _ \ 
#   |   |  |   |  (     (     (   |      |   |   | \ \ /  (   |      \ \ /  (   |  |     |  (   |  |   |  |   __/ 
#  _|  _| \__,_| \___| \___| \__,_|     _|  _|  _|  \_/  \__,_|       \_/  \__,_| _|    _| \__,_| _.__/  _| \___| 
#                                                                                                                
#

class MuccaMvaVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createMuccaMVA(self):
        self.getMuccaMVAV = ROOT.TMVA.Reader();
        
        # the order is important for TMVA!
        self.getMuccaMVAV.AddVariable("std_vector_lepton_pt[0]", (self.var1))
        self.getMuccaMVAV.AddVariable("std_vector_lepton_pt[1]", (self.var2))
        self.getMuccaMVAV.AddVariable("mll",                     (self.var3))
        self.getMuccaMVAV.AddVariable("ptll",                    (self.var4))
        self.getMuccaMVAV.AddVariable("mth",                     (self.var5))
        self.getMuccaMVAV.AddVariable("mtw1",                    (self.var6))
        self.getMuccaMVAV.AddVariable("mtw2",                    (self.var7))
        self.getMuccaMVAV.AddVariable("dphill",                  (self.var8))
        self.getMuccaMVAV.AddVariable("drll",                    (self.var9))
        self.getMuccaMVAV.AddVariable("dphilmet1",               (self.var10))
        self.getMuccaMVAV.AddVariable("dphilmet2",               (self.var11))
        self.getMuccaMVAV.AddVariable("dphilmet",                (self.var12))
        self.getMuccaMVAV.AddVariable("mpmet",                   (self.var13))
        self.getMuccaMVAV.AddVariable("metPfType1",              (self.var14))
        self.getMuccaMVAV.AddVariable("metTtrk",                 (self.var15))

        # I need to declare the spectator ... for some strange ROOT reasons ...
        #self.getMuccaMVAV.AddSpectator("std_vector_jet_pt[0]",   (self.var17))
       
        # mva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        #self.getMuccaMVAV.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/mucca/TMVAClassification_BDTG.weights.bkg" + self.kind + ".xml")
        self.getMuccaMVAV.BookMVA("BDT","/afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_5/src/MUCCA/Optimization/Weights-TTbar/TMVAClassification_BDT4.weights.xml")


    def help(self):
        return '''Add mucca mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',   dest='kind', help='Which background training to be used', default='1')
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
            raise RuntimeError('Missing parameter')
        self.kind   = opts.kind
        print(" kind = ", self.kind)


    def process(self,**kwargs):

        self.getMuccaMVAV = None

        self.var1  = array.array('f',[0])
        self.var2  = array.array('f',[0])
        self.var3  = array.array('f',[0])
        self.var4  = array.array('f',[0])
        self.var5  = array.array('f',[0])
        self.var6  = array.array('f',[0])
        self.var7  = array.array('f',[0])
        self.var8  = array.array('f',[0])
        self.var9  = array.array('f',[0])
        self.var10 = array.array('f',[0])
        self.var11 = array.array('f',[0])
        self.var12 = array.array('f',[0])
        self.var13 = array.array('f',[0])
        self.var14 = array.array('f',[0])
        self.var15 = array.array('f',[0])
        #self.var17 = array.array('f',[0])
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['muccamva'+ self.kind]

        self.clone(output,newbranches)

        muccamva   = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('muccamva'+ self.kind,  muccamva,  'muccamva' + self.kind + '/F')

        self.createMuccaMVA()

        nentries = self.itree.GetEntries()
        print('Total number of entries: ',nentries) 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree


        print('- Starting eventloop')
        step = 5000
        for i in range(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print(i,'events processed.')

            muccamva[0] = -9999.
            
            # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            
            if pt1>0 and pt2>0 : 

              self.var1[0]   =  itree.std_vector_lepton_pt[0]
              self.var2[0]   =  itree.std_vector_lepton_pt[1]
              self.var3[0]   =  itree.mll
              self.var4[0]   =  itree.ptll
              self.var5[0]   =  itree.mth
              self.var6[0]   =  itree.mtw1
              self.var7[0]   =  itree.mtw2
              self.var8[0]   =  itree.dphill
              self.var9[0]   =  itree.drll
              self.var10[0]  =  itree.dphilmet1
              self.var11[0]  =  itree.dphilmet2
              self.var12[0]  =  itree.dphilmet
              self.var13[0]  =  itree.mpmet
              self.var14[0]  =  itree.metPfType1
              self.var15[0]  =  itree.metTtrk
              #self.var17[0]  =  itree.std_vector_jet_pt[0]
              
              muccamva[0] = self.getMuccaMVAV.EvaluateMVA("BDT")
              
            otree.Fill()
            
        self.disconnect()
        print('- Eventloop completed')


