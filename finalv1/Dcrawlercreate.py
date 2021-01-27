from aws_cdk import (aws_s3 as s3,aws_glue as glue,core)

class GluecrawlerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        glue_crawler = glue.CfnCrawler(
            self, 'phoenix_crawler',
            description="Glue Crawler for my-data-science-s3",
            name='phoenixcrawler',
            database_name='phoenixdb',
            #schedule={"scheduleExpression": "cron(45 12 * * ? *)"},
            role='arn:aws:iam::147279300887:role/successnick',
            targets={"s3Targets": [{"path": "s3://mydemoobuckett31"}]}
        )

