## Joseph Melancon
## joseph@jmelancon.com
## 2022

import shutil

def getbar(progress):
    termLength = int(str(shutil.get_terminal_size()).split("=")[1][:-7])
    formattedProgress = str('{0:.1f}'.format(progress * 100)).rjust(4, "0")
    stopAt = termLength * progress
    returnBar = "{}% (".format(formattedProgress)
    for number in range(int(termLength) - 8):
        if number < stopAt:
            returnBar += "▓"
        else:
            returnBar += "░"
    returnBar += ")"
    #return("progress: {}%; terminal size: {}.".format(progress * 100, termLength))
    return returnBar