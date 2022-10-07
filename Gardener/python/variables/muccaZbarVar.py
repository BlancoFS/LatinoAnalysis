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

class MuccaZbarVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createMuccaZbar(self):
        self.getMuccaZbar = ROOT.TMVA.Reader();
        
        # the order is important for TMVA!
        self.getMuccaZbar.AddVariable("mth",      (self.var1))
        self.getMuccaZbar.AddVariable("metTtrk",  (self.var2))
        self.getMuccaZbar.AddVariable("mtw2",     (self.var3))
        self.getMuccaZbar.AddVariable("drll",     (self.var4))
        self.getMuccaZbar.AddVariable("mll",      (self.var5))

        # I need to declare the spectator ... for some strange ROOT reasons ...
        #self.getMuccaMVAV.AddSpectator("std_vector_jet_pt[0]",   (self.var17))
       
        # mva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        #self.getMuccaMVAV.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/mucca/TMVAClassification_BDTG.weights.bkg" + self.kind + ".xml")
        self.getMuccaZbar.BookMVA("BDT","/afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_5/src/MUCCA/Optimization/Weights-Zbar_TTbar_5var/TMVAClassification_BDT4.weights.xml")


    def help(self):
        return '''Add mucca mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',   dest='kind',   help='Which background training to be used', default='1')
        group.add_option('-s', '--signal', dest='signal', help='Signal model', default='Zbar')
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
            raise RuntimeError('Missing parameter')
        self.kind      = opts.kind
        print((" kind   = ", self.kind))
        self.signal    = opts.signal
        print((" signal = ", self.signal))


    def process(self,**kwargs):

        self.getMuccaZbar = None

        self.var1  = array.array('f',[0])
        self.var2  = array.array('f',[0])
        self.var3  = array.array('f',[0])
        self.var4  = array.array('f',[0])
        self.var5  = array.array('f',[0])
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['muccamva'+ self.signal]

        self.clone(output,newbranches)

        muccamva = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('muccamva'+ self.signal,  muccamva,  'muccamva' + self.signal + '/F')

        self.createMuccaZbar()

        nentries = self.itree.GetEntries()
        print(('Total number of entries: ',nentries)) 

        # avoid dots to go faster
        itree = self.itree
        otree = self.otree


        print('- Starting eventloop')
        step = 5000
        for i in range(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print((i,'events processed.'))

            muccamva[0] = -9999.
            
            # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            
            if pt1>0 and pt2>0 : 
  
              self.var1[0] = itree.mth
              self.var2[0] = itree.metTtrk
              self.var3[0] = itree.mtw2
              self.var4[0] = itree.drll
              self.var5[0] = itree.mll
              
              muccamva[0] = self.getMuccaZbar.EvaluateMVA("BDT")
              
            otree.Fill()
            
        self.disconnect()
        print('- Eventloop completed')


