
import os
import sys

ctmserver = "ctmaws"
runID = "1ef3af02-18d2-44a8-b20a-942568ac935f"
jobID = "00236"
#curjobs = "hou-workflow-hadoop.json" #hou-workflow-hadoop.json  #hou-workflow-hadoop_db.json

#set aapi environment - Run this if you have multiple aapi environments and you need to set to a specific env
#os.system ('ctm env set houston')

# Order/run a workflow using the aapi (Insert the path of your JSON files here -Set the curjobs variable to your JSON filename
#def wrkflo ():
#    os.system (('ctm run "C:\\Users\\ncullum\\Documents\\json\\%s"')%(curjobs))
#Git comment
#wrkflo()
def trackstatus ():
    os.system(('ctm run status %s')%(runID)) #5806063b-4e18-48c0-8c09-3aa3432f7f7b

#trackstatus()

# Return job logs from specific jobID
def getjoblogs ():
    os.system(('ctm run job:log::get ctmaws:%s')%(jobID)) #001vj

#getjoblogs()

# Return job output from specific jobID
def getjobout ():
    os.system(('ctm run job:output::get ctmaws:%s')%(jobID)) 

#getjobout()

def getjobjson ():
    os.system(('ctm deploy jobs::get -s "ctm=ctmaws&folder=MultiFlow"'))

getjobjson()

    

#    Get all the hostgroups of the specified Control-M Server.
def gethg ():
    hostgrps=os.system(('ctm config server:hostgroups::get %s')%(ctmserver))
    print(hostgrps)
#gethg() #Unhash this function call to run the function

#    Get status of jobs that match the requested search criteria. Search fields are jobname, ctm, folder, host, application, subApplication, status and description
#      run jobs:status::get [limit] -s <search query>
def getstatus ():
    #os.system (('ctm run jobs:status:: -s ctm=%s')%(ctmserver))
    os.system (('ctm run jobs:status::get -s "jobname=NCU_Command_test_job&application=NCU_ncc*&status=Ended OK,Ended Not OK,Executing"'))

#getstatus() #Unhash this function call to run the function

#  Get all the agents of the specified Control-M Server.
#getag = os.system('ctm config server:agents::get hou-presrv9')

def getagents ():
    getag = os.system(('ctm config server:agents::get %s')%(ctmserver))

#getagents() #Unhash this function call to run the function

#    Get all events records for specific search. Search fields are ctm=*, name=*, date=*
def getevents ():
    os.system('ctm run events::get -s ctm=hou-presrv9')

#getevents() #Unhash this function call to run the function

    #os.system ('ctm

# Run and track Control-M jobs

#Run jobs according to given definitions file (JSON or zip).
#     run <jobDefinitionsFile> -i

#    Add a new event. date may be of format MMDD, ODAT to set current controlm date, STAT to set no date. default value is ODAT.
#      run event::add <ctm> <name> <date>

#    Delete a event.
#      run event::delete <ctm> <name> <date>


#    confirm a job that waits for confirmation
#      run job::confirm <jobId>

#    mark delete as deleted
#      run job::delete <jobId>

#    free the job
#      run job::free <jobId>

#    hold the job
#      run job::hold <jobId>

#    Abort job execution.
#      run job::kill <jobId>

#    Get the job execution log.
#      run job:log::get <jobId>

#    Get the output returned from a job.
#      run job:output::get <jobId> [runNo]

#    Run an already executed job (again).
#      run job::rerun <jobId>

#    start a job immediately
#      run job::runNow <jobId>

#    set job&#39;s end status to OK, post processing action
#      run job::setToOk <jobId>

#    Get the job status.
#      run job:status::get <jobId>

#    recover a mark for deletion job
#      run job::undelete <jobId>

#    Run jobs from selected folder according to given filter
#      run order <ctm> <folder> [jobs] -i

#    Add a new quantitative resource.
#      run resource::add <ctm> <name> <max>

#   Update a quantitative resource.
#      run resource::update <ctm> <name> <max>

#    Delete a quantitative resource.
#      run resource::delete <ctm> <name>

#    Get all resources records matching search. Search fields are ctm=*, name=*
#      run resources::get  -s <search query>

#    Run status of jobs started with the Run service.
#      run status <runId> [startIndex] -i

#    Usage: [command] [options]

#    Options:
#      -e, --environment <env>       Use <env> environment for this command
#      -t, --token <token>           Use the user token <token> for this command
#      -f, --file <input file.json>  Use input file for more detailed advanced configurations
#      -s, --search <search query>   Use a query to refine/limit the results
#      -i, --interactive             View result in an interactive user interface
#      -o, --outputfile <file path>  Download results to file

#C:\Users\ncullum\Documents\json>ctm deploy jobs::get JSON -s ctm=workbench&folder=*
#{"errors":[{"message":"Failed to get Folder data. Folder name must be given in the search query"}]}
#'folder' is not recognized as an internal or external command,
#operable program or batch file.

#C:\Users\ncullum\Documents\json>ctm deploy jobs::get JSON -s ctm=workbench&folder=*
#    Add an agent to Control-M Server. This command does not install or configure the agent. It only defines the agent in the system.
#      config server:agent::add <ctm> <host> <port>

#    Delete an agent from a Control-M Server. This will not shut the agent down. It only disconnects and removes it from the list.
#     config server:agent::delete <ctm> <agent>

#  Set the value of the specified parameter in the specified agent.
#      config server:agent:param::set <ctm> <agent> <name> <value>

#   Get all the parameters of the specified Control-M Agent.
#      config server:agent:params::get <ctm> <agent>



#   Add an agent to hostgroup. Create the the hostgroup if it does not exist.
#    config server:hostgroup:agent::add <ctm> <hostgroup> <host>

#    Delete an agent from the specified hostgroup. If the group is empty it will also be deleted.
#     config server:hostgroup:agent::delete <ctm> <hostgroup> <host>

#  Get the agents that compose the specified hostgroup
#     config server:hostgroup:agents::get <ctm> <hostgroup>

#   Get all the parameters of the specified Control-M Server.
#     config server:params::get <ctm>

#    Add a remote host to Control-M Server.
#      config server:remotehost::add <ctm> <remotehost> [port] -f <configuration file>

#    Get the remote host configuration properties from the Control-M Server
#      config server:remotehost::get <ctm> <remotehost>

#    Delete a remote host from a Control-M Server.
#      config server:remotehost::delete <ctm> <remotehost>

#    Authorized known ssh remote host.
#      config server:remotehost::authorize <ctm> <remotehost>

#    Get all the remote hosts of the specified Control-M Server.
#      config server:remotehosts::get <ctm>

#    Get the names and hostnames of all Control-M Servers in the system.
#      config servers::get

#    Usage: [command] [options]
#    Options:
#      -e, --environment <env>       Use <env> environment for this command
#      -t, --token <token>           Use the user token <token> for this command
#      -f, --file <input file.json>  Use input file for more detailed advanced configurations
#      -s, --search <search query>   Use a query to refine/limit the results
#      -i, --interactive             View result in an interactive user interface
#      -o, --outputfile <file path>  Download results to file


