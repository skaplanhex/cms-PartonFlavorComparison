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

      // ----------member data ---------------------------
      edm::Service<TFileService> fs;
      edm::InputTag particles_,jets_,flavorByDR_,flavorByClustering_;
      edm::Handle< reco::GenParticleCollection > particles;
      edm::Handle< edm::View< reco::Jet > > jets;
      edm::Handle< reco::JetMatchedPartonsCollection > flavorByDR;
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
  particles_ = iConfig.getParameter<InputTag>("particleSource");
  jets_ = iConfig.getParameter<InputTag>("jets");
  flavorByDR_ = iConfig.getParameter<InputTag>("jetFlavourByRef");
  flavorByClustering_ = iConfig.getParameter<InputTag>("jetFlavourInfos");

}


PartonFlavorComparison::~PartonFlavorComparison()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

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

    iEvent.getByLabel(particles_,particles);
    iEvent.getByLabel(jets_, jets);
    iEvent.getByLabel(flavorByDR_,flavorByDR);
    iEvent.getByLabel(flavorByClustering_, flavorByClustering );

    for (reco::JetFlavourInfoMatchingCollection::const_iterator iMatch = flavorByClustering->begin(); iMatch != flavorByClustering->end(); ++iMatch) {
      
      int currentIndex = iMatch - flavorByClustering->begin();
      //check to see if jets between collections match
      if( edm::Ptr<reco::Candidate>((*iMatch).first.id(), (*iMatch).first.get(), (*iMatch).first.key())  != 
        edm::Ptr<reco::Candidate>((*flavorByDR)[currentIndex].first.id(), (*flavorByDR)[currentIndex].first.get(), (*flavorByDR)[currentIndex].first.key()) ) continue;

      const reco::Jet* iJet  = (*iMatch).first.get();
      int oldPartonFlavor = 0;
      const reco::GenParticleRef partonRef = (*flavorByDR)[currentIndex].second.algoDefinitionParton();
      if ( partonRef.isNonnull() ) oldPartonFlavor = partonRef.get()->pdgId();
      int newPartonFlavor = (*iMatch).second.getPartonFlavour();

      double jetPt = iJet->pt();
      double jetEta = iJet->eta();
      double jetPhi = iJet->phi();

      hJetPt->Fill(jetPt);
      hJetEta->Fill(jetEta);
      hJetPhi->Fill(jetPhi);

      hPartonFlavorOld_Phi->Fill( jetPhi, partonFlavourToChar(oldPartonFlavor), 1 );
      hPartonFlavorNew_Phi->Fill( jetPhi, partonFlavourToChar(newPartonFlavor), 1 );

      hPartonFlavorOld_Eta->Fill( jetEta, partonFlavourToChar(oldPartonFlavor), 1 );
      hPartonFlavorNew_Eta->Fill( jetEta, partonFlavourToChar(newPartonFlavor), 1 );

      hPartonFlavorOld_Pt->Fill( jetPt, partonFlavourToChar(oldPartonFlavor), 1 );
      hPartonFlavorNew_Pt->Fill( jetPt, partonFlavourToChar(newPartonFlavor), 1 );


    }



}


// ------------ method called once each job just before starting event loop  ------------
void 
PartonFlavorComparison::beginJob()
{

  hPartonFlavorOld_Phi = fs->make<TH2D>("hPartonFlavorOld_Phi", "Parton Flavor vs. Phi",150,0,3.141593,7,0,7);
  hPartonFlavorNew_Phi = fs->make<TH2D>("hPartonFlavorNew_Phi", "Parton Flavor vs. Phi",150,0,3.141593,7,0,7);

  hPartonFlavorOld_Eta = fs->make<TH2D>("hPartonFlavorOld_Eta", "Parton Flavor vs. Eta",600,-6,6,7,0,7);
  hPartonFlavorNew_Eta = fs->make<TH2D>("hPartonFlavorNew_Eta", "Parton Flavor vs. Eta",600,-6,6,7,0,7);

  hPartonFlavorOld_Pt = fs->make<TH2D>("hPartonFlavorOld_Pt", "Parton Flavor vs. Pt",500,0,500,7,0,7);
  hPartonFlavorNew_Pt = fs->make<TH2D>("hPartonFlavorNew_Pt", "Parton Flavor vs. Pt",500,0,500,7,0,7);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PartonFlavorComparison::endJob()
{
  hPartonFlavorOld = hPartonFlavorOld_Pt->ProjectionY();
  hPartonFlavorNew = hPartonFlavorNew_Pt->ProjectionY();

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
