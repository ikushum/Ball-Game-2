import cx_Freeze 

cx_Freeze.setup(
    name="Ball Game",
    version="2.0",
    options = {'build_exe':{'packages':['pygame'],'include_files':["1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","collide.wav","fly.gif","fly.wav","high_score.wav","howToPlay.jpg","intro.jpg","jump.wav","Kevin MacLeod - Carefree.mp3","land.wav","obs1.gif","obs2.gif","sky.jpg","start.jpg","wall.jpg","wood.gif","wood2.gif"]}},
    description="This is the version 2.0 of Ball Game. Have a awesome gaming.",
    executables=[cx_Freeze.Executable("ball_game.py")]
    )
















    
