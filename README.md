# P3 MacGyver project

MacGyver - [Help him out]" is a little game made with python and pygame. This is a simple level where the goal is to help MacGyver out with the collection of these items: an ether bottle, a needle and a small tube to make a syringe and put the guardian to sleep.

This project is my first contribution to Openclassroms on the context of learning code with this training: "application developer - python".

This application is standalone, to use it you must follow these indications:
* by clicking on the green button "Code", get the link and
* git clone <link>
* create a virtual environment in which you must install the modules from the requirements.txt file

Note: Only if *termcolor* gives you a message about `bdist_wheel`, you must also install *wheel* in your virtual environment:
pip install wheel

First of all, we had to show how to make the level structure.

So in a simple .txt file:

* S for the starting position (if any),
* An empty space for the position of the paths,
* . for the possible random position of objects,
* X for the position of the walls,
* F for the goalkeeper position.

```
SXXXXXX..X.XXXS
        .X..X..
XXX X X XXX.X.X
X...X X       .
..XXX X.XXX  X.
X.... XXX.X. X.
X.XX    X.XX X.
X.X. XX X    XX
S..  ......X.X.
XXX .XX.XX XXX.
X.X XXX        
X.....X.X.X.XX 
X.XXX.XXX.X.X  
....X.....X.X X
XXX.X.XXX.X.X F
```

## The MVC pattern

* Model, responsible for managing the data of the application.
* View, presentation of the model in a particular format.
* Controller, responds to the user input and performs interactions on the data model objects.

The application offers the choice of two versions :

* terminal version
* pygame version

With a single entry point to choose which one.
