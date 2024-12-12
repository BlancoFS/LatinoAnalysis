import copy

LepFilter_dict = {
   'Loose': 'isLoose',
   'Veto': 'isVeto',
   'WgStar': 'isWgs',
   'isLoose': 'FakeObjWP',
   'isVeto': 'VetoObjWP',
   'isWgs': 'WgStarObjWP'
}



####################### Electron WP ##################################

ElectronWP = {  



###___________________Full2018v9_______________________
'Full2018v9': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                ] ,             
                                   },
                       } ,
                 } ,
  
 # ------------ 
 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                      'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                      'electron_col[LF_idx]["pt"] > 7.0' ,
                                      'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                                      'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                                      'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                                  ] ,             
                         },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {
    'looseElectron_tthMVA':  {
        'cuts' : { 
            # Common cuts 
            'True' :
            [
                'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                'electron_col[LF_idx]["pt"] > 7.0' ,
                'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
            ] ,
            # Barrel
            'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.72) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.56) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.36)',
            ] ,
            # Overlap
            'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.72) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.56) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.28)',
            ],
            # EndCap
            'abs(electron_col[LF_idx]["eta"]) > 1.479' :                            
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.68) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.48) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > 0.08)',
            ] ,
        } ,
        'tkSF':  { 
            '1-1' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz'
        } ,
        'wpSF':  {
            '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/egammaEffi.txt',
        } ,
        'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/looseElectron_tthMVA/',              
    } ,
    'looseElectron_tthMVA_highEff':  {
        'cuts' : {
            # Common cuts            
            'True' :
            [
                'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                'electron_col[LF_idx]["pt"] > 7.0' ,
                'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
            ] ,
            # Barrel            
            'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.91) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.9) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.73)',
            ] ,
            # Overlap            
            'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.92) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.92) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.85)',
            ],
            # EndCap            
            'abs(electron_col[LF_idx]["eta"]) > 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.92) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.89)',
            ] ,
        } ,
        'tkSF':  {
            '1-1' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz'
        } ,
        'wpSF':  {
            '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/egammaEffi_tthMVA_highEff.txt',
        } ,
        'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/looseElectron_tthMVA_highEff/',
    },
},
'WgStarObjWP' : {

        },
},



###____________________Full2017v9__________________________
'Full2017v9': {
    ## ------------      
    'VetoObjWP' : { 
        'HLTsafe' : { 
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'False'
                ] ,             
            },
        } ,
    } ,    
    # ------------ 
    'FakeObjWP'  : {        
        'HLTsafe' : {
            'cuts' : {
                # Common cuts                                                                                                                                                              
                'True' :
                [
                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                    'electron_col[LF_idx]["pt"] > 7.0' ,
                    'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                    'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                ] ,
            },
        } ,        
    } ,
    # ------------ 
    'TightObjWP' : {        
        'looseElectron_tthMVA':  {
            'cuts' : {
                # Common cuts                
                'True' :
                [
                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                    'electron_col[LF_idx]["pt"] > 7.0' ,
                    'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                    'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                ] ,
                # Barrel                
                'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.72) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.60) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.36)',
                ] ,
                # Overlap
                'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.72) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.56) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.28)',
                ],
                # EndCap                
                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.68) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.48) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > 0.08)',
                ] ,
            } ,
            'tkSF':  {
                '1-5' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz'
            } ,
            'wpSF':  {
                '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/egammaEffi.txt',
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v9/looseElectron_tthMVA/',
        } ,        
        'looseElectron_tthMVA_highEff':  {
            'cuts' : {
            # Common cuts

            'True' :
            [
                'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                'electron_col[LF_idx]["pt"] > 7.0' ,
                'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
            ] ,
            # Barrel
            'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.91) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.9) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.73)',
            ] ,
            # Overlap
            'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.92) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.85)',
            ],
            # EndCap
            'abs(electron_col[LF_idx]["eta"]) > 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.89)',
            ] ,
                } ,
        'tkSF':  {
            '1-5' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz'
        } ,
        'wpSF':  {
            '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/egammaEffi_tthMVA_highEff.txt',
        } ,
        'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v9/looseElectron_tthMVA_highEff/',
        },
    },
    # ------------ 
    'WgStarObjWP' : {
        
    } ,        
},

###____________________Full2016v9________ : for nAODv9 - HIPM part
'Full2016v9HIPM': {
    'VetoObjWP' : {
        'HLTsafe' : {
            'cuts' : {
                # Common cuts
                'True' :
                [
                    'False'
                ] ,
            },
        } ,
    } ,    
    'FakeObjWP'  : {
        'HLTsafe' : { 
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                    'electron_col[LF_idx]["pt"] > 7.0' ,
                    'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                    'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                ] ,             
            },
        } ,
    } ,
    # ------------ 
    'TightObjWP' : {
        'looseElectron_tthMVA':  {
            'cuts' : {
                # Common cuts                                                                                                                                                                              
                'True' :
                [
                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                    'electron_col[LF_idx]["pt"] > 7.0' ,
                    'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                    'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                ] ,
                # Barrel                                                                                                                                                                                   
                'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.81) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.61) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.24)',
                ] ,
                # Overlap                                                                                                                                                                                  
                'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.81) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.57) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.13)',
                ],
                # EndCap                                                                                                                                                                                   
                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.78) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.49) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > 0.14)',
                ] ,
            } ,
            'tkSF':  {
                '1-3' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz'
            } ,
            'wpSF':  {
                '1-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/egammaEffi.txt',
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9HIPM/looseElectron_tthMVA/',
        } ,
        'looseElectron_tthMVA_highEff':  {
            'cuts' : {
            # Common cuts                                                                                                                                                                                  
            'True' :
            [
                'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                'electron_col[LF_idx]["pt"] > 7.0' ,
                'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
            ] ,
            # Barrel                                                                                                                                                                                       
            'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.91) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.69)',
            ] ,
            # Overlap                                                                                                                                                                                      
            'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.81)',
            ],
            # EndCap                                                                                                                                                                                       
            'abs(electron_col[LF_idx]["eta"]) > 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.95) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.86)',
            ] ,
                } ,
        'tkSF':  {
            '1-3' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz'
        } ,
        'wpSF':  {
            '1-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/egammaEffi_tthMVA_highEff.txt',
        } ,
        'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9HIPM/looseElectron_tthMVA_highEff/',
        },
    }, 
 'WgStarObjWP' : {
 } ,
    
},

###____________________Full2016v9________ : for nAODv9 - no HIPM part
'Full2016v9noHIPM': {
    ## ------------
    'VetoObjWP' : {
        'HLTsafe' : {
            'cuts' : {
                # Common cuts
                'True' :
                [
                    'False'
                ] ,
            },
        } ,
    } ,
    'FakeObjWP'  : {
        'HLTsafe' : { 
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                    'electron_col[LF_idx]["pt"] > 7.0' ,
                    'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                    'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                ] ,             
            },
        } ,
    } ,
    # ------------ 
    'TightObjWP' : {
        'looseElectron_tthMVA':  {
            'cuts' : {
                # Common cuts                                                                                                                                                                              
                'True' :
                [
                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                    'electron_col[LF_idx]["pt"] > 7.0' ,
                    'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                    'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
                ] ,
                # Barrel                                                                                                                                                                                   
                'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.83) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.65) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.32)',
                ] ,
                # Overlap                                                                                                                                                                                  
                'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.82) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.61) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.17)',
                ],
                # EndCap                                                                                                                                                                                   
                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                [
                    '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.77) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.51) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > 0.08)',
                ] ,
            } ,
            'tkSF':  {
                '4-7' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz'
            } ,
            'wpSF':  {
                '4-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/egammaEffi.txt',
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9noHIPM/looseElectron_tthMVA/',
        } ,
        'looseElectron_tthMVA_highEff':  {
            'cuts' : {
            # Common cuts                                                                                                                                                                                  
            'True' :
            [
                'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                'electron_col[LF_idx]["pt"] > 7.0' ,
                'abs(electron_col[LF_idx]["dxy"]) < 0.5' ,
                'abs(electron_col[LF_idx]["dz"]) < 1'  ,
                'abs(electron_col[LF_idx]["sip3d"]) < 4.0',
            ] ,
            # Barrel                                                                                                                                                                                       
            'abs(electron_col[LF_idx]["eta"]) <= 0.8' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.92) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.91) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.67)',
            ] ,
            # Overlap                                                                                                                                                                                      
            'abs(electron_col[LF_idx]["eta"]) > 0.8 and abs(electron_col[LF_idx]["eta"]) <= 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.81)',
            ],
            # EndCap                                                                                                                                                                                       
            'abs(electron_col[LF_idx]["eta"]) > 1.479' :
            [
                '(electron_col[LF_idx]["pt"]<=10.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.95) or (electron_col[LF_idx]["pt"] > 10.0 and electron_col[LF_idx]["pt"] <= 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.93) or (electron_col[LF_idx]["pt"] > 20.0 and electron_col[LF_idx]["mvaTTH_UL"] > -0.87)',
            ] ,
            } ,
            'tkSF':  {
                '4-7' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz'
            } ,
            'wpSF':  {
                '4-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/egammaEffi_tthMVA_highEff.txt',
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9noHIPM/looseElectron_tthMVA_highEff/',
        },
    }, 
    # ------------ 
    'WgStarObjWP' : {
    } ,
},
}

####################### Muon WP ######################################

MuonWP = {


###____________________Full2018v9__________________________
'Full2018v9': {
    
    ## ------------  
    'VetoObjWP' : { 
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                ]
            } ,
        }
    } ,    
    # ------------ 
    'FakeObjWP'  : {        
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
        } ,        
    } ,
    # ------------ 
    'TightObjWP' :  {        
        'Loose_HZZ' : {
            'cuts' : { 
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                    'muon_col[LF_idx]["pfRelIso03_all"] < 0.35',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',  
            } ,
            'idSF':  {
                '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/Loose_HZZ/',
        } ,
        'Loose_HZZ_tthMVA' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 10.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.94 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 10.0 and muon_col[LF_idx]["pt"] <= 20.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.87 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 20.0 and muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.22 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.22 ' ,
                ] ,
            } ,
            'tkSF':  {
                '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_LooseID_IP_tthMVA_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/Loose_HZZ_tthMVA/',
        } ,
        'Loose_HZZ_noIso' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-1' : ['LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/Loose_HZZ/',
        } ,
    },
    # -------------
    'WgStarObjWP' : {
        
    },
},                 

    
###____________________Full2017v9__________________________
'Full2017v9': {        
    ## ------------  
    'VetoObjWP' : { 
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                ]
            } ,
        }
    } , 
    'FakeObjWP'  : {
        'HLTsafe' : {
            'cuts' : {
                # Common cuts
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
        } ,
    } ,        
    # ------------ 
    'TightObjWP' :  {
        'Loose_HZZ' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                    'muon_col[LF_idx]["pfRelIso03_all"] < 0.35',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                                'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v9/Loose_HZZ/',
        } ,
        'Loose_HZZ_tthMVA' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 10.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.95 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 10.0 and muon_col[LF_idx]["pt"] <= 20.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.89 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 20.0 and muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.13 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.13 ' ,
                ] ,
            } ,
            'tkSF':  {
                '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_LooseID_IP_tthMVA_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v9/Loose_HZZ_tthMVA/',
        } ,
        'Loose_HZZ_noIso' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-5' : ['LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v9/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v9/Loose_HZZ/',
        } ,
    } ,
    # -------------
    'WgStarObjWP' : {        
    } ,    
},

###____________________Full2016v9HIPM__________________________

'Full2016v9HIPM': {
    'VetoObjWP' : { 
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                ]
            } ,
        }
    } ,
    # ------------ 
    'FakeObjWP'  : {
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
        } ,
        
    } ,
    # ------------ 
    'TightObjWP' :  {
        'Loose_HZZ' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                    'muon_col[LF_idx]["pfRelIso03_all"] < 0.35',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                                'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '1-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-3' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-3' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9HIPM/Loose_HZZ/',
        } ,
        'Loose_HZZ_tthMVA' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 10.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.94 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 10.0 and muon_col[LF_idx]["pt"] <= 20.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.89 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 20.0 and muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.17 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.17 ' ,
                ] ,
            } ,
            'tkSF':  {
                '1-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-3' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-3' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_LooseID_IP_TTHMVA_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9HIPM/Loose_HZZ_tthMVA/',
        } ,
        'Loose_HZZ_noIso' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '1-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '1-3' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '1-3' : ['LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9HIPM/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9HIPM/Loose_HZZ/',
        } ,
    } ,
    # -------------
    'WgStarObjWP' : {
    }, 
},
###____________________Full2016v9noHIPM__________________________

'Full2016v9noHIPM': {
    ## ------------  
    'VetoObjWP' : { 
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                ]
            } ,
        }
    } ,
    # ------------ 
    'FakeObjWP'  : {        
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
        } ,
    } ,    
    # ------------ 
    'TightObjWP' :  {
        'Loose_HZZ' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                    'muon_col[LF_idx]["pfRelIso03_all"] < 0.35',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                                'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '4-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '4-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '4-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9noHIPM/Loose_HZZ/',
        } ,
        'Loose_HZZ_tthMVA' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 10.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.95 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 10.0 and muon_col[LF_idx]["pt"] <= 20.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > -0.89 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 20.0 and muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.2 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                    'muon_col[LF_idx]["mvaTTH_UL"] > 0.2 ' ,
                ] ,
            } ,
            'tkSF':  {
                '4-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '4-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '4-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_LooseID_IP_TTHMVA_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9noHIPM/Loose_HZZ_tthMVA/',
        } ,
        'Loose_HZZ_noIso' : {
            'cuts' : {
                'True' :
                [
                    'muon_col[LF_idx]["pt"] > 5.0' ,
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    '(muon_col[LF_idx]["isGlobal"] == 1 or muon_col[LF_idx]["isTracker"] == 1)' ,
                    'abs(muon_col[LF_idx]["dxy"]) < 0.5' ,
                    'abs(muon_col[LF_idx]["dz"]) < 1' ,
                    'abs(muon_col[LF_idx]["sip3d"]) < 4',
                ] ,
                'muon_col[LF_idx]["pt"] <= 200.0' :
                [
                    'muon_col[LF_idx]["looseId"] == 1 ' ,
                ] ,
                'muon_col[LF_idx]["pt"] > 200.0' :
                [
                    '(muon_col[LF_idx]["looseId"] == 1 or muon_col[LF_idx]["highPtId"] == 1)' ,
                ] ,
            } ,
            'tkSF':  {
                '4-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_TrackerMuons_DEN_genTracks_abseta_pt.root',
            } ,
            'idSF':  {
                '4-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_LooseID_DEN_TrackerMuons_abseta_pt.root'],
            } ,
            'isoSF': {
                '4-7' : ['LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v9noHIPM/NUM_LooseID_IP_ISO_DEN_LooseID_abseta_pt.root'],
            } ,
            'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v9noHIPM/Loose_HZZ/',
        } ,
    } ,
    # -------------
    'WgStarObjWP' : { 
    }, 
},

}

for i in ["Full2016v5", "Full2016v6", "Full2016v7", "Full2017v5", "Full2017v6", "Full2017v7","Full2018v5", "Full2018v6", "Full2018v7"]:

    ElectronWP[i] = copy.deepcopy(ElectronWP['Full2018v9'])
    MuonWP[i] = copy.deepcopy(MuonWP['Full2018v9']) 

#MuonWP['Full2016v9HIPM'] = copy.deepcopy(MuonWP['Full2016v7'])
#MuonWP['Full2016v9noHIPM'] = copy.deepcopy(MuonWP['Full2016v7'])
#MuonWP['Full2018v9'] = copy.deepcopy(MuonWP['Full2018v7'])
#MuonWP['Full2017v9'] = copy.deepcopy(MuonWP['Full2017v7'])
 
if __name__ == '__main__':
    print('_______________LepFilter_dict___________')
    print(LepFilter_dict)
    print('') 
    print('_______________ElectronWP_______________')
    print('')
    for key in ElectronWP:
        print('__________' + key + '__________')
        print('')
        for typ in ElectronWP[key]:
            print('_____' + typ + '_____')
            for entr in ElectronWP[key][typ]:
                print(entr + ' =')
                print(ElectronWP[key][typ][entr]['cuts'])
                print('')
                for info in ElectronWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print(ElectronWP[key][typ][entr][info])
                        print('')
    print('_______________MuonWP___________________')
    print('')
    for key in MuonWP:
        print('__________' + key + '__________')
        print('')
        for typ in MuonWP[key]:
            print('_____' + typ + '_____')
            for entr in MuonWP[key][typ]:
                print(entr + ' =')
                print(MuonWP[key][typ][entr]['cuts'])
                print('')
                for info in MuonWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print(MuonWP[key][typ][entr][info])
                        print('')

