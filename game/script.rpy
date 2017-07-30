# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define a = Character('Asset', color="#c8ffc8")
define d = Character('Deniz', color="#c8ffc8")



# The game starts here.
label start:

menu:
    "играть за Асета":
        jump denizzz

    "play as Vriska":
        jump Sburb

label denizzz:

    scene jpbg

    a "О! Привет Дениз!"

    show asset sprite

    a "Если ты видишь это сообщение, значит ты освоила git!"

    show deniz2

    show deniz2 at right

    show asset sprite at left

    d "О, Асет!"

menu:

    "Спросить у нее как дела":
        jump feels

    "Спросить у нее о погоде":
        jump weather

label feels:

    a "ты как?"

    jump continuee

label weather:

    a "Чет холодно в Астане"

    jump continuee



    return
