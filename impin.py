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
        self.layer = list(4)
        self.counter = 0

    def reorder(self):
        pass

    def add_box(self, box, layer):
        if layer in range(3):
            self.layer[layer].append(box)
            self.counter += 1
            box.setid(self.counter)

    def delete_box(self, idno):
        pass


class box:
    """"The boxes contain text and are connected to each other."""
    def __init__(self, title, text=""):
        self.title = title
        self.text = text
        self.id = None

    def set_id(self, idno):
        self.id = idno

    def get_id(self):
        return self.id

    def add_text(self, text):
        self.text = text