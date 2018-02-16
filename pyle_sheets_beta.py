author__ = 'Mike'

title = "pyle_style.css"
if title == "":
    title = "untitled.css"
else:
    pass
writ = open(title, 'w')

variables = {'font1': 'Harlow Solid',
             'grey': '#454545',
             'font2': 'Mistral',
             'font3': 'Italic 25px Times New Roman',
             'pnk': 'pink',
             'grn': 'green'}


def changeValue():
    variables['font1'] = variables['font1'].replace(variables['font1'], 'Broadway')


changeValue()


style_sheet = '''/* Pyle Sheets */
hashone{
    font: Italic 70px font1;
    color: pnk;
}
hashtwo{
    font: bold 40px font2;
    color: grn;
}
hashthree{
    font: font3;
}
dotsample{
    text-align: center;
}
hashbodyid{
    background: grey;
}
h1{
    font: bold 55px font1;
    color: grn;
}
'''

replace_num = len(variables.keys())
counter = replace_num
content = style_sheet
for k, v in variables.items():
    counter -= 1
    content = content.replace(k, v, replace_num)
    if counter == 0:
        break
    else:
        pass


looped_content = str(content)
id_content = looped_content.replace("hash", "#")
clss_idContent = id_content.replace("dot", ".")
#------------
print(clss_idContent, "\n", "___________________", "\n")
print('title: ', title)
print('# of variables & amount of replacements executed: ', replace_num)
print('variables: ', variables, "\n", "___________________")
writ.write(clss_idContent)
writ.close()