from pandas import  DataFrame

## first two dataframes are just dummy, you can delete from them to get dataframe for a given region, 
df_out_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET', 
                                    'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                    'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                    'FJetMass',
                                    'Mu1Pt', 'Mu1Eta', 'Mu1Phi', 'Mu2Pt', 'Mu2Eta', 'Mu2Phi', 
                                    'Ele1Pt', 'Ele1Eta', 'Ele1Phi', 'Ele2Pt', 'Ele2Eta', 'Ele2Phi',
                                    'MT',
                                    'weight'])



df_out_resolved = DataFrame(columns=['run', 'lumi', 'event', 'MET', 
                                     'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                     'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi', 'Jet3Pt','Jet3Eta','Jet3Phi', 'Jet1CSV', 'Jet2CSV','Jet3CSV',
                                     'DiJetMass', 'DiJetPt', 'DiJetEta',
                                     'Mu1Pt', 'Mu1Eta', 'Mu1Phi', 'Mu2Pt', 'Mu2Eta', 'Mu2Phi', 
                                     'Ele1Pt', 'Ele1Eta', 'Ele1Phi', 'Ele2Pt', 'Ele2Eta', 'Ele2Phi',
                                     'MT',
                                     'weight'])


## SR dataframes 

df_out_SR_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET', 
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets','max_dphi_jets',
                                       'weight','btagweight','dbweight'])

df_out_SBand_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])

'''
df_out_SR_resolved = DataFrame(columns=['run', 'lumi', 'event', 'MET', 
                                        'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                        'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi', 'Jet3Pt','Jet3Eta','Jet3Phi','Jet1CSV', 'Jet2CSV','Jet3CSV',
                                        'DiJetMass','nJets','FJetN2b1','FJetN2b2','FJetrho',
                                        'weight'])



df_out_SBand_resolved = DataFrame(columns=['run', 'lumi', 'event', 'MET',
                                        'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                        'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi', 'Jet3Pt','Jet3Eta','Jet3Phi','Jet1CSV', 'Jet2CSV','Jet3CSV',
                                        'DiJetMass','nJets','FJetN2b1','FJetN2b2','FJetrho',
                                        'weight'])

'''

df_out_Tope_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
				       'lep1_pT','lep1_eta','lep1_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
				       'weight','btagweight','dbweight'])


df_out_Topmu_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])


df_out_We_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])

df_out_Wmu_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])



df_out_Zee_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi',
                                       'lep2_pT','lep2_eta','lep2_Phi',
				       'Zmass','ZpT','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])


df_out_Zmumu_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi',
                                       'lep2_pT','lep2_eta','lep2_Phi',
                                       'Zmass','ZpT','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])


df_out_TopWmu_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])

df_out_TopWe_boosted = DataFrame(columns=['run', 'lumi', 'event', 'MET','RECOIL',
                                       'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV', 'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                       'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                       'lep1_pT','lep1_eta','lep1_Phi','FJetN2b1','FJetN2b2','FJetrho','min_dphi_jets',
                                       'weight','btagweight','dbweight'])

## define more data frames for each region



df_out_Tope_resolved  = DataFrame(columns=['run', 'lumi', 'event','MET','RECOIL' ,
                                         'Njets_PassID','Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                         'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV','Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                         'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                         'lep1_pT','lep1_eta','lep1_Phi',
                                         'weight','puweight','lepweight','recoilweight','btagweight','ewkweight','toppTweight'])

df_out_Topmu_resolved  = DataFrame(columns=['run', 'lumi', 'event','MET','RECOIL' ,
                                         'Njets_PassID','Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                         'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV','Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                         'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                         'lep1_pT','lep1_eta','lep1_Phi',
                                         'weight','puweight','lepweight','recoilweight','btagweight','ewkweight','toppTweight'])
          

df_out_Wmu_resolved  = DataFrame(columns=['run', 'lumi', 'event','MET','RECOIL' ,
                                         'Njets_PassID','Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                         'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV','Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                         'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                         'lep1_pT','lep1_eta','lep1_Phi',
                                         'weight','puweight','lepweight','recoilweight','btagweight','ewkweight','toppTweight'])
                                
df_out_We_resolved  = DataFrame(columns=['run', 'lumi', 'event','MET','RECOIL' ,
                                         'Njets_PassID','Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                         'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV','Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                         'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                         'lep1_pT','lep1_eta','lep1_Phi',
                                         'weight','puweight','lepweight','recoilweight','btagweight','ewkweight','toppTweight'])


df_out_Zee_resolved    = DataFrame(columns=['run', 'lumi', 'event','MET','RECOIL',
					'Njets_PassID','Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                        'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV','Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                        'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                        'lep1_pT','lep1_eta','lep1_Phi',
                                        'lep2_pT','lep2_eta','lep2_Phi',
                                        'Zmass','ZpT',
                                        'weight','puweight','lepweight','recoilweight','btagweight','ewkweight','toppTweight'])

df_out_Zmumu_resolved    = DataFrame(columns=['run', 'lumi', 'event','MET','RECOIL',
                                        'Njets_PassID','Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                        'FJetPt', 'FJetEta', 'FJetPhi', 'FJetCSV','Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi',
                                        'FJetMass', 'DiJetPt', 'DiJetEta','nJets','min_dPhi','met_Phi','RECOIL_Phi',
                                        'lep1_pT','lep1_eta','lep1_Phi',
                                        'lep2_pT','lep2_eta','lep2_Phi',
                                        'Zmass','ZpT',
                                        'weight','puweight','lepweight','recoilweight','btagweight','ewkweight','toppTweight'])

df_out_SR_resolved = DataFrame(columns=['run', 'lumi', 'event','MET','Njets_PassID',
                                       'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                       'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet1CSV','Jet2Pt', 'Jet2Eta', 'Jet2Phi', 'Jet2CSV',
                                       'Jet3Pt', 'Jet3Eta', 'Jet3Phi', 'Jet3CSV',
                                       'DiJetMass','nJets',
                                       'weight'])

df_out_SBand_resolved = DataFrame(columns=['run', 'lumi', 'event', 'MET',
                                        'Njets_PassID', 'Nbjets_PassID', 'NTauJets', 'NEle', 'NMu', 'nPho',
                                        'Jet1Pt', 'Jet1Eta', 'Jet1Phi', 'Jet2Pt','Jet2Eta', 'Jet2Phi', 'Jet3Pt','Jet3Eta','Jet3Phi','Jet1CSV', 'Jet2CSV','Jet3CSV',
                                        'DiJetMass','nJets',
                                        'weight'])
