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
       # 'file:tt_herwig6_pythiastatus_events.root',
      # 'file:tt_pythia8_events.root',
      # 'file:tt_pythia8_events.root'
       #  '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00188A34-1224-E211-833B-003048D4612C.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0031649A-1324-E211-AEB0-0025B3E06484.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00328E09-9724-E211-824C-003048D4610A.root',
       #'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/006351C6-9DB7-E211-BE33-0024E8768D4E.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00A30CB5-D2B6-E211-8996-00266CF9B970.root',
       #  'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00D05C95-2EB7-E211-85DD-008CFA008CC8.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00F4E9AC-CFB6-E211-8FA0-00266CF9B254.root',

       # /TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM
       # '/store/mc/Summer12_DR53X/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7C-v1/00000/008BD264-1526-E211-897A-00266CFFA7BC.root',
       # '/store/mc/Summer12_DR53X/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7C-v1/00000/0AA5BB7F-0126-E211-8F23-002481E0D398.root',
       # '/store/mc/Summer12_DR53X/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7C-v1/00000/0ABEDFAF-8A25-E211-955D-003048F0E5B4.root',

       # /ZH_ZToLL_HToBB_M-125_8TeV-powheg-herwigpp/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM
       # '/store/mc/Summer12_DR53X/ZH_ZToLL_HToBB_M-125_8TeV-powheg-herwigpp/AODSIM/PU_S10_START53_V7A-v1/0000/58B9CF67-D8F5-E111-B651-001A645D4F7A.root',
       # '/store/mc/Summer12_DR53X/ZH_ZToLL_HToBB_M-125_8TeV-powheg-herwigpp/AODSIM/PU_S10_START53_V7A-v1/0000/58DB12E2-DFF5-E111-BC23-00215E2227D8.root',
       # '/store/mc/Summer12_DR53X/ZH_ZToLL_HToBB_M-125_8TeV-powheg-herwigpp/AODSIM/PU_S10_START53_V7A-v1/0000/5A3E6629-DBF5-E111-AF04-00215E221812.root',

       # /GluGluToHToBB_M-125_8TeV-powheg-pythia8/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM

       '/store/mc/Summer12_DR53X/GluGluToHToBB_M-125_8TeV-powheg-pythia8/AODSIM/PU_S10_START53_V7C-v1/10000/B23C2E63-4FA1-E211-BC07-003048679228.root',
       '/store/mc/Summer12_DR53X/GluGluToHToBB_M-125_8TeV-powheg-pythia8/AODSIM/PU_S10_START53_V7C-v1/10000/B4B64DF3-4BA1-E211-9CCB-0026189438FD.root',
       '/store/mc/Summer12_DR53X/GluGluToHToBB_M-125_8TeV-powheg-pythia8/AODSIM/PU_S10_START53_V7C-v1/10000/BA86FB89-4AA1-E211-A55C-003048678B34.root',
       '/store/mc/Summer12_DR53X/GluGluToHToBB_M-125_8TeV-powheg-pythia8/AODSIM/PU_S10_START53_V7C-v1/10000/C85DC6B2-49A1-E211-8F8D-002354EF3BE6.root',
       '/store/mc/Summer12_DR53X/GluGluToHToBB_M-125_8TeV-powheg-pythia8/AODSIM/PU_S10_START53_V7C-v1/10000/CCB0A5A6-47A1-E211-9936-00248C0BE014.root',
       '/store/mc/Summer12_DR53X/GluGluToHToBB_M-125_8TeV-powheg-pythia8/AODSIM/PU_S10_START53_V7C-v1/10000/D4BD03FB-43A1-E211-8997-00248C0BE018.root',

       # /TT_CT10_AUET2_8TeV-powheg-herwig/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM
       # '/store/mc/Summer12_DR53X/TT_CT10_AUET2_8TeV-powheg-herwig/AODSIM/PU_S10_START53_V19-v1/10000/08183209-09CB-E211-AB1E-003048FFD79C.root',
       # '/store/mc/Summer12_DR53X/TT_CT10_AUET2_8TeV-powheg-herwig/AODSIM/PU_S10_START53_V19-v1/10000/081ADBBC-F0CA-E211-A893-002618943962.root',
       # '/store/mc/Summer12_DR53X/TT_CT10_AUET2_8TeV-powheg-herwig/AODSIM/PU_S10_START53_V19-v1/10000/08372094-D0CA-E211-BBAA-0025905938D4.root',
    )
)

#to get ca4PFJets
from RecoJets.JetProducers.ca4PFJets_cfi import ca4PFJets
process.ca4PFJets = ca4PFJets.clone()

process.selectedHadronsAndPartons = cms.EDProducer('HadronAndPartonSelector',
           src = cms.InputTag("generator"),
           particles = cms.InputTag("genParticles"),
           partonMode = cms.string("Auto")
)
process.jetFlavourInfosAK5 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ak5PFJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartons","partons"),
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(False)
)
process.jetFlavourInfosKT6 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("kt6PFJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartons","partons"),
      jetAlgorithm             = cms.string("Kt"),
      rParam                   = cms.double(0.6),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(False)
)
process.jetFlavourInfosKT6Leptons = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("kt6PFJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartons","partons"),
      leptons                  = cms.InputTag("selectedHadronsAndPartons","leptons"),
      jetAlgorithm             = cms.string("Kt"),
      rParam                   = cms.double(0.6),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(False)
)
process.jetFlavourInfosCA4 = cms.EDProducer("JetFlavourClustering",
      jets                     = cms.InputTag("ca4PFJets"),
      bHadrons                 = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
      cHadrons                 = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
      partons                  = cms.InputTag("selectedHadronsAndPartons","partons"),
      jetAlgorithm             = cms.string("CambridgeAachen"),
      rParam                   = cms.double(0.4),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(False)
)
process.TFileService = cms.Service("TFileService",
      fileName = cms.string(options.outfilename)
)
process.analyzerAK5 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartons","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartons","leptons"),
         jets            = cms.InputTag("ak5PFJets"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5")
)
process.analyzerKT6 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartons","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartons","leptons"),
         jets            = cms.InputTag("kt6PFJets"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosKT6")
)
process.analyzerKT6Leptons = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartons","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartons","leptons"),
         jets            = cms.InputTag("kt6PFJets"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosKT6Leptons")
)
process.analyzerCA4 = cms.EDAnalyzer('PartonFlavorComparison',
         bHadrons        = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
         cHadrons        = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
         partons         = cms.InputTag("selectedHadronsAndPartons","partons"),
         leptons         = cms.InputTag("selectedHadronsAndPartons","leptons"),
         jets            = cms.InputTag("ca4PFJets"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosCA4")
)
# process.out = cms.OutputModule("PoolOutputModule",
#       fileName = cms.untracked.string("tt_herwig6_events_prunedGenParticles.root")
# )
process.p = cms.Path( (process.selectedHadronsAndPartons+process.ca4PFJets)
                *(process.jetFlavourInfosAK5+process.jetFlavourInfosKT6+process.jetFlavourInfosKT6Leptons+process.jetFlavourInfosCA4)
                *(process.analyzerAK5+process.analyzerKT6+process.analyzerKT6Leptons+process.analyzerCA4)
)
# process.ep = cms.EndPath(process.out)
# process.schedule = cms.Schedule(process.p,process.ep)

# process.p = cms.Path((process.myPartons+process.selectedHadronsAndPartons)
#   *process.genParticlesForJets*process.ak5GenJets
#   *(process.flavourByRefAK5+process.jetFlavourInfosAK5)*process.analyzerAK5)
