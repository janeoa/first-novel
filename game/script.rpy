﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define a = Character('Asset', color="#c8ffc8")


# The game starts here.
label start:

    scene jpbg

    a "О! Привет Дениз!"

    show asset sprite

    a "Если ты видишь это сообщение, значит ты освоила git!"

    return
