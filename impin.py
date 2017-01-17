IMPACT = 0
OUTCOMES = 1
RESULTS = 2
ACTIVITIES = 3

class area:
    """The area is where the impactplot is drawn."""
    def __init__(self, width=1080, height=768):
        self.title = "Empty"
        self.bg_color = "00000000"
        self.bg_picture = None
        self.width = width
        self.height = height
        self.title_font = None
        self.title_font_size = 24
        self.font = None
        self.font_size = 18
        self.layer = (list(), list(), list(), list())
        self.relationships = list()
        self.counter = 0

    def reorder(self):
        pass

    def redraw(self):
        pass

    def describe(self):
        """This function describes in text what the area should look like. It's a placeholder until graphics are added."""
        print("These are the boxes to be drawn:")
        for l in self.layer:
            for b in l:
                print(b.title, )
        for r in self.relationships:
            print("Box %s connects to %s" % (r.from_box.title, r.to_box.title))


    def get_number_of_boxes(self, layer = None):
        if layer is None:
            number_of_boxes = 0
            for l in self.layer:
                number_of_boxes += l.count()
            return number_of_boxes
        else:
            return self.layer[layer].count()


    def add_box(self, box, layer):
        if layer in range(3):
            self.layer[layer].append(box)
            self.counter += 1
            box.set_id(self.counter)
        self.redraw()

    def add_relationship(self, relationship):
        self.relationships.append(relationship)

    def delete_box(self, idno):
        pass

    def delete_relationship(self, idno):
        pass


class box:
    """"The boxes contain text and are connected to each other."""
    def __init__(self, title, text=""):
        self.title = title
        self.text = text
        self.id = None
        self.subgroup = None

    def set_id(self, idno):
        self.id = idno

    def get_id(self):
        return self.id

    def add_text(self, text):
        self.text = text

    def get_location(self):
        pass

class relationship:
    """These objects are the relationships between boxes."""
    def __init__(self, from_box, to_box):
        self.from_box = from_box
        self.to_box = to_box
        self.id = None

    def draw(self):
        start = self.from_box.get_location()
        end = self.to_box.get_location()