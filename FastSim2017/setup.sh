#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_12/src ] ; then 
 echo release CMSSW_9_4_12 already exists
else
scram p CMSSW CMSSW_9_4_12
fi
cd CMSSW_9_4_12/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIIFall17wmLHEGS-02398 --retry 2 --create-dirs -o Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-02398-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-02398-fragment.py ] || exit $?;

scram b
cd ../../
#cmsDriver.py Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-02398-fragment.py --fileout file:testFS.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIIFall17FSPrePremix-PUMoriond17_94X_mc2017_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent AODSIM --fast --datatier AODSIM --conditions 94X_mc2017_realistic_v15 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)" --step LHE,GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datamix PreMix --era Run2_2017_FastSim --python_filename run_fastsim.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1092 || exit $? ; 


