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

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:ttbarevents_pythia6.root'
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
