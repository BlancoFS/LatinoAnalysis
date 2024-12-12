# Cross section DB for Ultra-Legacy samples
# Units in pb
#
# Detailed references at: https://docs.google.com/spreadsheets/d/1IEfle0H1V3ih2JVFpYckmTd-ACTBqgBRIsFydegGgPQ/edit?usp=sharing
#
# References
#
#	A	https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV		
#	B	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO		
#	C	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV		
#	D	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec		
#	E	https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
#       F       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV
#	F2	https://github.com/latinos/LatinoAnalysis/blob/master/Tools/python/HiggsXSection.py
#	G	https://twiki.cern.ch/twiki/bin/view/CMS/GenXsecTaskForce		
#	H	http://arxiv.org/pdf/1307.7403v1.pdf		
#	I	https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer		
#	J	https://svnweb.cern.ch/cern/wsvn/LHCDMF/trunk/doc/tex/TTBar_Xsecs_Appendix.tex
#	K	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProductionMassScan (powheg numbers)
#	L	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProduction (powheg numbers)
#       M       https://github.com/shu-xiao/MadGraphScanning/blob/master/diffCrossSection/madGraph.txt
#       N       MCM
#       O       https://twiki.cern.ch/twiki/pub/LHCPhysics/LHCHXSWG/Higgs_XSBR_YR4_update.xlsx
#       P       https://drive.google.com/file/d/0B7mfFpGbPaMvb0ZtMlJfdXhJb2M/view
#       Q       #https://indico.cern.ch/event/448517/session/0/contribution/16/attachments/1164999/1679225/Long_Generators_WZxsec_05_10_15.pdf
#	R	https://cms-pdmv.cern.ch/mcm/requests?page=0&prepid=B2G-RunIISummer15GS*&dataset_name=TTbarDMJets_*scalar_Mchi-*_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#       S       https://docs.google.com/spreadsheets/d/1b4qnWfZrimEGYc1z4dHl21-A9qyJgpqNUbhOlvCzjbE/edit?usp=sharing
#       T       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
#       U       https://twiki.cern.ch/twiki/pub/CMS/MonoHCombination/crossSection_ZpBaryonic_gq0p25.txt
#	V	https://twiki.cern.ch/twiki/bin/viewauth/CMS/SameSignDilepton2016
#       W       https://cms-gen-dev.cern.ch/xsdb/
#       Z       http://cms.cern.ch/iCMS/analysisadmin/cadilines?line=SMP-18-006
#       Y       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV
#       A1      https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf 
#	X	Unknown! - Cross section not yet there

samples['WJetsToLNu']                   .extend( ['xsec=61526.7','kfact=1.00','ref=E'] )
samples['WJetsToLNu-LO']                .extend( ['xsec=61526.7','kfact=1.00','ref=E'] )
### DY
samples['DYJetsToLL_M-10to50']          	.extend( ['xsec=18610.0',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50-LO']               .extend( ['xsec=18610.0',       'kfact=1.000',          'ref=E'] )

samples['DYJetsToLL_M-50']                      .extend( ['xsec=6077.22',       'kfact=1.000',          'ref=E'] )
samples['DYJetsToLL_M-50-LO']      	        .extend( ['xsec=6077.22',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-50-LO_ext1']     	        .extend( ['xsec=6077.22',	'kfact=1.000',		'ref=E'] )
samples['DYJetsToLL_M-10to50_NLO']          	.extend( ['xsec=20490.0',	'kfact=1.000',		'ref=W'] )

# 1.4*0.0368 --> 1.4 is a k-factor, 0.0368 comes from XSDB, divided by 1000
samples['GluGluToZZTo4M']      	        .extend( ['xsec=0.00159',	'kfact=1.000',		'ref=W'] )
samples['GluGluToZZTo4E']              	.extend( ['xsec=0.00159',	'kfact=1.000',		'ref=W'] )
samples['GluGluToZZTo4T']              	.extend( ['xsec=0.00159',	'kfact=1.000',		'ref=W'] )
samples['GluGluToZZTo2M2E']              	.extend( ['xsec=0.00319',	'kfact=1.000',		'ref=W'] )
samples['GluGluToZZTo2E2T']              	.extend( ['xsec=0.00319',	'kfact=1.000',		'ref=W'] )
samples['GluGluToZZTo2M2T']              	.extend( ['xsec=0.00319',	'kfact=1.000',		'ref=W'] )

### WZ

samples['WZTo3LNu']		                .extend( ['xsec=4.666',  	'kfact=1.000',		'ref=X'] ) # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf
samples['WZewk_3LNu']                           .extend( ['xsec=0.08124',       'kfact=1.000',          'ref=E'] )
samples['WZG']                                  .extend( ['xsec=0.04345',       'kfact=1.000',          'ref=E'] )
### ZZ
samples['ZZ']                                   .extend( ['xsec=12.14', 	'kfact=1.000',		'ref=E'] )
samples['ZZTo4L']                               .extend( ['xsec=1.325', 	'kfact=1.000',		'ref=E'] )
samples['ZZewk']                               .extend( ['xsec=0.0009922',         'kfact=1.000',          'ref=E'] )
### ZG
samples['ZGToLLG']                              .extend( ['xsec=51.1',          'kfact=1.000',          'ref=W'] )


### Top
samples['TTJets-LO']                            .extend( ['xsec=815.96',	'kfact=1.000',		'ref=E'] )
samples['TTTo2L2Nu'] 	             	        .extend( ['xsec=87.310',	'kfact=1.000',		'ref=E'] )

samples['TTZ']                          .extend( ['xsec=0.259',        'kfact=1.000',          'ref=W'] )      
samples['TTZZ']                              .extend( ['xsec=0.001572',        'kfact=1.000',          'ref=E'] )
samples['TTWW']                       .extend( ['xsec=0.007883',        'kfact=1.000',          'ref=W'] )

## VVV
samples['WWW']			        	.extend( ['xsec=0.2158',	'kfact=1.000',		'ref=W'] )
samples['WWW_ext1']			        .extend( ['xsec=0.2158',	'kfact=1.000',		'ref=W'] )
                                               
samples['WWZ']				        .extend( ['xsec=0.1707',	'kfact=1.000',		'ref=W'] )
samples['WWZ_ext1']     			.extend( ['xsec=0.1707',	'kfact=1.000',		'ref=W'] )
                                               
samples['WZZ']	 			        .extend( ['xsec=0.05709',	'kfact=1.000',		'ref=W'] )
samples['WZZ_ext1']			        .extend( ['xsec=0.05709',	'kfact=1.000',		'ref=W'] )
                                               
samples['ZZZ']				        .extend( ['xsec=0.01476',	'kfact=1.000',		'ref=W'] )
samples['ZZZ_ext1']			        .extend( ['xsec=0.01476',	'kfact=1.000',		'ref=W'] )
                                               
samples['WWG']                                  .extend( ['xsec=0.2147',        'kfact=1.000',          'ref=E'] )

### Signals - XS are dummy and taken from YR4 N3LO

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
# BR (H-->WW) = 0.2152
# BR (H-->tt) = 0.06256
# BR (H-->ZZ) = 0.02641

# ggH - XS = 48.52 pb
# 
samples['GluGluHToZZTo4L_M125']    		.extend( ['xsec=0.01218',	'kfact=1.000',	'ref=F'] )
samples['GGHjjToZZTo4L_minloHJJ_M125']       .extend( ['xsec=1',             'kfact=1.000',  'ref=X'] ) 

#
samples['VBFHToZZTo4L_M125']    		.extend( ['xsec=0.001044',	'kfact=1.000',	'ref=F'] )

# 
samples['HWminus_HToZZTo4L_M125']    		.extend( ['xsec=0.000147',	'kfact=1.000',	'ref=F'] )
samples['HWplus_HToZZTo4L_M125']       .extend( ['xsec=0.000232',       'kfact=1.000',  'ref=F'] )
samples['HZ_HToZZ_M125']     .extend( ['xsec=0.000668',       'kfact=1.000',  'ref=F'] )

# 
samples['ttH_HToZZ_M125']    		.extend( ['xsec=0.000393',	'kfact=1.000',	'ref=F'] )
samples['bbH_HToZZ_M125']       .extend( ['xsec=0.000135',       'kfact=1.000',  'ref=F'] ) 
samples['tqH_HToZZ_M125']     .extend( ['xsec=0.0000213',       'kfact=1.000',  'ref=F'] )

samples['DYJetsToLL_M-50_HT-70to100']           .extend( ['xsec=146.5',   'kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-100to200']          .extend( ['xsec=160.7',        'kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-200to400']          .extend( ['xsec=48.63',        'kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-400to600']          .extend( ['xsec=6.993',        'kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-600to800']          .extend( ['xsec=1.761',        'kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-800to1200']         .extend( ['xsec=0.8021','kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-1200to2500']        .extend( ['xsec=0.1937','kfact=1.23',        'ref=W'] ) 
samples['DYJetsToLL_M-50_HT-2500toInf']         .extend( ['xsec=0.003514','kfact=1.23',        'ref=W'] ) 
