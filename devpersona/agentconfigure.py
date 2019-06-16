
import os
import sys

ctmserver = "ctmaws"
runID = "efdae4e5-affc-4d52-9c4d-160989da8ca5"
jobID = "0005t"


#################################################
##These are the steps for provisioning an agent##
##Perform the steps from the host where you    ##
##want the agent installed                     ##
#################################################

#def imagecheck():
#    os.system('ctm provision images Linux')

#def agentinstall():
    #ctm provision install Agent.Linux workbench <agenthostname> 7010    
####Don't run this from here. Must be from the host where you want the agent installed
    
#imagecheck()
#set aapi environment - Run this if you have multiple aapi environments and you need to set to a specific env
#os.system ('ctm env set houston')

# Return job logs from specific jobID
def getjoblogs ():
    os.system(('ctm run job:log::get ctmaws:%s')%(jobID)) #001vj
getjoblogs()

