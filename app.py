#!/usr/bin/env python3
import aws_cdk as cdk
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app,"MyPipelineStack", 
    env=cdk.Environment(account="296174375647",region="ap-south-1"))
app.synth()