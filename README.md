# P3 MacGyver project

"MacGyver - [get out]" is little game made with python and pygame.
It's a simple basic level where the goal is to help MacGyver to exit
with the collect of those tools : a ether bottle, a needle and a little tube  
to make a syringe and make asleep the gatekeeper.

This project is my first contribution to Openclassroms on the context
of learning code with that formation : "developpeur d'application - python".

For the first constraint, we had to show how to make the level structure :

```.WWWWWW..W.WWW.
        .W..W..
WWW W W WWW.W.W
W...W W       .
..WWW W.WWW  W.
W.... WWW.W. W.
W.WW    W.WW W.
W.W. WW W    WW
s..  ......W.W.
WWW .WW.WW WWW.
W.W WWW        
W.....W.W.W.WW 
W.WWW.WWW.W.W  
....W.....W.W W
WWW.W.WWW.W.W f```

## The MVC pattern

* Model, responsible for managing the data of the application.
* View, presentation of the model in a particular format.
* Controller, responds to the user input and performs interactions on the data model objects.

The application offers the choice of two versions :

* terminal version
* pygame version

With only one entry point to make this application modular.

To do that, my approch was to do a txt file with some
characters to mark the position of each image. Then, in loop 
it was simple to generate each possition under the form of coordinates.

For the second constraint, we had to use the pygame module to generate
that level with the images of player and gatekeeper. Only the player can move
and the goal here is to move MacGyver to the exit and asleep the gatekeeper.
