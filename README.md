# greenr 🍃
A web app to tell whether your image is a dandelion or grass.

Adds more swap space if required
```
sudo bash swap.sh
```

```
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
Adds docker official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Adds stable repo
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
Install docker and docker-compose
```
sudo apt-get install docker docker-compose
```
Build docker image
```
sudo docker image build -t app:latest .
```
Run 
```
sudo docker run -d -p 80:8008 app:latest
```