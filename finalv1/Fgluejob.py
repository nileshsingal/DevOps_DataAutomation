from aws_cdk import (
    aws_glue as glue,
    aws_iam as iam,
    core
    )
from aws_cdk.aws_stepfunctions_tasks import GlueStartJobRun
import boto3
import sys
class Gluejob1Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        client = boto3.client(service_name='glue', region_name='us-east-1',endpoint_url='https://glue.us-east-1.amazonaws.com')

        myJob = client.create_job(Name='phoenixjob', Role='arn:aws:iam::147279300887:role/successnick',
                                ExecutionProperty={'MaxConcurrentRuns': 123},
                                  Command={'Name': 'glueetl', 'ScriptLocation': 's3://phoenixbucketgrp25/weatheretld.py'}, Timeout=10)
    
        myNewJobRun = client.start_job_run(JobName=myJob['Name'])

        #print(status['JobRun']['JobRunState'])
        
