# lembretes-estudos

## Itens

Todos os itens a seguir devem ser realizados em todos os projetos ao menos que esteja explicitado a sua não execução:

- Todos os recursos criados vão ter tags de verificação mesmo que nao esteja especificado na documentação Ex: "project":"gameday"; "owner":"brazil team";
  
- Sempre que houver aplicações web/apis no contexto do jogo e se falar as palavras "cache", deve-se utilizar Cloudfront, além disso caso tenham rotas expostas via ALB ou APIGW, considerar o CloudFront;
  
- Sempre que houver menção a proteção de apis contra ataques, deve-se utilizar o WAF;
  
- Sempre que tiver que utilizar um S3 no projeto, ele deve ter a seguinte características: configuração de ciclo de vida (definir movimentação de tiers), ativar o versionamento e o encryption, endpoint (vpc endpoint).
  
- Criar um vpc nova para cada projeto e ativar o vpc flow logs;
  
- no ECR, configuração da imutabilidade, lifecycle configuration (expire), resource policies, e endpoint (vpc endpoint)
  
- No ALB, sempre ligar o log;
  
- no RDS, sempre ativar a proteção de delação, parameter group proprio, snapshots e config logs
  
- GuardDuty e WAF relacionados a: "Ensure compliance with relevant regulations and maintain records of suspicious activities."
- Cloud-based = provavel serviço gerenciado (cloud-base batch processing system = AWS Batch)
  
- Se usar ECS fazer a config com Fargate, ativar Container Insights, task definition logging enabled "Consider computing services taht minimize infrastructure management"
  
- API Gateway: ativar logs e x-ray
  
- Analisar as roles pre existentes na doc, e avaliar serviços potencialmente relacionaveis
  
- caso haja "Point deductions" explicitamente na doc, tomar cuidado com os serviços
  
- DynamoDB: deletion protection, ttl, encryption, endpoint (vpc endpoint), tag e backup
  
- Security Groups: remover regras 0.0.0.0/0 e SSH.
  
  
- Kinesis: data streams com criptografia
  
- CloudWatch: menções a monitoramento, alerta, observabilidade. Criar Alertas, Dashboards, retention policy
  
- GuardDuty: Malware protection
  
- Macie - PII (sensitive data) in S3, storage

## Lembretes Rápidos:

### VPC

- Tag
- Flow Logs
  
### S3

- Tag
- Lifecycle
- Versionamento
- Criptografia
- VPC Endpoint

### DynamoDB

- Tag
- Deletion Protection
- Criptografia
- TTL
- Backup
- VPC Endpoint
- Analisar GSI

### RDS

- Tag
- Deletion Protection
- Parameter Group personalizado
- Snapshots/Backups
- Logs

### API Gateway

- Tag
- Logs
- X-Ray

### ECR

- Tag
- Imutabilidade
- Criptografia
- Lifecycle (expire)
- Scan on push
- Resource based policies
- VPC Endpoints

### EC2

#### Security Groups

- Remover regras 0.0.0.0/0

#### Load Balancers

- Logs export
