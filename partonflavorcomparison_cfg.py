from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('outfilename',
                 "outfile.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "Name of output file"
                 )
options.register('useSubjets',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  'Whether or not to analyze subjet based tagging'
                  )
## 'maxEvents' and 'outputFile' are already registered by the Framework, changing default value
options.setDefault('maxEvents', 15)
#options.setDefault('outputFile', 'jetmatchingplots.root')
options.parseArguments()

import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
      # 'file:tt_herwig6_herwigstatus_events.root',
       'file:tt_herwig6_pythiastatus_events.root',
      # 'file:tt_pythia8_events.root',
      # 'file:tt_pythia8_events.root'
       #  '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00188A34-1224-E211-833B-003048D4612C.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0031649A-1324-E211-AEB0-0025B3E06484.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00328E09-9724-E211-824C-003048D4610A.root',
       #'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/006351C6-9DB7-E211-BE33-0024E8768D4E.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00A30CB5-D2B6-E211-8996-00266CF9B970.root',
       #  'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00D05C95-2EB7-E211-85DD-008CFA008CC8.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00F4E9AC-CFB6-E211-8FA0-00266CF9B254.root',
    )
)
process.prunedGenParticlesForJetFlavorPt0 = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
    "drop  *  ", #by default
    "keep (abs(pdgId) = 4 || abs(pdgId) = 5) & (status = 2 || status = 11 || status = 71 || status = 72)",
    "keep (abs(pdgId) = 1 || abs(pdgId) = 2 || abs(pdgId) = 3 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72)",
    "keep (abs(pdgId) = 11 || abs(pdgId)= 13) & status = 1",
    "keep abs(pdgId)= 15 & status = 2",
    "keep (400 < abs(pdgId) && abs(pdgId) < 600) || (4000 < abs(pdgId) && abs(pdgId) < 6000)",
    )
)
process.prunedGenParticlesForJetFlavorPt5 = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
    "drop  *  ", #by default
    "keep (abs(pdgId) = 4 || abs(pdgId) = 5) & (status = 2 || status = 11 || status = 71 || status = 72)",
    "keep (abs(pdgId) = 1 || abs(pdgId) = 2 || abs(pdgId) = 3 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72) & (pt>5)",
    "keep (abs(pdgId) = 11 || abs(pdgId)= 13) & status = 1",
    "keep abs(pdgId)= 15 & status = 2",
    "keep (400 < abs(pdgId) && abs(pdgId) < 600) || (4000 < abs(pdgId) && abs(pdgId) < 6000)",
    )
)
process.prunedGenParticlesForJetFlavorPt10 = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
    "drop  *  ", #by default
    "keep (abs(pdgId) = 4 || abs(pdgId) = 5) & (status = 2 || status = 11 || status = 71 || status = 72)",
    "keep (abs(pdgId) = 1 || abs(pdgId) = 2 || abs(pdgId) = 3 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72) & (pt>10)",
    "keep (abs(pdgId) = 11 || abs(pdgId)= 13) & status = 1",
    "keep abs(pdgId)= 15 & status = 2",
    "keep (400 < abs(pdgId) && abs(pdgId) < 600) || (4000 < abs(pdgId) && abs(pdgId) < 6000)",
    )
)
process.prunedGenParticlesForJetFlavorPt15 = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
    "drop  *  ", #by default
    "keep (abs(pdgId) = 4 || abs(pdgId) = 5) & (status = 2 || status = 11 || status = 71 || status = 72)",
    "keep (abs(pdgId) = 1 || abs(pdgId) = 2 || abs(pdgId) = 3 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72) & (pt>15)",
    "keep (abs(pdgId) = 11 || abs(pdgId)= 13) & status = 1",
    "keep abs(pdgId)= 15 & status = 2",
    "keep (400 < abs(pdgId) && abs(pdgId) < 600) || (4000 < abs(pdgId) && abs(pdgId) < 6000)",
    )
)
process.myPartons = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)
process.selectedHadronsAndPartons = cms.EDProducer('HadronAndPartonSelector',
           src = cms.InputTag("generator"),
           particles = cms.InputTag("genParticles"),
           partonMode = cms.string("Auto")
)
process.selectedHadronsAndPartonsPt0 = cms.EDProducer('HadronAndPartonSelector',
           src = cms.InputTag("generator"),
           particles = cms.InputTag("prunedGenParticlesForJetFlavorPt0"),
           partonMode = cms.string("Auto")
)
process.selectedHadronsAndPartonsPt5 = cms.EDProducer('HadronAndPartonSelector',
           src = cms.InputTag("generator"),
           particles = cms.InputTag("prunedGenParticlesForJetFlavorPt5"),
           partonMode = cms.string("Auto")
)
process.selectedHadronsAndPartonsPt10 = cms.EDProducer('HadronAndPartonSelector',
           src = cms.InputTag("generator"),
           particles = cms.InputTag("prunedGenParticlesForJetFlavorPt10"),
           partonMode = cms.string("Auto")
)
process.selectedHadronsAndPartonsPt15 = cms.EDProducer('HadronAndPartonSelector',
           src = cms.InputTag("generator"),
           particles = cms.InputTag("prunedGenParticlesForJetFlavorPt15"),
           partonMode = cms.string("Auto")
)
from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJets
process.genParticlesForJets = genParticlesForJets.clone()

from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
process.ak5GenJets = ak5GenJets.clone()
process.flavourByRefAK5 = cms.EDProducer("JetPartonMatcher",
 jets = cms.InputTag("ak5GenJets"),
 coneSizeToAssociate = cms.double(0.3),
 partons = cms.InputTag("myPartons")
)
process.jetFlavourInfosAK5 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ak5GenJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartons","partons"),
      leptons                  = cms.InputTag("selectedHadronsAndPartons","leptons"),
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(True)
)
process.jetFlavourInfosAK5Pt0 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ak5GenJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt0","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt0","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartonsPt0","partons"),
      leptons                  = cms.InputTag("selectedHadronsAndPartonsPt0","leptons"),
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(True)
)
process.jetFlavourInfosAK5Pt5 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ak5GenJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt5","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt5","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartonsPt5","partons"),
      leptons                  = cms.InputTag("selectedHadronsAndPartonsPt5","leptons"),
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(True)
)
process.jetFlavourInfosAK5Pt10 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ak5GenJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt10","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt10","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartonsPt10","partons"),
      leptons                  = cms.InputTag("selectedHadronsAndPartonsPt10","leptons"),
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(True)
)
process.jetFlavourInfosAK5Pt15 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ak5GenJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt15","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartonsPt15","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartonsPt15","partons"),
      leptons                  = cms.InputTag("selectedHadronsAndPartonsPt15","leptons"),
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(True)
)
process.TFileService = cms.Service("TFileService",
      fileName = cms.string(options.outfilename)
)
process.analyzerAK5 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartons","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartons","leptons"),
         jets            = cms.InputTag("ak5GenJets"),
         jetFlavourByRef = cms.InputTag("flavourByRefAK5"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5")
)
process.analyzerAK5Pt0 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartonsPt0","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartonsPt0","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartonsPt0","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartonsPt0","leptons"),
         jets            = cms.InputTag("ak5GenJets"),
         jetFlavourByRef = cms.InputTag("flavourByRefAK5"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5Pt0")
)
process.analyzerAK5Pt5 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartonsPt5","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartonsPt5","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartonsPt5","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartonsPt5","leptons"),
         jets            = cms.InputTag("ak5GenJets"),
         jetFlavourByRef = cms.InputTag("flavourByRefAK5"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5Pt5")
)
process.analyzerAK5Pt10 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartonsPt10","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartonsPt10","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartonsPt10","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartonsPt10","leptons"),
         jets            = cms.InputTag("ak5GenJets"),
         jetFlavourByRef = cms.InputTag("flavourByRefAK5"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5Pt10")
)
process.analyzerAK5Pt15 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartonsPt15","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartonsPt15","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartonsPt15","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartonsPt15","leptons"),
         jets            = cms.InputTag("ak5GenJets"),
         jetFlavourByRef = cms.InputTag("flavourByRefAK5"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5Pt15")
)
# process.out = cms.OutputModule("PoolOutputModule",
#       fileName = cms.untracked.string("tt_herwig6_events_prunedGenParticles.root")
# )
process.p = cms.Path(
  (process.myPartons+process.prunedGenParticlesForJetFlavorPt0+process.prunedGenParticlesForJetFlavorPt5+process.prunedGenParticlesForJetFlavorPt10*process.prunedGenParticlesForJetFlavorPt15)
  *(process.selectedHadronsAndPartons+process.selectedHadronsAndPartonsPt0+process.selectedHadronsAndPartonsPt5+process.selectedHadronsAndPartonsPt10+process.selectedHadronsAndPartonsPt15)
  *(process.flavourByRefAK5+process.jetFlavourInfosAK5+process.jetFlavourInfosAK5Pt0+process.jetFlavourInfosAK5Pt5+process.jetFlavourInfosAK5Pt10+process.jetFlavourInfosAK5Pt15)
  *(process.analyzerAK5+process.analyzerAK5Pt0+process.analyzerAK5Pt5+process.analyzerAK5Pt10+process.analyzerAK5Pt15)
)
# process.ep = cms.EndPath(process.out)
# process.schedule = cms.Schedule(process.p,process.ep)

# process.p = cms.Path((process.myPartons+process.selectedHadronsAndPartons)
#   *process.genParticlesForJets*process.ak5GenJets
#   *(process.flavourByRefAK5+process.jetFlavourInfosAK5)*process.analyzerAK5)
