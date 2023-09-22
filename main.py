
from reportlab.pdfgen import canvas
#from reportlab.pdfbase import pdfform
#from reportlab.lib.colors import magenta, pink, blue, green
from reportlab.lib.pagesizes import A4
from configparser import ConfigParser

# PARAMETERS
config = ConfigParser()
config.read('config.ini')
phrase = config.get('PHRASE', 'WORDS')
title = config.get('FILE', 'TITLE')
filename = config.get('FILE', 'NAME') + '_' + str(len(phrase)) + 'W.pdf'

# DIMENSIONS
pagesize = A4
font_title_size = 20
font_box_size = 8

# HEADER
c = canvas.Canvas(filename, pagesize=pagesize)
c.setTitle(filename)
c.setFont("Courier", font_title_size)
c.drawCentredString(pagesize[0]/2, pagesize[1]-font_title_size, title)
c.setFont("Courier", font_box_size)
form = c.acroForm


def append_text_box(text_list, initY, deltaY):
    # INIT
    X = 40
    Y = initY
    i = 1
    boxPerRow = 6
    width = 50

    while i <= len(text_list):
        #print('i', i)
        c.drawString(X, Y+2/3*font_box_size, '[' + str(i) + ']')
        form.textfield(value=phrase[i-1], name=str(i), tooltip=str(i), x=X+25, y=Y, width=width, height=font_box_size*2, borderStyle='inset', forceBorder=True)

        if i % boxPerRow == 0:
            Y -= deltaY
            X = 40
        else:
            X += width + 30
        
        i += 1
    c.save()

if __name__ == '__main__':
    append_text_box(phrase, pagesize[1]-50, font_box_size*3)