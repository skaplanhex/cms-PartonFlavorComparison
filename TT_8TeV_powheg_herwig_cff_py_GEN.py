# Auto generated configuration file
# using: 
# Revision: 1.381.2.27 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EightTeV/TT_8TeV_powheg_herwig_cff.py Configuration/GenProduction/python/EightTeV/TT_8TeV_powheg_herwig_cff.py --step GEN --beamspot Realistic8TeVCollision --conditions START52_V9::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       'file:tt_herwig6_lhe2edm.root'
    ),
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('Showering of Powheg TTbar events with Herwig+Jimmy, 7 TeV, AUET2'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/TT_8TeV_powheg_herwig_cff.py,v $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('tt_herwig6_pythiastatus_events.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V27::All', '')

process.generator = cms.EDFilter("Herwig6HadronizerFilter",
    HerwigParameters = cms.PSet(
        herwigParams = cms.vstring('RMASS(5) = 4.8       ! Set b mass.', 
            'RMASS(6) = 172.5     ! Set top mass.', 
            'SOFTME   = 0         ! Do not use soft matrix-element corrections.'),
        parameterSets = cms.vstring('herwigParams', 
            'herwigAUET2settings'),
        herwigAUET2settings = cms.vstring('MODPDF(1)  = 10042      ! PDF set according to LHAGLUE', 
            'MODPDF(2)  = 10042      ! CTEQ6L1', 
            'ISPAC      = 2', 
            'QSPAC      = 2.5', 
            'PTRMS      = 1.2', 
            'PTJIM      = 4.550      ! 3.224 * (runArgs.ecmEnergy/1800.)**0.231 @ 8 TeV', 
            'JMRAD(73)  = 2.386      ! inverse proton radius squared', 
            'PRSOF      = 0.0        ! prob. of a soft underlying event', 
            'MAXER      = 1000000    ! max error')
    ),
    doMPInteraction = cms.bool(True),
    useJimmy = cms.bool(True),
    herwigHepMCVerbosity = cms.untracked.bool(False),
    filterEfficiency = cms.untracked.double(1.0),
    herwigVerbosity = cms.untracked.int32(0),
    emulatePythiaStatusCodes = cms.untracked.bool(True),
    comEnergy = cms.double(8000.0),
    lhapdfSetPath = cms.untracked.string(''),
    printCards = cms.untracked.bool(False),
    crossSection = cms.untracked.double(149.6),
    maxEventsToPrint = cms.untracked.int32(0)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

