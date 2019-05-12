# AWS Cloud Track Demo

#### 1.	Introduce aws cloud architecture with Postgres/Oracle RDS integration
##### 2.	Talk concept of creating a draft job in the Web UI and submitting it for promotion
##### 3.	Create sample workflow in the Web UI planning domain
##### 4.	Order the jobs to run (Do this as admin user so that the jobs will order and run
 
## 5.	Workload Change
##### a.	Log in as developer ID and create a new job
##### b.	Attach the job to a site standard
##### c.	Once done, submit the job
##### d.	Log in as orchestration admin and mediate the newly created developer job
##### e.	Make some changes and refer them back to the developer for agreement
##### f.	Log back in as developer and agree.  Add notes to the workflow.
##### g.	Return to the orchadmin user and check the job in and run it.
 
## 6.	Automation API
##### a.	Open Eclipse (or your choice of IDE)
##### b.	Use the samples to show WCM from the IDE
#####  i.	Create a standard job and submit it - (If you are logged in as developer you should get a response that you are not authorised and should use a site standard)
#####  ii.	Insert a SiteStandard "key": "value" and resubmit the job with some incorrect fields
#####  iii.	Repair the job according to the errors returned when deploying
#####  iv.	Redeploy the job once all errors are resolved.
 
## 7.	AWS service integration
##### a.	Create and demonstrate an MFT job that transfers from one instance to s3
 
##### b.	Lambda Demo
#####  i.	Log in to the aws console and navigate to the Lambda Functions screen
#####  ii.	Find the Lambda function that will be demonstrated for even based orchestration
#####  iii.	Show the S3 to Lambda connection and the Lambda to Cloud watch
#####  iv.	Go to the S3 bucket that contains the master.json file with the workflow in it
#####  v.	Navigate to either your IDE or cmdline and perform an S3 copy of a .trig file to the s3 bucket described in the lambda trigger function
#####  vi.	Navigate to the Control-M Web UI and show the dynamically generated workflow in the UI.
#####  vii.	Navigate to Cloud watch and show the resultant logs of the triggered lambda function

