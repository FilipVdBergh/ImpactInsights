import impin
import impin_pygameplot
import impin_textplot

canvas = impin.canvas(layernames=("input", "throughput", "output"), title="Testplot")

def parse(user_input):
    if " " in user_input:
        command = user_input.lower().split(" ",maxsplit=1)[0]
        arguments = user_input.lower().split(" ",maxsplit=1)[1].split(";")
    else:
        command = user_input
        arguments = []
    return command, arguments

textplot = impin_textplot.textplot()
graphicalplot = impin_pygameplot.pygameplot(1080, 768)
graphicalplot.bg_picture = 'smg.jpg'

cont = True
while cont:
    command, arguments = parse(input("> "))
    if command == "quit":
        cont = False
    elif command == "list" or command== "print":
        canvas.plot(textplot)
    elif command == "plot":
        canvas.plot(graphicalplot)
    elif command == "add":
        if len(arguments) < 2:
            print("Usage: add;layer;title;[text]")
        else:
            if len(arguments) == 2:
                box = canvas.add_box(arguments[0], arguments[1], "None")
            elif len(arguments) == 3:
                box = canvas.add_box(arguments[0], arguments[1], arguments[2])
            print("Added box %s (Id %s)" % (box.title, box.id))
    elif command == "del":
        if len(arguments) < 1:
            print("Usage: del id")
        elif len(arguments) == 1:
            box = canvas.get_box_by_id(arguments[0])
            print("Deleted box %s (Id %s)" % (box.title, box.id))
            canvas.delete_box(box)
    elif command == "?":
        if len(arguments) < 1:
            print("Usage: ? id/title")
            canvas.plot(textplot)
        elif len(arguments) == 1:
            if arguments[0].isdigit():
                box = canvas.get_box_by_id(arguments[0])
            else:
                box = canvas.get_box_by_title(arguments[0])
            print("%s, %s (%s)"%(box.id, box.title, box.text))
    elif command == "layers":
        if len(arguments) < 1:
            print("Usage: layers l1;l2[;l3;...]")
        else:
            canvas.layernames = arguments
            canvas.layer = {l: list() for l in range(len(canvas.layernames))}
    elif command == "bg":
        if len(arguments) < 1:
            print("Usage: bg background")
        else:
            graphicalplot.bg_picture = arguments[0]
    else:
        print("Command not recognized: ", command)