from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner'
config.General.workArea        = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'ggh_nopol.py'

config.Data.outputPrimaryDataset = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = 5000000
config.Data.outLFNDirBase        = '/store/user/%s/POWHEG_2016/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_nospinner'

#config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'

