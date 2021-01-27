from aws_cdk import (aws_s3 as s3,aws_glue as glue,core)


class MyProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        bucket = s3.Bucket(self,"phoenixoutput12", bucket_name="phoenixoutput",public_read_access=True)
        bucket1 = s3.Bucket(self, "phoenixbucketgrp2",bucket_name="phoenixbucketgrp25", public_read_access=True)
       # core.CfnOutput(self,"phoenixbucket1", value=bucket.bucket_name)
       
       
       # Destination Bucket
