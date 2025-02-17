# Cross section DB                                                                                                                                                                                                                            
# Units in pb                                                                                                                                                                                                                                 
#                                                                                                                                                                                                                                             
# References                                                                                                                                                                                                                                  
#                                                                                                                                                                                                                                             
#       A       https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV                                                                                                                                                    
#       B       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO                                                                                                                                                                     
#       C       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV                                                                                                                                                 
#       D       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec                                                                                                                                                              
#       E       https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns                                                                                                                                                                   
#       F       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV                                                                                                                                                   
#       F2      https://github.com/latinos/LatinoAnalysis/blob/master/Tools/python/HiggsXSection.py                                                                                                                                           
#       G       https://twiki.cern.ch/twiki/bin/view/CMS/GenXsecTaskForce                                                                                                                                                                     
#       H       http://arxiv.org/pdf/1307.7403v1.pdf                                                                                                                                                                                          
#       I       https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer                                                                                                                                                             
#       J       https://svnweb.cern.ch/cern/wsvn/LHCDMF/trunk/doc/tex/TTBar_Xsecs_Appendix.tex                                                                                                                                                
#       K       https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProductionMassScan (powheg numbers)                                                                                                                                      
#       L       https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProduction (powheg numbers)                                                                                                                                              
#       M       https://github.com/shu-xiao/MadGraphScanning/blob/master/diffCrossSection/madGraph.txt                                                                                                                                        
#       N       MCM                                                                                                                                                                                                                           
#       O       https://twiki.cern.ch/twiki/pub/LHCPhysics/LHCHXSWG/Higgs_XSBR_YR4_update.xlsx                                                                                                                                                
#       P       https://drive.google.com/file/d/0B7mfFpGbPaMvb0ZtMlJfdXhJb2M/view                                                                                                                                                             
#       Q       #https://indico.cern.ch/event/448517/session/0/contribution/16/attachments/1164999/1679225/Long_Generators_WZxsec_05_10_15.pdf                                                                                                
#       R       https://cms-pdmv.cern.ch/mcm/requests?page=0&prepid=B2G-RunIISummer15GS*&dataset_name=TTbarDMJets_*scalar_Mchi-*_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8                                                            
#       S       https://docs.google.com/spreadsheets/d/1b4qnWfZrimEGYc1z4dHl21-A9qyJgpqNUbhOlvCzjbE/edit?usp=sharing                                                                                                                          
#       T       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR                                                                                                                                                        
#       U       https://twiki.cern.ch/twiki/pub/CMS/MonoHCombination/crossSection_ZpBaryonic_gq0p25.txt                                                                                                                                       
#       V       https://twiki.cern.ch/twiki/bin/viewauth/CMS/SameSignDilepton2016                                                                                                                                                             
#       W       https://cms-gen-dev.cern.ch/xsdb/                                                                                                                                                                                             
#       Y       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV                                                                                                                                                
#   A1 https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf                                                                                                             
#       X       Unknown! - Cross section not yet there                                                                                                                                                                                        



## Early Winter2022 samples - nanoAODv10                                                                                                                                                                                                                                     

samples['WW_TuneCP5_13p6TeV-pythia8']                   .extend( ['xsec=80.42', 'kfact=1.00',           'ref=E'] )
samples['TTTo2L2Nu']                                    .extend( ['xsec=96.9', 'kfact=1.00',           'ref=E'] )
samples['DYJetsToLL_M-10to50']                          .extend( ['xsec=19317.5', 'kfact=1.00',           'ref=E'] )
samples['WZ']                                           .extend( ['xsec=29.12', 'kfact=1.00',           'ref=E'] )
samples['ZZ']                                           .extend( ['xsec=12.85', 'kfact=1.00',           'ref=E'] )





