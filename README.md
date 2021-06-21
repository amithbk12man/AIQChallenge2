## Problem Statement:

Attached is a csv file which contains image data referenced by the column depth. The rest of columns
(200) represent image pixel values from 0 to 255 at each depth.
The challenge consists of the following requirements:
· The image size is relatively big. Hence, there is a need to resize the image width to 150 instead of
200.
· The resized image has to be stored in a database.
· An API is required to request image frames based on depth_min and depth_max.
· Apply a custom color map to the generated frames.
· The solution should be based on Python.
· Bonus: deployment of the solution in a cloud service.



## Image Service

Current implementation is a basic approch to solve problem statment. This will provide an API to resize and get the image in given frame size.
Frame size is determined by

 - Python 3.8(flask, pandas, OpenCV, Pillow)
 - Docker
 - Docker Compose

## Assumptions:
1. We are considering top plants on basis of net generation of power plants they have
2. Federal State percentage for plant is calculated on basis of net generation of power plants for that state

### Run Applications

```bash
-- Using Docker Compose:
Requirements:
 1. need to install Docker and Docker-compose and run
 2. docker-compose up
```
```bash
-- Using IDE/Command Line
Requirements:
 1. need to install python3.8, pip
 2. pip3 install -r requirements.txt
 3. python3.8 server.py
```

### Test APIs
```bash
//Fetch image dataframe
curl -X GET http://0.0.0.0:9090/getFrame?depth_min=1&depth_max=5000&cmap=gray

Sample Response:
![image](https://user-images.githubusercontent.com/10739723/122793278-0ee54580-d2cc-11eb-8e98-2b8bc5f30739.png)

```

### Features which could have been done:
- A database or Block store could be used or mounted in docker rather than local file system. 
- Need to add proper error handling
- Need to add proper logs mechanism
- Need to add the unit and integration testings
- Need to add automatic checks for enforcing code quality
- Need to add CI/CD plugin for automatic deployment through docker
