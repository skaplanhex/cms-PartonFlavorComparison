// -*- C++ -*-
//
// Package:    PartonFlavorComparison
// Class:      PartonFlavorComparison
// 
/**\class PartonFlavorComparison PartonFlavorComparison.cc Analyzers/PartonFlavorComparison/src/PartonFlavorComparison.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  steven kaplan
//         Created:  Wed Feb 19 09:10:28 CST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetfwd.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/getRef.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/JetReco/interface/JetFloatAssociation.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "SimDataFormats/JetMatching/interface/JetFlavour.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourMatching.h"
#include "SimDataFormats/JetMatching/interface/MatchedPartons.h"
#include "SimDataFormats/JetMatching/interface/JetMatchedPartons.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourInfo.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourInfoMatching.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "fastjet/JetDefinition.hh"
#include "fastjet/ClusterSequence.hh"
#include "fastjet/Selector.hh"
#include "fastjet/PseudoJet.hh"

//GenParticleCollection
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"

#include "TH2D.h"
#include "TH3D.h"
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace edm;
using namespace std;
//
// class declaration
//

class PartonFlavorComparison : public edm::EDAnalyzer {
   public:
      explicit PartonFlavorComparison(const edm::ParameterSet&);
      ~PartonFlavorComparison();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual const char* partonFlavourToChar(int);
      virtual const char* hadronFlavourToChar(int);

      // ----------member data ---------------------------
      edm::Service<TFileService> fs;
      edm::InputTag bHadrons_,cHadrons_,partons_,leptons_,jets_,flavorByClustering_;
      edm::Handle< reco::GenParticleRefVector > bHadrons,cHadrons,partons,leptons;
      edm::Handle< edm::View< reco::Jet > > jets;
      edm::Handle< reco::JetFlavourInfoMatchingCollection > flavorByClustering;

      //plots
      TH1D* hPartonFlavorOld;
      TH1D* hPartonFlavorNew;

      TH2D* hPartonFlavorOld_Phi;
      TH2D* hPartonFlavorNew_Phi;
      TH2D* hPartonFlavorOld_Eta;
      TH2D* hPartonFlavorNew_Eta;
      TH2D* hPartonFlavorOld_Pt;
      TH2D* hPartonFlavorNew_Pt;

      TH1D* hJetPt;
      TH1D* hJetEta;
      TH1D* hJetPhi;

      TH1D* hHardestBJetPt;
      TH1D* hHardestBJetEta;
      TH1D* hHardestBJetPhi;
      TH1D* hSecondHardestBJetPt;
      TH1D* hSecondHardestBJetEta;
      TH1D* hSecondHardestBJetPhi;

      TH1D* hSoftJetsEta;
      TH1D* hSoftJetsPhi;

      TH2D* hJetPt_BHadronPt_HighPt;
      TH2D* hJetPt_BHadronPt_LowPt;

      TH1D* hNumBHadrons;
      TH1D* hNumCHadrons;
      TH1D* hNumPartons;
      TH1D* hNumLeptons;

      TH2D* hJetPt_LightQuarkPt;
      TH2D* hJetPt_GluonPt;

      TH2D* hPartonFlavor_HadronFlavor;

      bool useLeptons;

      ofstream events;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PartonFlavorComparison::PartonFlavorComparison(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
  bHadrons_ = iConfig.getParameter<InputTag>("bHadrons");
  cHadrons_ = iConfig.getParameter<InputTag>("cHadrons");
  partons_ = iConfig.getParameter<InputTag>("partons");
  useLeptons = iConfig.exists("leptons");
  if (useLeptons) leptons_ = iConfig.getParameter<InputTag>("leptons");
  jets_ = iConfig.getParameter<InputTag>("jets");
  flavorByClustering_ = iConfig.getParameter<InputTag>("jetFlavourInfos");

  //events.open("events.txt");

}


PartonFlavorComparison::~PartonFlavorComparison()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
  //events.close();

}


//
// member functions
//
const char*
PartonFlavorComparison::partonFlavourToChar(int temp)
{
    int flav = abs(temp);
    if (flav == 1){
        return "d";
    }
    else if (flav == 2){
        return "u";
    }
    else if (flav == 3){
        return "s";
    }
    else if(flav == 4){
        return "c";
    }
    else if (flav == 5){
        return "b";
    }
    else if (flav == 21){
        return "g";
    }
    else if (flav == 0){
        return "no match";
    }
    else{
        throw cms::Exception("PDGID Issue") << "PDGID Not recognized, investigate!";
    }
}
const char*
PartonFlavorComparison::hadronFlavourToChar(int temp)
{
  int flav = abs(temp);
  if      (flav == 4) return "c";
  else if (flav == 5) return "b";
  else if (flav == 0) return "light";
  else throw cms::Exception("PDGID Issue") << "PDGID Not recognized, investigate!";
}
// ------------ method called for each event  ------------
void
PartonFlavorComparison::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    unsigned int lumi = iEvent.luminosityBlock();
    unsigned int run = iEvent.run();
    unsigned int event = iEvent.id().event();
    
    stringstream ss;
    ss << run << ":" << lumi << ":" << event;
    string eventAddress = ss.str();

    iEvent.getByLabel(bHadrons_,bHadrons);
    iEvent.getByLabel(cHadrons_,cHadrons);
    iEvent.getByLabel(partons_,partons);
    if(useLeptons) iEvent.getByLabel(leptons_,leptons);
    iEvent.getByLabel(jets_, jets);
    iEvent.getByLabel(flavorByClustering_, flavorByClustering );

    //fill histograms with the number of ghost b hadrons, c hadrons, partons, and leptons in each event
    hNumBHadrons->Fill( bHadrons->size() );
    hNumCHadrons->Fill( cHadrons->size() );
    hNumPartons->Fill( partons->size() );
    if(useLeptons) hNumLeptons->Fill( leptons->size() );

    // //find the two hardest b hadrons
    // reco::GenParticleRef hardestBHadron;
    // reco::GenParticleRef secondHardestBHadron;
    // double hardestBPt = -1.;
    // double secondHardestBPt = -1.;
    // for (reco::GenParticleRefVector::const_iterator iHadron = bHadrons->begin(); iHadron != bHadrons->end(); ++iHadron){
    //   double pt = (*iHadron)->pt();
    //   if ( pt > hardestBPt ){
    //     hardestBHadron = (*iHadron);
    //     hardestBPt = pt;
    //   }
    //   else if ( (pt < hardestBPt) && (pt > secondHardestBPt) ){
    //     secondHardestBHadron = (*iHadron);
    //     secondHardestBPt = pt;
    //   }

    // }//end loop over genparticles

    // //find two hardest b jets
    // reco::Jet* hardestBJet = NULL;
    // reco::Jet* secondHardestBJet = NULL;
    // reco::GenParticleRefVector hardestBJetBHadrons;
    // reco::GenParticleRefVector secondHardestBJetBHadrons;
    // double hardestBJetPt = -1.;
    // double secondHardestBJetPt = -1.;
    // for (reco::JetFlavourInfoMatchingCollection::const_iterator iMatch = flavorByClustering->begin(); iMatch != flavorByClustering->end(); ++iMatch) {
    //   const reco::Jet* iJet  = (*iMatch).first.get();
    //   int partonFlavor = abs((*iMatch).second.getPartonFlavour());
    //   if (partonFlavor == 1 || partonFlavor == 2 || partonFlavor == 3)
    //     hJetPt_LightQuarkPt->Fill( (*iMatch).second.getPartons().at(0)->pt(), iJet->pt() );
    //   else if (partonFlavor == 21)
    //     hJetPt_GluonPt->Fill( (*iMatch).second.getPartons().at(0)->pt(), iJet->pt() );
    //   if (partonFlavor != 5) continue;
    //   double jetPt = iJet->pt();
    //   if ( jetPt > hardestBJetPt ){
    //     hardestBJet = const_cast<reco::Jet*>(iJet);
    //     hardestBJetBHadrons = (*iMatch).second.getbHadrons();
    //     hardestBJetPt = jetPt;
    //   }
    //   else if ( (jetPt < hardestBJetPt) && (jetPt > secondHardestBJetPt) ){
    //     secondHardestBJet = const_cast<reco::Jet*>(iJet);
    //     secondHardestBJetBHadrons = (*iMatch).second.getbHadrons();
    //     secondHardestBJetPt = jetPt;
    //   }
    
    // }//end loop over jet matches to get two hardest b jets and to fill histograms for jet pt/parton pt comparison
    // //plots including just two hardest b jets
    // if (!hardestBJet){
    //   //cout << "no b jets!" << endl;
    //   return; //just move on to the next event
    // }
    // if (!secondHardestBJet){
    //   // events << eventAddress << "\n";
    //   // cout << "only one b jet!" << endl;
    //   // cout << eventAddress << endl;
    // }
    // hHardestBJetPhi->Fill( hardestBJet->phi() );
    // hHardestBJetEta->Fill( hardestBJet->eta() );
    // hHardestBJetPt->Fill( hardestBJetPt );
    // if(secondHardestBJet){
    //   hSecondHardestBJetPhi->Fill( secondHardestBJet->phi() );
    //   hSecondHardestBJetEta->Fill( secondHardestBJet->eta() );
    //   hSecondHardestBJetPt->Fill( secondHardestBJetPt );
    // }
    // //compare jet pT to bhadron pT
    // //if(hardestBJetBHadrons.size() == 0 || secondHardestBJetBHadrons.size() == 0) throw cms::Exception("b jet issue") << "one of the two b jets don't have clustered b hadrons!!!";
    // hJetPt_BHadronPt_HighPt->Fill(hardestBJetBHadrons.at(0)->pt(),hardestBJetPt);
    // if(secondHardestBJet)
    //   hJetPt_BHadronPt_HighPt->Fill(secondHardestBJetBHadrons.at(0)->pt(),secondHardestBJetPt);

    for (reco::JetFlavourInfoMatchingCollection::const_iterator iMatch = flavorByClustering->begin(); iMatch != flavorByClustering->end(); ++iMatch) {

      const reco::Jet* iJet  = (*iMatch).first.get();
      int partonFlavor = abs((*iMatch).second.getPartonFlavour());
      int hadronFlavor = abs((*iMatch).second.getHadronFlavour());
      // if (partonFlavor != 5) continue;

      double jetPt = iJet->pt();
      double jetEta = iJet->eta();
      double jetPhi = iJet->phi();

      hJetPhi->Fill(jetPhi);
      hJetEta->Fill(jetEta);
      hJetPt->Fill(jetPt);

      // if(jetPt < 30 && partonFlavor == 5){
      //   hSoftJetsPhi->Fill(jetPhi);
      //   hSoftJetsEta->Fill(jetEta);
      //   hJetPt_BHadronPt_LowPt->Fill((*iMatch).second.getbHadrons().at(0)->pt(),jetPt);
      // }

      if ( jetPt < 20 ) continue;

      hPartonFlavorNew->Fill( partonFlavourToChar(partonFlavor), 1 );
      hPartonFlavorNew_Phi->Fill( jetPhi, partonFlavourToChar(partonFlavor), 1 );
      hPartonFlavorNew_Eta->Fill( jetEta, partonFlavourToChar(partonFlavor), 1 );
      hPartonFlavorNew_Pt->Fill( jetPt, partonFlavourToChar(partonFlavor), 1 );
      char* f = const_cast<char*>( partonFlavourToChar(partonFlavor) );
      //yes the line below is ugly, but it was a quick way to get the job done
      if (partonFlavor == 1 || partonFlavor == 2 || partonFlavor == 3 || partonFlavor == 21) f = const_cast<char*>( hadronFlavourToChar(0) );
      hPartonFlavor_HadronFlavor->Fill( hadronFlavourToChar(hadronFlavor), f, 1);


    } //end loop over new jet matches


}


// ------------ method called once each job just before starting event loop  ------------
void 
PartonFlavorComparison::beginJob()
{

  hPartonFlavorOld_Phi = fs->make<TH2D>("hPartonFlavorOld_Phi", "Parton Flavor vs. Phi",300,-3.15,3.15,7,0,7);
  hPartonFlavorNew_Phi = fs->make<TH2D>("hPartonFlavorNew_Phi", "Parton Flavor vs. Phi",300,-3.15,3.15,7,0,7);

  hPartonFlavorOld_Eta = fs->make<TH2D>("hPartonFlavorOld_Eta", "Parton Flavor vs. Eta",600,-6,6,7,0,7);
  hPartonFlavorNew_Eta = fs->make<TH2D>("hPartonFlavorNew_Eta", "Parton Flavor vs. Eta",600,-6,6,7,0,7);

  hPartonFlavorOld_Pt = fs->make<TH2D>("hPartonFlavorOld_Pt", "Parton Flavor vs. Pt",500,0,500,7,0,7);
  hPartonFlavorNew_Pt = fs->make<TH2D>("hPartonFlavorNew_Pt", "Parton Flavor vs. Pt",500,0,500,7,0,7);

  hJetPhi = fs->make<TH1D>("hJetPhi","All B Jet Phi",300,-3.15,3.15);
  hJetEta = fs->make<TH1D>("hJetEta","All B Jet Eta",600,-6,6);
  hJetPt = fs->make<TH1D>("hJetPt", "All B Jet pT",500,0,500);

  hHardestBJetPhi = fs->make<TH1D>("hHardJetsPhi","Phi of Hardest B Jet",300,-3.15,3.15);
  hHardestBJetEta = fs->make<TH1D>("hHardJetsEta","Eta of Hardest B Jet",600,-6,6);
  hHardestBJetPt = fs->make<TH1D>("hHardJetsPt", "pT of Hardest B Jet",500,0,500);

  hSecondHardestBJetPhi = fs->make<TH1D>("hSecondHardestBJetPhi","Phi of Second Hardest B Jet",300,-3.15,3.15);
  hSecondHardestBJetEta = fs->make<TH1D>("hSecondHardestBJetEta","Eta of Second Hardest B Jet",600,-6,6);
  hSecondHardestBJetPt = fs->make<TH1D>("hSecondHardestBJetPt", "pT of Second Hardest B Jet",500,0,500);

  hSoftJetsPhi = fs->make<TH1D>("hSoftJetsPhi","Phi of Jets with pT < 30 GeV",300,-3.15,3.15);
  hSoftJetsEta = fs->make<TH1D>("hSoftJetsEta","Eta of Jets with pT < 30 GeV",600,-6,6);

  hJetPt_BHadronPt_HighPt = fs->make<TH2D>("hJetPt_BHadronPt_HighPt", "Jet pT vs. B Hadron pT (high pT jets)",500,0,500,500,0,500);
  hJetPt_BHadronPt_LowPt = fs->make<TH2D>("hJetPt_BHadronPt_LowPt", "Jet pT vs. B Hadron pT (low pT jets)",500,0,500,500,0,500);

  hNumBHadrons = fs->make<TH1D>("hNumBHadrons","Number of b Hadrons Clustered",11,-0.5,10.5);
  hNumCHadrons = fs->make<TH1D>("hNumCHadrons","Number of c Hadrons Clustered",16,-0.5,15.5);
  hNumPartons = fs->make<TH1D>("hNumPartons","Number of Partons Clustered",501,-0.5,500);
  hNumLeptons = fs->make<TH1D>("hNumLeptons","Number of Leptons Clustered",16,-0.5,15.5);

  hPartonFlavorNew = fs->make<TH1D>("hPartonFlavorNew","Jet Parton Flavor Profile",7,0,7);

  hJetPt_LightQuarkPt = fs->make<TH2D>("hJetPt_LightQuarkPt", "Jet pT vs. Light Quark pT",500,0,500,500,0,500);
  hJetPt_GluonPt = fs->make<TH2D>("hJetPt_GluonPt", "Jet pT vs. Gluon pT",500,0,500,500,0,500);
  hPartonFlavor_HadronFlavor = fs->make<TH2D>("hPartonFlavor_HadronFlavor","Parton and Hadron Flavor Comparison",3,0,3,4,0,4);


}

// ------------ method called once each job just after ending the event loop  ------------
void 
PartonFlavorComparison::endJob()
{
  hPartonFlavorNew->LabelsOption("a","X");
  hPartonFlavorNew_Pt->LabelsOption("a","Y");
  hPartonFlavorNew_Eta->LabelsOption("a","Y");
  hPartonFlavorNew_Phi->LabelsOption("a","Y");

  hPartonFlavor_HadronFlavor->LabelsOption("a","X");
  hPartonFlavor_HadronFlavor->LabelsOption("a","Y");

}

// ------------ method called when starting to processes a run  ------------
void 
PartonFlavorComparison::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PartonFlavorComparison::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PartonFlavorComparison::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PartonFlavorComparison::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PartonFlavorComparison::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PartonFlavorComparison);
               