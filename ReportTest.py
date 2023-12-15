from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import pdfencrypt
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker

# Funzione per calcolare l'area del triangolo
def calcola_area_triangolo(base, altezza):
    return 0.5 * base * altezza

# Funzione per creare il PDF
def crea_documento_pdf():
    # Crea un documento PDF
    c = canvas.Canvas("documento.pdf", pagesize=letter)

    # Aggiunge la formula dell'area del triangolo
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "Formula per calcolare l'area del triangolo:")
    c.drawString(100, 680, "Area = 1/2 * base * altezza")

    # Aggiunge un testo di una canzone
    c.setFont("Helvetica", 14)
    c.drawString(100, 650, "Testo della canzone:")
    c.drawString(100, 630, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    # Aggiunge un grafico 3D di un paraboloide
    d = Drawing(400, 200)
    paraboloide = LinePlot()
    paraboloide.x = 50
    paraboloide.y = 50
    paraboloide.width = 300
    paraboloide.height = 150
    paraboloide.data = [[(x, y, x ** 2 + y ** 2) for x in range(-10, 11)] for y in range(-10, 11)]
    paraboloide.lineLabelFormat = {'fillColor': colors.black,
                                   'fontName': 'Helvetica',
                                   'fontSize': 8,
                                   'labelSep': 0.01,
                                   'side': 'right'}
    # paraboloide.categoryAxis.categoryNames = range(-10, 11)
    # paraboloide.valueAxis.valueMin = -10 ** 2
    # paraboloide.valueAxis.valueMax = 10 ** 2
    # paraboloide.valueAxis.valueStep = 100
    paraboloide.lines[0].symbol = makeMarker('FilledCircle')
    d.add(paraboloide)
    renderPDF.draw(d, c, 100, 400)

    # Aggiunge un grafico con la sinusoide e descrizione degli assi
    d2 = Drawing(400, 200)
    sinusoide = LinePlot()
    sinusoide.x = 50
    sinusoide.y = 50
    sinusoide.width = 300
    sinusoide.height = 150
    sinusoide.data = [[(x, math.sin(x)) for x in range(-10, 11)]]
    sinusoide.lineLabelFormat = {'fillColor': colors.black,
                                 'fontName': 'Helvetica',
                                 'fontSize': 8,
                                 'labelSep': 0.01,
                                 'side': 'right'}
    # sinusoide.categoryAxis.categoryNames = range(-10, 11)
    # sinusoide.valueAxis.valueMin = -1
    # sinusoide.valueAxis.valueMax = 1
    # sinusoide.valueAxis.valueStep = 0.25
    sinusoide.lines[0].symbol = makeMarker('FilledCircle')
    d2.add(sinusoide)
    renderPDF.draw(d2, c, 100, 200)

    # Chiude il documento PDF
    c.showPage()
    c.save()

# Chiamata alla funzione per creare il documento PDF
crea_documento_pdf()