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

-------

### What does picker model file contains?
Pickle is used for serializing and de-serializing Python object structures, also called marshalling or flattening.

Pickling is useful for applications where you need some degree of persistency in your data. Your program's state data can be saved to disk, so you can continue working on it later on. It can also be used to send data over a Transmission Control Protocol (TCP) or socket connection, or to store python objects in a database.

## When Not To Use pickle
If you want to use data across different programming languages, pickle is not recommended. Its protocol is specific to Python, 