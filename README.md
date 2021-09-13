# aws-step-functions
Brief Tutorial on AWS Step Functions

Watch [Walkthrough on O'Reilly](https://learning.oreilly.com/videos/data-engineering-with/6132021VIDEOPAIML/)

## Overview

The overall idea is to chain AWS Lambda functions together where the input of one feeds into another function.

![visual-workflow](https://user-images.githubusercontent.com/58792/133004789-b237b7f8-536f-49ff-a84d-bc28a49655a2.png)

![score](https://user-images.githubusercontent.com/58792/133004839-be15f663-e469-4fdd-8ed8-5ba7598a7aee.png)

![step-function-out](https://user-images.githubusercontent.com/58792/133004976-f30e2821-0236-41eb-bd70-d1876d71cc0c.png)

### You can invoke the step functions or individual lambdas via the AWS CLI



#### List AWS Step Functions
`aws stepfunctions list-state-machines`

<img width="1238" alt="cloud-shell" src="https://user-images.githubusercontent.com/58792/133125070-f2ac2bcb-2a57-4eb6-a010-83383b5acc98.png">

#### Execute Step Functions

`aws stepfunctions start-execution --state-machine-arn "arn:aws:states:us-east-1:561744971673:stateMachine:Demo-Customer-Service-System" --input "{\"phrase\" : \"Today is a beautiful day\"}"`

This invokes the step function remotely which is a powerful way to do serverless Data Engineering.

<img width="1280" alt="step-functions" src="https://user-images.githubusercontent.com/58792/133126314-35e3eb01-a1dc-4e5f-afa5-6d6381269990.png">


#### List AWS Lambdas

`aws lambda list-functions`

<img width="1280" alt="Screen Shot 2021-09-13 at 1 05 16 PM" src="https://user-images.githubusercontent.com/58792/133126947-7f7d4e97-3af1-407c-8d84-7dfe193286b9.png">



## Resources

* [Sample Blank Python Lambda with Cloud Formation](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-python)
* [Python SAM Lambda](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-python)
* [Step Function Documentation](https://docs.aws.amazon.com/cli/latest/reference/stepfunctions/start-execution.html)

