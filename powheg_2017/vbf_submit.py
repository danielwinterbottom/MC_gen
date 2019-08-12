from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'VBFHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext1'
config.General.workArea        = 'VBFHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext1'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'VBFnoSpin_GEN.py'

config.Data.outputPrimaryDataset = 'VBFHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext1'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 3000
config.Data.totalUnits           = 30000000
config.Data.outLFNDirBase        = '/store/user/%s/POWHEG_2017/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'VBFHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext1'

#config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'

