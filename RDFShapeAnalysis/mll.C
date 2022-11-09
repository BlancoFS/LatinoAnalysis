#include "TLorentzVector.h"

float mll(float Lepton_pt, float Lepton_phi, float Lepton_eta, float Lepton_pt_2, float Lepton_phi_2, float Lepton_eta_2){

  TLorentzVector l1;
  TLorentzVector l2;

  l1.SetPtEtaPhiM(Lepton_pt, Lepton_eta, Lepton_phi, 0.0);
  l2.SetPtEtaPhiM(Lepton_pt_2, Lepton_eta_2, Lepton_phi_2, 0.0);

  double mass = (l1 + l2).M();
  return mass;
}