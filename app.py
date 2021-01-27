#!/usr/bin/env python3

from aws_cdk import core

from finalv1.As3create import MyProjectStack
from finalv1.Bgluedbcreate import GluedemoStack
from finalv1.Dcrawlercreate import GluecrawlerStack
from finalv1.Clambda import S3LambdaStack
from finalv1.Fgluejob import Gluejob1Stack
from finalv1.Gwfcreate import WF



app = core.App()
MyProjectStack(app, "As3create")
GluedemoStack(app, "Bgluedbcreate")
S3LambdaStack(app, "Clambda")
GluecrawlerStack(app, "Dcrawlercreate")
Gluejob1Stack(app, "Fgluejob")
WF(app, "Gwfcreate")

app.synth()
