## Joseph Melancon
## joseph@jmelancon.com
## 2022

import colors
import statusbar
import os

def main():
    ## INTRO
    print(colors.colortext("The following output is a test of my modules.\n","yellow"))

    ## COLORS TEST
    print(colors.colortext("COLORS", "purple", style="b"))
    
    # Define what colors we want to use in a list. See colors.py
    colorsToTest = ["red", "yellow", "green", "cyan", "blue", "purple", "white", "black"]
    
    # Define variables to hold color test strings.
    colorTestString = ""
    intenseColorTestString = ""
    backgroundTestString = ""
    intenseBackgroundTestString = ""

    # Use a while loop to make things easier
    i = int(0)
    while i < len(colorsToTest):
        # Get low and high intensity text colors
        colorTestString += colors.colortext("███",colorsToTest[i])
        intenseColorTestString += colors.colortext("███",colorsToTest[i], highIntensityText = True)

        # Get low and high intensity background colors
        backgroundTestString += colors.colortext("   ", "white", colorsToTest[i])
        intenseBackgroundTestString += colors.colortext("   ","white", colorsToTest[i], highIntensityBG = True)

        # Increment loop
        i+=1
    
    # Output color-processed text (ugly lol)
    print(colors.colortext("text colors (normal):  ", "green") + colorTestString)
    print(colors.colortext("text colors (intense): ", "green") + intenseColorTestString)
    print()
    print(colors.colortext("bg colors (normal):    ", "green") + backgroundTestString)
    print(colors.colortext("bg colors (intense):   ", "green") + intenseBackgroundTestString)
    print()
    print(colors.colortext("wow, cool colors!\n", "yellow", highIntensityText = True))

    ## STATUSBAR TEST
    print(colors.colortext("STATUSBAR", "purple", style="b"))
    print(colors.colortext(statusbar.getbar(.6541), "cyan"))

    ## EXIT
    print(colors.colortext("\nGOODBYE!", "purple", style="b"))


if __name__ == "__main__":
    main()