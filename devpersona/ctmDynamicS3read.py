import boto3
import json
import pprint
import collections
import requests

#def lambda_handler(event, context): # unhash when packaging into lambda
def lambda_handler():
    s3 = boto3.resource('s3')
#Define master object
    obj = s3.Object('ncu-schumi', 'master.json')

#Define object for manipulation
    objectdata = s3.Object('ncu-schumi', 'procfile.json')

#Load master object
    file_content = json.loads(obj.get()['Body'].read().decode('utf-8'),object_pairs_hook=collections.OrderedDict)


    infilename = 'neilc.txt'
    file_command = '/home/neilc/myscript.sh'
    proc_step = file_command + " " + infilename

#Manipulate JSON key values
    tmp = file_content
    file_content["quicktest"][infilename] = file_content["quicktest"]["DYNFILE"]
    del file_content["quicktest"]["DYNFILE"]

    newfile_content = json.dumps(file_content, ensure_ascii=False)

    objectdata.put(Body=newfile_content)
#pprint.pprint(newfile_content)

#Open object in correct format for REST submission
    ctmobj = s3.Object('ncu-schumi', 'procfile.json')
    ctm_content = ctmobj.get()['Body'].read().decode('utf-8')

#Define endpoint and submit payload    
    endpoint_url='https://ec2-35-177-38-80.eu-west-2.compute.amazonaws.com:8443/'  
    login_url=endpoint_url+'automation-api/session/login'
    user='emuser'                                                       
    password='ncpass'                                                   
    payload = {'username': user, 'password': password}
    headers = {'Content-type': 'application/json'}
#  Request for token   
    r = requests.post(login_url, data=json.dumps(payload),verify=False,headers=headers)
    r_json=json.loads(r.text)
    token=r_json['token']
#print(token)
#ctm='ctmaws'
    endpoint_run=endpoint_url+'automation-api'
    header_auth_val= 'Bearer '+ token
    headers.update(Authorization=header_auth_val)
#  Request for submitting and running a JSON payload  
    payload = ctm_content
#r = requests.post(endpoint_run, data=payload,verify=False,headers=headers)
#print(r.text)
    uploaded_files = [
        ('jobDefinitionsFile', ('Jobs.json', payload, 'application/json'))
    ]
    r = requests.post(endpoint_run + '/run', files=uploaded_files, headers={'Authorization': 'Bearer ' + token}, verify=False)
    print(r.content)
#  Request for logout
    endpoint_logout=endpoint_url+'automation-api/session/logout'
    r = requests.post(endpoint_logout, verify=False,headers=headers)
    print(json.loads(r.text))
    return 'Request for delete received'

lambda_handler()    #Hash out when packaging for lambda