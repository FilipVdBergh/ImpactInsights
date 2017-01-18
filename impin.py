class canvas:
    """The area is where the impactplot is drawn."""
    def __init__(self, layernames=(), title="Empty"):
        # Variables for making the canvas tick
        self.title = title
        self.layernames = layernames
        self.layer = {l: list() for l in range(len(layernames))}
        self.relationships = list()
        self.counter = 0

    def plot(self, impinplot_object):
        impinplot_object.plot(self)

    def import_from_file(self):
        pass

    def __add(self, thing, layer=None):
        if type(thing) == box:
            if layer in self.layernames:
                self.layer[self.layernames.index(layer)].append(thing)
                self.counter += 1
                thing.set_id(self.counter)
        elif type(thing) == relationship:
            self.relationships.append(thing)

    def add_box(self, layer, title, text=""):
        b = box(title, text)
        self.__add(b, layer)
        return b

    def add_relationship(self, from_box, to_box):
        r = relationship(from_box, to_box)
        self.__add(r)
        return r

    def delete_box(self, box):
        for l in self.layer:
            for n, b in enumerate(self.layer[l]):
                if b == box:
                    del self.layer[l][n]
        for n, r in enumerate(self.relationships):
            if (r.from_box == box) or (r.to_box == box):
                del self.relationships[n]

    def delete_relationship(self, relationship):
        """This is deprecated"""
        for n, r in enumerate(self.relationships):
            if r == relationship:
                del self.relationships[n]

    def get_box_by_id(self, idno):
        for l in self.layer:
            for b in self.layer[l]:
                if b.id == idno:
                    return b

    def get_box_by_title(self, title):
        for l in self.layer:
            for b in self.layer[l]:
                if b.title == title:
                    return b

    def count_boxes(self):
        answer = 0
        for l in self.layer.values():
            answer += len(l)
        return answer

    def count_relationships(self):
        return len(self.relationships)

class box:
    """"The boxes contain text and are connected to each other."""
    def __init__(self, title, text=""):
        self.title = title
        self.text = text
        self.id = None
        self.subgroup = None

    def set_id(self, idno):
        self.id = idno

    #def delete_me(self, from_canvas):
    #    from_canvas.delete_box_by_id(self.id)

class relationship:
    """These objects are the relationships between boxes."""
    def __init__(self, from_box, to_box):
        self.from_box = from_box
        self.to_box = to_box
        self.id = None

    def draw(self):
        start = self.from_box.get_location()
        end = self.to_box.get_location()