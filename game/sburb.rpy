define Vriska = Character('Vriska', color="#007BA7")
define dave = Character('Dave', color="#FF0000")
image vriskaPNG = "vriskaPNG.png"
image vriskaPNG flip = im.Flip("vriskaPNG.png", vertical=True)

label Sburb:

    show vriskaPNG at left
    Vriska "It is kinda lonely here"

    show vriskaPNG at right

    Vriska "Oh, hi!"
return
