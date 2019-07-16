from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'GluGluToHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_FastSim'
config.General.workArea        = 'GluGluToHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_FastSim'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'run_fastsim.py'

config.Data.outputPrimaryDataset = 'GluGluToHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_FastSim'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 1000
config.Data.totalUnits           = 5000000
config.Data.outLFNDirBase        = '/store/user/%s/MG_FastSim/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'GluGluToHToTauTauPlusTwoJets_M125_13TeV_amcatnloFXFX_pythia8_FastSim'

#config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'

