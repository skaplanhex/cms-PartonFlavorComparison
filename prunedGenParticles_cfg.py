
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
       # 'file:tt_pythia6_events.root',
      #'file:tt_pythia8_events.root'
       #  '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00188A34-1224-E211-833B-003048D4612C.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0031649A-1324-E211-AEB0-0025B3E06484.root',
       # '/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/00328E09-9724-E211-824C-003048D4610A.root',
       #'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/006351C6-9DB7-E211-BE33-0024E8768D4E.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00A30CB5-D2B6-E211-8996-00266CF9B970.root',
       #  'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00D05C95-2EB7-E211-85DD-008CFA008CC8.root',
       # 'root://xrootd.unl.edu//store/mc/Summer12_DR53X/TTJets_SemiLeptDecays_8TeV-sherpa/AODSIM/PU_S10_START53_V19-v1/20000/00F4E9AC-CFB6-E211-8FA0-00266CF9B254.root',
    )
)
process.prunedGenParticles = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
    "drop  *  ", #by default
    "keep (abs(pdgId) = 1 || abs(pdgId) = 2 || abs(pdgId) = 3 || abs(pdgId) = 4 || abs(pdgId) = 5 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72)",
    "keep (abs(pdgId) = 11 || abs(pdgId)= 13) & status = 1",
    "keep abs(pdgId)= 15 & status = 2",
    "++keep (400 < abs(pdgId) && abs(pdgId) < 600) || (4000 < abs(pdgId) && abs(pdgId) < 6000)",
    )
)

process.out = cms.OutputModule("PoolOutputModule",
      fileName = cms.untracked.string(options.outfilename)
)
process.p = cms.Path(process.prunedGenParticles)
process.ep = cms.EndPath(process.out)
