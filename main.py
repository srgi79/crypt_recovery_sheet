
from reportlab.pdfgen import canvas
#from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, Color
from reportlab.lib.pagesizes import A4
import json

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile) # Reading the file
    jsonfile.close()
    wallet = config[0]

def append_text_box(text_list, initY, deltaY):
    # INIT
    X = 20
    Y = initY
    i = 1
    boxPerRow = 6
    width = 60

    while i <= len(text_list):
        #print('i', i)
        c.drawString(X, Y+2/3*font_box_size, '[' + str(i) + ']')
        form.textfield(value=phrase[i-1], name=str(i), tooltip=str(i), x=X+25, y=Y, width=width, height=font_box_size*2, borderStyle='underlined', borderWidth=0, fillColor=color)
        lastY = Y

        if i % boxPerRow == 0:
            Y -= deltaY
            X = 20
        else:
            X += width + 30
        
        i += 1
    
    c.setFont("Courier", font_box_size)
    c.drawString(20, lastY-10, address)
    return lastY-10

pagesize = A4
title = wallet['pdf_title']
filename = wallet['filename'] + '.pdf'
c = canvas.Canvas(filename, pagesize=pagesize)
c.setTitle(filename)

# DIMENSIONS
font_title_size = 20
font_box_size = 8
color = Color(100, 100, 100, alpha=0)

startTitle = pagesize[1]-font_title_size-10
startWallet = pagesize[1]-50

for wallet in config:

    # PARAMETERS
    phrase = wallet['words']
    address = wallet['address']

    # HEADER
    c.setFont("Courier", font_title_size)
    c.drawCentredString(pagesize[0]/2, startTitle, title)
    c.setFont("Courier", font_box_size)
    form = c.acroForm

    lastY = append_text_box(phrase, startWallet, font_box_size*3)

    startTitle = lastY-30
    startWallet = startTitle - 20


c.save()

