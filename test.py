import impin
import impin_plots

canvas = impin.canvas(layernames=("Impact", "Outcomes", "Results", "Activities", "Conditions"), title="Testplot")

b1 = canvas.add_box("Impact",     "Goede cijfers halen")
b2 = canvas.add_box("Outcomes", "Stof snappen")
b3 = canvas.add_box("Results",   "Opletten")
b4 = canvas.add_box("Results",   "Goed uitleggen")
b5 = canvas.add_box("Activities",   "Naast de juf zitten")

canvas.add_relationship(b2, b1)
canvas.add_relationship(b3, b2)
canvas.add_relationship(b4, b2)
canvas.add_relationship(b5, b4)


textplot = impin_plots.text_impactplot()
canvas.plot(textplot)

graphicalplot = impin_plots.pygame_impactplot(1080, 768)
canvas.plot(graphicalplot)

while True:
    pass