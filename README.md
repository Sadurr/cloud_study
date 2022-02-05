# Azure application

## Creating vm - azure cli:

```
az group create --name wsb_group --location eastus

az vm create \
  --location eastus \
  --resource-group wsb_group \
  --name wsb_vm \
  --size Standard_B1ls  \
  --image Win2019Datacenter \
  --public-ip-sku Standard \
  --admin-username filip_sadurski \
  --admin-password AzurePa$$w0rd
```

## Creating database - azure cli:

```
az mysql server create --resource-group wsb_group --name sadurskidatabase --location eastus --admin-user filip_sadurski --admin-password AzurePa$$w0rd --sku-name GP_Gen5_2
```

## Creating container registry

### azure cli:
```
az group create --name wsb_group --location eastus
az acr create --resource-group wsb_group \
  --name wsbregistry --sku Basic
az acr login --name wsbregistry
```
### vscode:
```
docker login wsbregistry.azurecr.io
```
Building docker image: 'wsbregistry.azurecr.io/cloud_study:latest'

Push container to Azure App Service

(right cick on image) -> Deploy image to Azure App Service

Create New App service Plan:

    wsbplan
    wsbwebapp
