import impin
import impin_pygameplot
import impin_textplot
import impin_powerpointplot

canvas = impin.canvas(layernames=("Impact", "Outcomes", "Results", "Activities"), title="Testplot")

b1 = canvas.add_box("Impact",     "Het gaat goed")
b2 = canvas.add_box("Outcomes",   "Opdrachten op tijd afkrijgen")
b3 = canvas.add_box("Outcomes",   "Aandachtvermogen ontwikkelt zich")
b4 = canvas.add_box("Activities", "Thuis half uur op één ding concentreren")
b5 = canvas.add_box("Activities", "Weekplanning in de klas maken")
b6 = canvas.add_box("Activities", "Nog iets")

canvas.add_relationship(b2, b1)
canvas.add_relationship(b3, b2)
canvas.add_relationship(b4, b2)
canvas.add_relationship(b5, b4)


textplot = impin_textplot.textplot()
canvas.plot(textplot)

#graphicalplot = impin_pygameplot.pygameplot(1080, 768)
#canvas.plot(graphicalplot)

ppplot = impin_powerpointplot.powerpointplot()
canvas.plot(ppplot)

#while True:
#    pass