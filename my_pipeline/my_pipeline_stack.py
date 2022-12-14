from aws_cdk import (
    Stack,
    Environment
)
from aws_cdk.pipelines import ManualApprovalStep
from constructs import Construct
from my_pipeline.my_pipeline_app_stage import MyPipelineAppStage


from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

class MyPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("kashifalli/T2_cdk_pipeline","main"),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )
        testing_stage=pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=Environment(account="296174375647", region="ap-south-1")))
        testing_stage.add_post(ManualApprovalStep('approval'))

        testing_stage.add_post(ShellStep("validate",
            commands=['curl -Ssf https://google.com/']
            ))