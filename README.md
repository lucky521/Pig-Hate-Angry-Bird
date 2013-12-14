AngryBirdGame
=============

This is a Flying Game about AngryBird.



This game is writtern by Python base on Pyglet.
To learn more about Pyglet, you can refer to http://www.pyglet.org/




The source code structure:


.
|- luckybird.py   the main proceture
|- game

     |- __init__.py   modules used by luckybird.py
     |- config.py     configure file, global constant
     |- resources.py    import resources
     |- util.py     util functions
     |- player.py   Player class is about the player himself, derived from PhysicalObject
     |- angrybird.py    AngryBird class is about the enemy, derived from PhysicalObject
     |- egg.py      Egg class is about the score, derived from PhysicalObject
     |- physicalobject.py   Base class, moving things
     |- load.py   instantiate and load all objects
     
     
