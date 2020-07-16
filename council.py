import csv
from PIL import Image, ImageDraw
from PIL import ImageFont

filename = "council.csv"
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

for row in rows:
    bibno = row[0]
    name = row[1]
    category = row[2]
    print (name, bibno, category)

    image = Image.open("Council.png")
    draw = ImageDraw.Draw(image)

    name_font = ImageFont.truetype("./gabriola.ttf", 220)
    category_font = ImageFont.truetype("./gabriola.ttf", 125)
    bib_font = ImageFont.truetype("./arial.ttf", 50)
    url_font = ImageFont.truetype("./gabriola.ttf", 65)

    name_color = (187, 72, 142)
    wname, hname = draw.textsize(name, font=name_font)
    name_coordinates = (1525 - wname / 2, 1160)
    draw.text(name_coordinates, name, name_color, font=name_font, spacing=200, stroke_width=3)

    category_color = (0, 0, 0)
    wcat, hcat = draw.textsize(category, font=category_font)
    category_coordinates = (1680, 1395)
    draw.text(category_coordinates, category, category_color, font=category_font, spacing=1, stroke_width=1)

    bib_color = (0, 0, 0)
    bib_coordinates = (110 , 2375)
    draw.text(bib_coordinates, "Certificate ID - ", bib_color, font=url_font, stroke_width=0)

    bib_coordinates = (415 , 2370)
    draw.text(bib_coordinates, bibno, bib_color, font=bib_font, stroke_width=0)

    url = "https://gymkhana.iitb.ac.in/~hostel2/" + bibno + ".pdf"
    url_color = (255, 255, 255)
    wurl, hurl = draw.textsize(url, font=url_font)
    url_coordinates = (110 , 2500)
    draw.text(url_coordinates, url, url_color, font=url_font, stroke_width=0)

    image.save(bibno+".png", "PNG")