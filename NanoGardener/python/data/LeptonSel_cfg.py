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
   

   
   
###____________________Full2022v9__________________________ For nAODv9
'Full2022v9': {


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
                                   'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- cutBasedFall22Iso

          'cutBasedFall22Iso':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         #'tkSF':  {   ### To be computed for Run 3
                         #           '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/egammaEffi.txt_EGM2D_updatedAll.root',
                         #         } ,
                         #'wpSF':  {
                         #           '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2018.txt',
                         #         } ,
                         #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v7/mvaFall17V1Iso_WP90/',
                         #
                              } ,


             },

 # ------------ 
 'WgStarObjWP' : {

          # ----- cutBasedFall22Iso

          'cutBasedFall22Iso':  {
                         'cuts' : {
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                     'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' , 
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None'
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None'
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         #'tkSF':  {
                         #           '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/egammaEffi.txt_EGM2D_updatedAll.root',
                         #         } ,
                         #'wpSF':  {
                         #           '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2018.txt',
                         #         } ,
                         #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v7/mvaFall17V1Iso_WP90/',
                         
                                 } ,

                 } ,

},

}

####################### Muon WP ######################################

MuonWP = {

###____________________Full2022v9__________________________
'Full2022v9': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.4',
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight_HWWW' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         #'idSF':  {
                         #           '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ID_TH2_SFs_pt_eta.root'],
                         #         } ,
                         #'isoSF': {
                         #           '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ISO_TH2_SFs_pt_eta.root'],
                         #         } ,
                         #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v7/cut_Tight_HWWW/',

                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {

      'cut_Tight_HWWW' : {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         #'idSF':  {
                         #           '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ID_TH2_SFs_pt_eta.root'],
                         #         } ,
                         #'isoSF': {
                         #           '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ISO_TH2_SFs_pt_eta.root'],
                         #         } ,
                         #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v7/cut_Tight_HWWW/',
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                       } ,
 
                 }, 
},


}


if __name__ == '__main__':
    print('_______________LepFilter_dict___________')
    print(LepFilter_dict)
    print('') 
    print('_______________ElectronWP_______________')
    print('')
    for key in ElectronWP:
        print(('__________' + key + '__________'))
        print('')
        for typ in ElectronWP[key]:
            print(('_____' + typ + '_____'))
            for entr in ElectronWP[key][typ]:
                print((entr + ' ='))
                print((ElectronWP[key][typ][entr]['cuts']))
                print('')
                for info in ElectronWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print((ElectronWP[key][typ][entr][info]))
                        print('')
    print('_______________MuonWP___________________')
    print('')
    for key in MuonWP:
        print(('__________' + key + '__________'))
        print('')
        for typ in MuonWP[key]:
            print(('_____' + typ + '_____'))
            for entr in MuonWP[key][typ]:
                print((entr + ' ='))
                print((MuonWP[key][typ][entr]['cuts']))
                print('')
                for info in MuonWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print((MuonWP[key][typ][entr][info]))
                        print('')

