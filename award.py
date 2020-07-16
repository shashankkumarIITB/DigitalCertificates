import csv
from PIL import Image, ImageDraw
from PIL import ImageFont

filename = "award.csv"
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

    image = Image.open("Award.png")
    draw = ImageDraw.Draw(image)

    name_font = ImageFont.truetype("./gabriola.ttf", 105)
    category_font = ImageFont.truetype("./gabriola.ttf", 100)
    bib_font = ImageFont.truetype("./arial.ttf", 26)

    name_color = (207, 139, 72)
    wname, hname = draw.textsize(name, font=name_font)
    name_coordinates = (970 - wname / 2, 620)
    draw.text(name_coordinates, name, name_color, font=name_font, stroke_width=0)

    category_color = (56, 83, 124)
    wcat, hcat = draw.textsize(category, font=category_font)
    category_coordinates = (1470 - wcat, 370)
    draw.text(category_coordinates, category, category_color, font=category_font, stroke_width=0)

    bib_color = (255, 255, 255)
    bib_coordinates = (40 , 1087)
    draw.text(bib_coordinates, "Certificate ID - " + bibno, bib_color, font=bib_font, stroke_width=0)

    url = "https://gymkhana.iitb.ac.in/~hostel2/" + bibno + ".pdf"
    wurl, hurl = draw.textsize(url, font=bib_font)
    url_coordinates = (40 , 1125)
    draw.text(url_coordinates, url, bib_color, font=bib_font, stroke_width=0)

    image.save(bibno+".png", "PNG")