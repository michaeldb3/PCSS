from pyle_sheets_module import *


def varsfunc():
    font1 = "Harlow Solid"
    grey = '#454545'
    font2 = 'Mistral'
    font3 = 'Italic 35px Times New Roman'
    pnk = 'pink'
    grn = 'green'
    # this was my first step in making them mutable
    # globals().update(locals())
    return locals()
# ---------------
the_vars = varsfunc()

# compyle()'s name is a pun on the task it obviously completes. 'compyle()' is in charge of starting compilation. It
# takes a few parameters to get all the info it needs to process the style sheet.
# compyle(#title, #stylesheet, #variable list, #Compile On/Off, Optional:#Annotations On/Off(print status updates))
# For On/Off parameters; On = True, Off = False.
compyle("pyle_sheet", getSheet('readwrite.css'), the_vars, True)


class ReservedArea:
    # --------
    # --- This area is reserved for the original doc-string containing the style sheet that is in "readwrite.css".
    # --- It is simply here to serve as a visual aide so you do not have to click through multiple files to see an
    # --- example of how the "compyle()" function works.
    '''
    style =
    #one{
        font: Italic 70px font1;
        color: pnk;
    }
    #two{
        font: bold 40px font2;
        color: grn;
    }
    #three{
        font: font3;
    }
    .sample{
        text-align: center;
    }
    #bodyid{
        background: grey;
    }
    h1{
        font: bold 55px font1;
        color: grn
    }
    '''
    # --------
