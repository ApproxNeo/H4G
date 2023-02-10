[[back](../Mattermost.md)]


# Mattermost Installation (Docker)
Install Mattermost via Docker
***

## Installing Docker (and Docker-Compose) 🐋
- Run the commands:  
`sudo apt update -y`  
`sudo apt install docker.io docker-compose -y`  
`sudo systemctl start docker`  
***

## Step 0: Preparation
- Make a folder for the installation  
`mkdir mattermost && cd mattermost`
***

## Step 1: Clone the repository  
- This repo contains the `docker-compose.yaml` files  
`git clone https://github.com/mattermost/docker && cd docker`
***

## Step 2: Set up the environment variables
- Make copy of example `.env` file  
`cp env.example .env`     
- Change the following line inside the `.env` file to the fully-qualified domain name for the Mattermost server
```
DOMAIN=mm.example.com
```
- Optionally edit the default Postgre Database username and password   
```
POSTGRES_USER=mmuser
POSTGRES_PASSWORD=mmuser_password 
```
- Also, substitude the ${placeholder} values in these 2 lines
```
MM_SQLSETTINGS_DATASOURCE=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}?sslmode=disable&connect_timeout=10

MM_SERVICESETTINGS_SITEURL=https://{DOMAIN}
```  
> this is a temporary fix, there may be an alternate configuration for `Docker-Compose` to automatically substitute these values

***

## Step 3: Create the required directories
`mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes} && sudo chown -R 2000:2000 ./volumes/app/mattermost`

***

## Step 4: Configure TLS for Nginx

- This steps sets up the configs for a reverse proxy providing public access to the Mattermost server
> This uses `certbot` to automatically register a HTTPS certificate with LetsEncrypt. You can also opt to do this step manually at [certbot's website](https://certbot.eff.org/)

- Create new Cert/Key pair with the provided script. 
`bash scripts/issue-certificate.sh -d <YOUR_MM_DOMAIN> -o ${PWD}/certs`  

> The `issue-certificate.sh` script is found in the Docker folder 

- Uncomment the following lines in the `.env` file

```
#CERT_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/fullchain.pem
#KEY_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/privkey.pem
```

***
## Step 4: Deployment

To deploy (with Nginx):  
`sudo docker-compose -f docker-compose.yml -f docker-compose.with-nginx.yml up -d`

To deploy (without Nginx):  
`sudo docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d`

To take down:  
`sudo docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml down`

***

## Step 5: Configure Mattermost
- Execute into the Mattermost Container  
`sudo docker exec -it <container-id> /bin/sh`
- `mmctl` is a custom Mattermost binary to have root access control over an instance of Mattermost. The Mattermost container comes with this binary built-in
- Run these commands  
`mmctl config set ServiceSettings.EnableAPIUserDeletion true`  
    > by default, Mattermost does not allow for deletion of user accounts. This configuration allows for deletion through API calls

[[back](../Mattermost.md)]
