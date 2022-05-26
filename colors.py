## Joseph Melancon
## joseph@jmelancon.com
## 2022

def colortext(text, textColor = "green", backgroundColor = "black", style = "n"):
    colorDict = {
        "black":"0",
        "red":"1",
        "green":"2",
        "yellow":"3",
        "blue":"4",
        "purple":"5",
        "cyan":"6",
        "white":"7"
    }
    styleDict = {
        "n":"0",
        "b":"1",
        "i":"3",
        "u":"4",
    }
    return ("\033[{};{};{}m{}\033[0m".format(styleDict[style], "3" + colorDict[textColor], "4" + colorDict[backgroundColor], text))