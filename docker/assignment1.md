# Docker and Docker Hub

## Task 1:

### Dockers basic commands

```
1. docker -v : checking the version of dockers.
```
<img width="338" alt="1 version" src="https://user-images.githubusercontent.com/28885876/195696172-e81b9c9f-2fc3-4147-a0c2-d8334a0e8d51.png">

```
2. docker pull <image name>:
pull an image or repository from the registry.
```
<img width="593" alt="2 pull" src="https://user-images.githubusercontent.com/28885876/195696177-497ce025-1bb9-40ee-8277-4a5ac40239aa.png">

```
3. docker images :
lists all the docker images pulled in the local system.
```
<img width="697" alt="3 images" src="https://user-images.githubusercontent.com/28885876/195696183-bab97a6c-af06-4c54-8d76-4786388dabc1.png">

```
4. docker run -d -p containerport:host port <image name> :
This command runs a new docker container in detach(background)
```
<img width="557" alt="4 run" src="https://user-images.githubusercontent.com/28885876/195696188-82b1d610-9a96-4def-9ac3-17f97b36791b.png">

```
5. docker ps :
list the running containers.
```
<img width="968" alt="5 ps" src="https://user-images.githubusercontent.com/28885876/195696521-6fba85d1-5f49-4aba-b6d2-adf42ba73baa.png">

```
6. docker stop container id:
To stop the container which is running.
```
<img width="536" alt="6 stop" src="https://user-images.githubusercontent.com/28885876/195696557-86033001-e5df-4422-950d-e3c6337acae5.png">

```
7. docker image rm image id:
This command removes the specified images with respect to the mentioned by image id.
```
<img width="850" alt="7 rm image" src="https://user-images.githubusercontent.com/28885876/195696584-556b05e7-f6ca-4ec9-9073-82d02176be18.png">

```
8. docker network ls :
list all the network the daemon knows about.
```
<img width="408" alt="8 network" src="https://user-images.githubusercontent.com/28885876/195696609-97e01832-da79-4bb4-91e1-95821f883537.png">

```
9. docker container logs <container id >:
Lists the logs of the specified container .
```
<img width="914" alt="9 logs" src="https://user-images.githubusercontent.com/28885876/195696739-e8ce6a84-3f9e-4fb5-a8c6-f5955e4545e8.png">

```
10. docker build -t <image name> . :
Builds a docker image from the specified docker file.
```
<img width="985" alt="10 build" src="https://user-images.githubusercontent.com/28885876/196200105-a5dd537b-12dd-4d0c-b973-5dfa746dec9a.png">

```
11.docker login :
This command helps in login in to the docker hub registry where we can push or pull the docker images .
```
<img width="436" alt="11 login" src="https://user-images.githubusercontent.com/28885876/195696784-f904d0e1-8d02-4321-a4de-22c6903436d5.png">

```
12. docker kill <container id>:
It kiils the container by stopping its execution immediately .
```
<img width="530" alt="12 kill" src="https://user-images.githubusercontent.com/28885876/195696792-26dcbe91-4a2a-40dc-ae49-c2c56cad4f31.png">

```
13. docker commit <container id> <new image name> :
This command creates new image from the existing changes made in the container.
```
<img width="596" alt="13 comit" src="https://user-images.githubusercontent.com/28885876/195696795-09584d4a-2be4-4896-9af5-634a96bc6fa5.png">

```
14. docker export --output="newdockerfile" <container id> :
It saves the docker image specified in the local system as a tar file .
```
<img width="628" alt="14 export" src="https://user-images.githubusercontent.com/28885876/195696796-3d384716-3847-41c0-ab53-55aa903a0a44.png">

```
15. docker import <full path>:
This command imports the docker image from the local system
```
<img width="641" alt="15 import" src="https://user-images.githubusercontent.com/28885876/195696798-7ff73a4e-8b38-4636-8e42-3b34859fe5f0.png">
