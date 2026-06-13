# lembretes-estudos

Lyon:

day1:

Cost Optimization 5
"infrastructure deployment size"?

Operational Excellence 6.5
app main works 0.5
app stub works 0.5
auto scaling *importante

Security 4
public access to db or cache 2pts
least privilege in policies 2pts

Reliability 10
load tests, requisitos de rede
"subnet failure?"

Performance Efficiency 7.5
app response time

grande parte dos pontos eram realmente relacionadas a resposta da aplicação em si



## Itens

Todos os itens a seguir devem ser realizados em todos os projetos ao menos que esteja explicitado a sua não execução:
- Todos os recursos criados vão ter tags de verificação mesmo que nao esteja especificado na documentação Ex: "project":"gameday"; "owner":"brazil team";
- Sempre que houver aplicações web/apis no contexto do jogo e se falar as palavras "cache", deve-se utilizar Cloudfront;
- Sempre que houver menção a proteção de apis contra ataques, deve-se utilizar o WAF;
- Sempre que tiver que utilizar um S3 no projeto, ele deve ter a seguinte características: configuração de ciclo de vida (definir movimentação de tiers), ativar o versionamento e o encryption, endpoint (vpc endpoint).
- Criar um vpc nova para cada projeto e ativar o vpc flow logs;
- no ECR, configuração da imutabilidade, lifecycle configuration (expire), resource policies, e endpoint (vpc endpoint)
- No ALB, sempre ligar o log;
- no RDS, sempre ativar a proteção de delação, parameter group proprio, snapshots
- Cloud-based = provavel serviço gerenciado (cloud-base batch processing system = AWS Batch)
- Se usar ECS fazer a config com Fargate
- Analisar as roles pre existentes na doc, e avaliar serviços potencialmente relacionaveis
- caso haja "Point deductions" explicitamente na doc, tomar cuidado com os serviços
- DynamoDB: deletion protection, ttl, encryption, tag e backup
