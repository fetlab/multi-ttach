import pandas as pd
import random
import math


def get_center_point():
    gcode = open("vase35.gcode", "r")
    lines = gcode.readlines()
    flag = "no"
    first_layer = ""
    for l in lines:
        if ";TYPE:WALL-OUTER" in l:
            flag = "yes"
        elif ";TYPE:SKIN" in l:
            flag = "skin"
        if flag == "yes":
            first_layer = first_layer + l
        elif flag == "skin":
            break
    #print(first_layer)
    lines = first_layer.split("\n")
    # first point
    first_x = float(lines[1].split(" ")[2].split("X")[1])  # x coordinate
    first_y = float(lines[1].split(" ")[3].split("Y")[1])  # y coordinate
    max_dist = 0
    farthest_point = []
    for i in range(2, len(lines)):
        l = lines[i]
        if "X" in l and "Y" in l:
            x = float(l.split("X")[1].split(" ")[0])  # x coordinate
            y = float(l.split("Y")[1].split(" ")[0])  # y coordinate
            dist = math.sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
            if dist > max_dist:
                max_dist = dist
                farthest_point.clear()
                farthest_point.append(x)
                farthest_point.append(y)
        else:
            pass
    #print(max_dist)
    #print(farthest_point)
    midpoint_x = (first_x + farthest_point[0]) / 2
    midpoint_y = (first_y + farthest_point[1]) / 2

    return [midpoint_x, midpoint_y]


def modifying_gcode():

    gcode = open("vase35.gcode", "r")

    lines = gcode.readlines()

    center_point = get_center_point()

    flag = "no"

    result = ""

    layers = ""

    for l in lines:

        if ";TYPE:WALL-OUTER" in l:
            flag = "yes"
        elif ";TYPE:" in l:
            flag = "no"
        if flag == "yes" and ";TYPE:WALL-OUTER" not in l:
            splited = l.split(" ")
            new_x = ""
            new_y = ""

            for i in range(len(splited)):

                if "X" in splited[i]:
                    current_x = float(splited[i].split("X")[1])
                    direction_vector_x = current_x - center_point[0]
                    new_x = str(center_point[0] + (direction_vector_x * random.randint(100, 105) / 100))
                    break

            for j in range(len(splited)):

                if "Y" in splited[j]:
                    current_y = float(splited[j].split("Y")[1])
                    direction_vector_y = current_y - center_point[1]
                    new_y = str(center_point[1] + (direction_vector_y * random.randint(100, 105) / 100))
                    break

            replaced = ""

            for k in range(len(splited)):

                if k == i:
                    replaced += "X"+new_x + " "
                elif k == j:
                    replaced += "Y"+new_y + " "
                else:
                    replaced += splited[k] + " "
            #print(replaced)
            l = replaced
            #print(replaced)

        l = l.strip()

        if "\n" not in l:
            l += "\n"



        result = result + l

    text_file = open("vase35_droop.gcode", "wt")
    text_file.write(result)
    text_file.close()

    gcode2 = open("vase35_droop.gcode", "r")
    droop = gcode2.readlines()

    # get head/tail lines
    head = ""
    tail = ""

    for l in droop:
        if ";LAYER:0" in l:
            break
        else:
            head += l

    for l in droop:
        if ";TIME_ELAPSED:905.713563" in l:
            flag = "keep"
        elif flag == "keep":
            tail += l

    for ls in droop:
        #print(ls)
        if ";LAYER:" in ls and int(ls.split(":")[1]) % 10 != 1:
            #print(ls)
            flag = "keep"
            layers += ls
        elif ";LAYER:" in ls and int(ls.split(":")[1]) % 10 == 1:
            flag = "remove"
        elif flag == "keep":
            layers += ls

    text_file = open("vase35_droop_layerremove.gcode", "wt")
    text_file.write(head + layers + tail)
    text_file.close()


if __name__ == "__main__":
    modifying_gcode()