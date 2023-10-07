from models.YOLOv5_object import YOLOv5Object
import re


class YOLOv5Label:
    def __init__(self, filename, yolov5_objects: list[YOLOv5Object]):
        self.filename = remove_extension(filename)
        self.yolov5_objects = yolov5_objects

    def __str__(self):
        output_string = ""

        for yolov5_object in self.yolov5_objects:
            line = f"0 {yolov5_object.x_center} {yolov5_object.y_center} {yolov5_object.width} {yolov5_object.height}\n"
            output_string += line

        return output_string


def remove_extension(filename):
    return re.sub(r'\..*', '', filename)
