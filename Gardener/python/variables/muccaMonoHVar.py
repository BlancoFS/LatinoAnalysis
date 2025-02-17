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

class MuccaMonoHVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createMuccaMonoH(self):
        self.getMuccaMonoH = ROOT.TMVA.Reader();
        
        # the order is important for TMVA!
        self.getMuccaMonoH.AddVariable("mth",      (self.var1))
        self.getMuccaMonoH.AddVariable("mtw2",     (self.var2))
        self.getMuccaMonoH.AddVariable("metTtrk",  (self.var3))
        self.getMuccaMonoH.AddVariable("drll",     (self.var4))
        self.getMuccaMonoH.AddVariable("ptll",     (self.var5))

        # I need to declare the spectator ... for some strange ROOT reasons ...
        #self.getMuccaMVAV.AddSpectator("std_vector_jet_pt[0]",   (self.var17))
       
        # mva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        self.getMuccaMonoH.BookMVA("BDT","/afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_5/src/MUCCA/Optimization/Weights-" + self.model + "_TTbar_5var_" + self.channel + "/TMVAClassification_" + self.training + ".weights.xml")


    def help(self):
        return '''Add mucca mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',     dest='kind',     help='Which background training to be used', default='1')
        group.add_option('-s', '--signal',   dest='signal',   help='Variable name',                        default='2HDMadaptTTbar_em')
        group.add_option('-a', '--training', dest='training', help='Training',                             default='BDT4')
        group.add_option('-c', '--channel',  dest='channel',  help='Channel',                              default='em')
        group.add_option('-m', '--model',    dest='model',    help='Signal Model',                         default='2HDM')
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
            raise RuntimeError('Missing parameter')
        self.kind        = opts.kind
        print((" kind     = ", self.kind))
        self.signal      = opts.signal
        print((" signal   = ", self.signal))
        self.training    = opts.training
        print((" training = ", self.training))
        self.channel     = opts.channel
        print((" channel  = ", self.channel))
        self.model       = opts.model
        print((" model  = ", self.model))


    def process(self,**kwargs):

        self.getMuccaMonoH = None

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

        self.createMuccaMonoH()

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
              self.var2[0] = itree.mtw2
              self.var3[0] = itree.metTtrk
              self.var4[0] = itree.drll
              self.var5[0] = itree.ptll
              
              muccamva[0] = self.getMuccaMonoH.EvaluateMVA("BDT")
              
            otree.Fill()
            
        self.disconnect()
        print('- Eventloop completed')


