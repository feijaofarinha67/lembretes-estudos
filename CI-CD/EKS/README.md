# Pipelines para deployment no EKS

## kubectl

- Criar stage de deploy usando a opção kubectl
- Criar access entry para a role do CodePipeline no EKS cluster
- Selecionar o artefato
- Selecionar o namespace
- Especificar todos os arquivos a aplicar ex:
```
manifests/deploy.yaml,manifests/svc.yaml,manifests/lbconfig.yaml,manifests/tgconfig.yaml,manifests/gatewayclass.yaml,manifests/gateway.yaml,manifests/routes.yaml,manifests/deployapp2.yaml,manifests/svcapp2.yaml
```

## Helm

- Criar stage de deploy usando a opção Helm
- Passar nome desejado do release 
- Passar o diretório ex: `charts/my-app` sem `/` no final
- Para o helm funcionar devem ser criados novos recursos sempre a partir de um helm create
