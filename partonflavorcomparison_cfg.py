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
      #'file:weirdsherpaevent.root'
       #  '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00188A34-1224-E211-833B-003048D4612C.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0031649A-1324-E211-AEB0-0025B3E06484.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00328E09-9724-E211-824C-003048D4610A.root',
       '/store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/006351C6-9DB7-E211-BE33-0024E8768D4E.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00A30CB5-D2B6-E211-8996-00266CF9B970.root',
        #'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00D05C95-2EB7-E211-85DD-008CFA008CC8.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00F4E9AC-CFB6-E211-8FA0-00266CF9B254.root',
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
      jetAlgorithm             = cms.string("AntiKt"),
      rParam                   = cms.double(0.5),
      ghostRescaling           = cms.double(1e-18),
      hadronFlavourHasPriority = cms.bool(True)
      )


process.TFileService = cms.Service("TFileService",
      fileName = cms.string(options.outfilename)
)
process.analyzerAK5 = cms.EDAnalyzer('PartonFlavorComparison',
         particleSource = cms.InputTag("genParticles"),
         jets = cms.InputTag("ak5GenJets"),
         jetFlavourByRef = cms.InputTag("flavourByRefAK5"),
         jetFlavourInfos = cms.InputTag("jetFlavourInfosAK5")
)


process.p = cms.Path((process.myPartons+process.selectedHadronsAndPartons)*(process.flavourByRefAK5+process.jetFlavourInfosAK5)*process.analyzerAK5)
