# Pipelines para deployment no ECS

## Deploy to ECS Fargate

- Pipeline creation option `Deploy to ECS Fargate`
- Choose the root ECR repository

## ECS

- Select `ECS` as the Deploy Provider option for the pipeline
- Deploy IAM Role needs to have ECS access

## ECS Blue/Green

- Select `ECS Blue/Green` as the Deploy Provider option for the pipeline
- Criar ECS service com o deployment controller `CODE_DEPLOY`:
```
aws ecs create-service \
  --cluster <ECS-CLUSTER> \
  --service-name <SERVICE-NAME> \
  --task-definition <TASK-NAME>:<REVISION> \
  --desired-count 1 \
  --launch-type FARGATE \
  --platform-version LATEST \
  --deployment-controller type=CODE_DEPLOY \
  --load-balancers "targetGroupArn=<TG-ARN>,containerName=Main,containerPort=8080" \
  --network-configuration "awsvpcConfiguration={subnets=[<SUBNET-ID>,<SUBNET-ID>],securityGroups=[<SG-ID>]}"   
```
- Create CodeDeploy Application
- Create CodeDeploy Deployment Group
- requer build artifact `imageDetail.json`
- requer `appspec.yaml`
- requer `taskdef.json` 

## CodeDeploy

- Select `CodeDeploy` as the Deploy Provider option for the pipeline
- Requer `appspec.yaml` 
- Todas as configurações são feitas via appspec