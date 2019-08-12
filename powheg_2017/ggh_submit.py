from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext'
config.General.workArea        = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'ggHnoSpin_GEN.py'

config.Data.outputPrimaryDataset = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 16000
config.Data.totalUnits           = 60000000
config.Data.outLFNDirBase        = '/store/user/%s/POWHEG_2017/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner-filter-v2-ext'

#config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'

