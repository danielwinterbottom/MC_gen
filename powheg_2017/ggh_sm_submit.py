from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_SM-filter'
config.General.workArea        = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_SM-filter'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'ggHnoSpin_SM.py'

config.Data.outputPrimaryDataset = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_SM-filter'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 2000
config.Data.totalUnits           = 20000000
config.Data.outLFNDirBase        = '/store/user/%s/POWHEG_2017/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'GluGluHToTauTau_M125_13TeV_powheg_pythia8_SM-filter'

#config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'

