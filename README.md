# modularDSM
MSc. Dissertation project 

# MUJOCO is such a pain in the ass to install that there is a file just for it!

# Simulation turned out to be a pain in the ass:

# Project Chrono: (OS + No flexible bodies unless C++ (dubious even there))
I may as well surrender and use Chrono, use rigid bodies and try to "emulate" the softness of the actuators through some function.

## The best contender seems to be: PositionBasedDynamics AAAAAAAAAAAAAAND is C++!
https://github.com/InteractiveComputerGraphics/PositionBasedDynamics

Is a for debian so Im going to drop this below...

Perhaps the best way forward would be to model the "soft" elements here and use the results to build a model for  them.


### How to Install deb Packages on Ubuntu Linux
There are many ways you can install deb packages. Among them, the below list is the best and easy way to follow.

Simply download the program, and clicking on it
Using gdebi
dpkg – Debian Package Management System
apt to install packages