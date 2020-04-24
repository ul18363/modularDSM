# Using Mujoco: (Paid + No liquids)
Mujoco is a widely used physics simulator used in bizillions of projects. However is not free for academic or commercial purposes, the student license only suits personal projects.
The cost of a license is around 500 dollars.
## Optional steps in case of trouble
apt install gcc
apt-get install patchelf
apt-get install libglu1-mesa-dev mesa-common-dev
## Instalation command 

pip install mujoco_py==2.0.2.8
Other versions don't work! (See https://github.com/openai/mujoco-py/issues/492 ) 20/04/2020



## Get computer ID:
Download computer ID generator for linux from: https://www.roboti.us/getid/getid_linux
Once downloaded the file
1.Open a terminal in the download folder
2. Run chmod +x getid_linux
3. Run ./getid_linux -> Obtain the computer id.

## MUJOCO Student licence:
After requesting a free student licence from MuJoCo can be obtained by soliciting at: https://www.roboti.us/license.html

Go back to https://www.roboti.us/license.html with both the license and the computer ID and register your computer. An email with an attachment called mjkey.txt should get to you and you should copy this file into the bin subdirectory to make use of the software. By using:
    sudo cp mjkey.txt /bin/

## Installation

    For some reason only installing the python library isnt enough. After downloading the Mujoco from https://www.roboti.us/ use the following commands 
     mkdir  ~/.mujoco 
     mkdir  ~/.mujoco/mujoco200
     unzip mujoco200_linux.zip  -d ~/.mujoco/mujoco200


## Usage 
MuJoCo uses the following environment variable to know were the binaries of MuJoCo are:
import os
os.environ['LD_LIBRARY_PATH']='/home/bruno/.mujoco/mujoco200/bin'

# More Bugs on MuJoCo

command 'gcc' failed with exit status 1 - > It seems that it has something to do with "developer headers" no idea what they are

Should be fixed by using "pip install python-dev-tools"


Tried to : 
- pip install python-dev-tools
- pip install -r requirements.txt
- pip install -r requirements.dev.txt
- sudo apt-get install libosmesa6-dev



Contrary what the installation guide says put the key in the "bin directory" in my case:
 - ~/.mujoco/mjpro/bin/mjkey.txt
 - /home/bruno/.mujoco/mjkey.txt


## OK Almost had it working:

-- Set the environment variables needed, one can either set it up from the console from python or to make it more automatic pre-load it in the terminal by adding the next 2 lines to the file home/.bashrc
1. Install Mujoco:
git clone https://github.com/openai/mujoco-py
cd mujoco-py
pip install -e . --no-cache

or [pip install mujoco_py]

[Perhaps install dependencies]

export LD_LIBRARY_PATH=$HOME/.mujoco/mujoco200/bin
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so

The first line make visible the mujoco files.
The second line makes available visualization OpenGL files to mujoco.

For some reason running spyder on its own doesn't load MuJoCo.
To make it work:
1. Go to a Terminal
2. Activate environment 
3. Open spyder from the environment 