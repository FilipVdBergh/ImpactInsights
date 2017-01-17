import impin

canvas = impin.canvas()
for i in range(2):
    canvas.add_box(impin.IMPACT, "Box no %s" % (i+1))
for i in range(4):
    canvas.add_box(impin.ACTIVITIES, "Box no %s" % i)

canvas.add_relationship(canvas.get_box_by_id(6), canvas.get_box_by_id(2))

canvas.delete_box_by_id(3)

canvas.describe()