class textplot:
    def __init__(self):
        pass

    def plot(self, canvas):
        print(canvas.title.upper())
        print("These are the %s boxes to be drawn on the canvas:" % canvas.count_boxes())
        for l in canvas.layer:
            print("  Level", l, canvas.layernames[l])
            for b in canvas.layer[l]:
                print("    %s (Id %s)" % (b.title, b.id))
        print("These are the %s relationships to be drawn on the canvas:" % canvas.count_relationships())
        for r in canvas.relationships:
            print("    %s <connects to> %s" % (r.from_box.title, r.to_box.title))
