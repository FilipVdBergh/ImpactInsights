import impin
import impin_pygameplot, impin_textplot, impin_powerpointplot
import os
from win32com.client import Dispatch
import pickle

canvas = impin.canvas(layernames=("input", "throughput", "output"), title="Testplot")

def parse(user_input):
    if " " in user_input:
        command = user_input.lower().split(" ",maxsplit=1)[0]
        arguments = user_input.split(" ",maxsplit=1)[1].split(";")
    else:
        command = user_input
        arguments = []
    return command, arguments




cont = True
while cont:
    command, arguments = parse(input("%s > " % canvas.title))
    if command == "quit" or command == "exit":
        cont = False
    elif command == "save":
        if len(arguments) < 1:
            print("Saves a file. Usage: save [*/filename]")
        else:
            if arguments[0] == "*":
                arguments[0] = canvas.title + ".ii"
            if not ".ii" in arguments[0]:
                arguments[0] += ".ii"
            with open(arguments[0], 'wb') as file_output:
                pickle.dump(canvas, file_output, pickle.HIGHEST_PROTOCOL)
            print("Saved file %s" % arguments[0])
    elif command == "load":
        if len(arguments) < 1:
            print("Loads a file. Usage: load filename")
        else:
            if not ".ii" in arguments[0]:
                arguments[0] += ".ii"
            with open(arguments[0], 'rb') as file_input:
                canvas = pickle.load(file_input)
            canvas.plot(impin_textplot.textplot())
    elif command == "list" or command== "ls":
        canvas.plot(impin_textplot.textplot())
    elif command == "plot":
        canvas.plot(impin_pygameplot.pygameplot(1080, 768))
    elif command == "export" or command == "exp":
        if len(arguments) < 1:
            print("Exports a plot to Powerpoint. Usage: exp[ort] [*/filename]")
        else:
            ppplot = impin_powerpointplot.powerpointplot()
            if arguments[0] == "*":
                arguments[0] = canvas.title + ".pptx"
            if not ".pptx" in arguments[0]:
                arguments[0] += ".pptx"
            ppplot.filename = arguments[0]
            canvas.plot(ppplot)
            print("Saving " + ppplot.filename)

            pp = Dispatch('PowerPoint.Application')
            print("Open presentation "+os.getcwd()+"\\"+ppplot.filename)
            f = pp.Presentations.Open(os.getcwd()+"\\"+ppplot.filename)
            pp.Visible = True
    elif command == "add":
        if len(arguments) < 2:
            print("Adds a box. Usage: add;layer;title;[text]")
        else:
            if len(arguments) == 2:
                box = canvas.add_box(arguments[0], arguments[1], "None")
            elif len(arguments) == 3:
                box = canvas.add_box(arguments[0], arguments[1], arguments[2])
            print("Added box %s (Id %s)" % (box.title, box.id))
    elif command == "connect" or command == "con":
        if len(arguments) < 2:
            print("Connects two boxes. Usage: con[nect] id0;id1")
        elif len(arguments) == 2:
            box1 = canvas.get_box_by_id(arguments[0])
            box2 = canvas.get_box_by_id(arguments[1])
            canvas.add_relationship(box1, box2)
            print("Added connection from %s to %s" % (box1.title, box2.title))
    elif command == "del":
        if len(arguments) < 1:
            print("Deletes a box or a connection. Usage: del id")
        elif len(arguments) == 1:
            box = canvas.get_box_by_id(arguments[0])
            print("Deleted box %s (Id %s)" % (box.title, box.id))
            canvas.delete_box(box)
    elif command == "?":
        if len(arguments) < 1:
            print("Get box or connection information. Usage: ? id/title")
            canvas.plot(impin_textplot.textplot())
        elif len(arguments) == 1:
            if arguments[0].isdigit():
                box = canvas.get_box_by_id(arguments[0])
            else:
                box = canvas.get_box_by_title(arguments[0])
            print("%s, %s (%s)"%(box.id, box.title, box.text))
    elif command == "layers" or command == "lay":
        if len(arguments) < 1:
            print("Change layer names. May orphan boxes or relationships. Usage: lay[ers] l1;l2[;l3;...]")
            print(canvas.layernames)
        else:
            canvas.layernames = arguments
            canvas.layer = {l: list() for l in range(len(canvas.layernames))}
    elif command == "title":
        if len(arguments) < 1:
            print("Changes plot title. Usage: title title")
        else:
            canvas.title = arguments[0]
    else:
        print("Command not recognized: ", command)