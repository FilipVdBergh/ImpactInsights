import impin
import impin_plots

canvas = impin.canvas(layernames=("Impact", "Outcomes", "Results", "Activities"), title="Testplot")

b1 = canvas.add_box("Impact",     "")
b2 = canvas.add_box("Outcomes",   "Opdrachten op tijd afkrijgen")
b3 = canvas.add_box("Outcomes",   "Aandachtvermogen ontwikkelt zich")
b4 = canvas.add_box("Activities", "Thuis half uur op één ding concentreren")
b5 = canvas.add_box("Activities", "Weekplanning in de klas maken")
b6 = canvas.add_box("Activities", "")

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