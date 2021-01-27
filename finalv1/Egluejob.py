from aws_cdk import (
    aws_glue as glue,
    aws_iam as iam,
    core
    )
from aws_cdk.aws_stepfunctions_tasks import GlueStartJobRun
import boto3
class Gluejob1Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        glue = boto3.client(service_name='glue', region_name='us-east-1',endpoint_url='https://glue.us-east-1.amazonaws.com')

        myJob = glue.create_job(Name='sample', Role='arn:aws:iam::919238404395:role/service-role/AWSGlueServiceRole-my_2nd_iamrole',
        Command={'Name': 'glueetl','ScriptLocation': 's3://nikhils3/titanicjob.py'})
        
        myNewJobRun = glue.start_job_run(JobName=myJob['Name'])

        #print(status['JobRun']['JobRunState'])
        
