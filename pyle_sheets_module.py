import logging
__author__ = 'Mike', 'Intuitive Design'


def compyle(title, style_sheet, variables, boolean=False, boolean2=True):
    """
    :param title: The name you wish your .css file to be named.
    :param style_sheet: The name of the multi-line string that will compose your .css file
    :param variables: The name of the dictionary containing your .pcss variables
    :param boolean: A.K.A the "Compiler Parameter" - Turns the compiler on or off
    :param boolean2: A.K.A the "Annotation Parameter" - Turns annotations on or off
    :return: returns compiled .pcss text as normal .css style text to be utilized with .html
    """
    # -----------------------------------
    file_name = title + ".css"
    replace_num = len(variables.keys())
    counter = replace_num
    content = style_sheet
    # -----------------------------------
    # add theme support with namedtuple's formatted to mimic structs in C/C++
    # this will be a major feature update as well as a nice way to allow the future prospect of integrating C/C++ into
    # the compiler. Info: https://stackoverflow.com/questions/35988/c-like-structures-in-python
    for k, v in variables.items():
        counter -= 1
        content = content.replace(k, v, replace_num)
        if counter == 0:
            break
        else:
            pass
    looped_content = str(content)
    id_content = looped_content.replace("hash_", "#")
    output = id_content.replace("dot_", ".")

    if boolean is True:
        if boolean2 is True:
            output = " /* --- Pyle Sheet --- */\n" + output
            with open(file_name, 'w') as writ:
                writ.write(output)
                writ.close()
                print('compiled successfully; The file was saved as ' + "\"" + file_name + "\".")
        elif boolean2 is False:
            pass
        else:
            logging.warning("An Error Occurred - see module, documentation, or online Q&A for assistance.")
    elif boolean is False:
        if boolean2 is True:
            print('compiled successfully; The file ' + "\"" + file_name + "\"" + "was not saved/created.")
        elif boolean2 is False:
            pass
        else:
            logging.warning("An Error Occurred - see module, documentation, or online Q&A for assistance.")
    else:
        logging.warning('An Error Occurred with the Compile Parameter (See: boolean in pyle_sheets source file) - \ '
                        'see module, documentation, or online Q&A for assistance.')


def changeValue(x, y, var):
    try:
        var[x] = var[x].replace(var[x], y)
        # return x
        # should this return value stay? It works without it...
    except Exception:
        logging.warning("""function call of changeValue did not work.\nAn Error Occurred - see module, \
documentation, or online Q&A for assistance.""")


def getSheet(file, mode="r"):
    """First parameter is the file you wish to read, """
    with open(file, mode) as file:
        string = file.read()
        file.close()
    return string
