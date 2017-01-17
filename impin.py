IMPACT = 0
OUTCOMES = 1
RESULTS = 2
ACTIVITIES = 3

class canvas:
    """The area is where the impactplot is drawn."""
    LEFT = 0
    RIGHT = 1
    CENTER = 2

    def __init__(self, width=1080, height=768):
        # Variables for making the canvas tick
        self.title = "Empty"
        self.layer = {IMPACT: list(),
                      OUTCOMES: list(),
                      RESULTS: list(),
                      ACTIVITIES: list()}
        self.relationships = list()
        self.counter = 0

        # Layout variables for the canvas
        self.bg_color = "00000000"
        self.bg_picture = None
        self.width = width
        self.height = height
        self.lane_padding = 0.25
        self.title_font = None
        self.title_font_size = 24


        # Layout variables for the boxes
        self.box_font = None
        self.box_font_size = 18
        self.box_height = self.height/(8*self.lane_padding+4)
        self.box_width = 100
        self.box_justify = canvas.LEFT

    def describe(self):
        """This function describes in text what the area should look like. It's a placeholder until graphics are
        added."""
        print("These are the boxes to be drawn on the canvas:")
        for l in self.layer:
            print("Level",l)
            for b in self.layer[l]:
                print(" - %s (Id %s)" % (b.title, b.id))
        print("These are the relationships to be drawn on the canvas:")
        for r in self.relationships:
            print(" - %s connects to %s" % (r.from_box.title, r.to_box.title))

    def import_from_file(self):
        pass

    def __add(self, thing, layer = None):
        if type(thing) == box:
            if layer in range(len(self.layer.keys())):
                self.layer[layer].append(thing)
                self.counter += 1
                thing.set_id(self.counter)
        elif type(thing) == relationship:
            self.relationships.append(thing)
        self.plot()

    def add_box(self, layer, title, text=""):
        b = box(title, text)
        self.__add(b, layer)

    def add_relationship(self, from_box, to_box):
        r = relationship(from_box, to_box)
        self.__add(r)

    def delete_box_by_id(self, idno):
        for l in self.layer:
            for n, b in enumerate(self.layer[l]):
                if b.id == idno:
                    del self.layer[l][n]
        for n, r in enumerate(self.relationships):
            if (r.from_box.id == idno) or (r.to_box.id == idno):
                del self.relationships[n]

    def delete_relationship(self, idno):
        for n, r in enumerate(self.relationships):
            if r.id == idno:
                del self.relationships[n]

    def get_box_by_id(self, idno):
        for l in self.layer:
            for b in self.layer[l]:
                if b.id == idno:
                    return b

    def plot(self):
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

    def add_text(self, text):
        self.text = text

    def get_location(self):
        pass

    def delete_me(self, from_canvas):
        from_canvas.delete_box_by_id(self.id)

class relationship:
    """These objects are the relationships between boxes."""
    def __init__(self, from_box, to_box):
        self.from_box = from_box
        self.to_box = to_box
        self.id = None

    def draw(self):
        start = self.from_box.get_location()
        end = self.to_box.get_location()