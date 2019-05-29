
import os
import sys

ctmserver = "ctmaws"
runID = "9eedd358-54ef-4f38-ab6b-6b4b0bbd6ee4"
jobID = "0024s"


#################################################
##These are the steps for provisioning an agent##
##Perform the steps from the host where you    ##
##want the agent installed                     ##
#################################################

def imagecheck():
    os.system('ctm provision images Linux')

def agentinstall():
    ctm provision install Agent.Linux workbench <agenthostname> 7010    
####Don't run this from here. Must be from the host where you want the agent installed
    
imagecheck()
#set aapi environment - Run this if you have multiple aapi environments and you need to set to a specific env
#os.system ('ctm env set houston')

# Return job logs from specific jobID
def getjoblogs ():
    os.system(('ctm run job:log::get ctmaws:%s')%(jobID)) #001vj

#getjoblogs()

