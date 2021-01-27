from aws_cdk import (aws_iam as iam,
    aws_lambda as lb,
    aws_s3 as s3,
    aws_s3_notifications as nik,
    core
)

class S3LambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        function = lb.Function(self, "lambda_function",
                                    runtime=lb.Runtime.PYTHON_3_7,
                                    handler="lambdahandler.lambda_handler",
                                    code=lb.Code.asset("./lambda"),
                                    role=iam.Role.from_role_arn(self, "Role", "arn:aws:iam::147279300887:role/successnick", mutable=False)
                                    #role=iam.RoleName('successnick')
                                     )



        # create s3 bucket
        bucket = s3.Bucket(self,"mybucket", bucket_name="mydemoobuckett31",public_read_access=True)
        core.CfnOutput(self,"mybucketname", value=bucket.bucket_name)
        
        

        # create s3 notification for lambda function
        notification = nik.LambdaDestination(function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)
