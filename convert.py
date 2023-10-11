import logging
import argparse
from json_parser import parse_to_dfg_labels
from labels_export import yolov5_labels_to_txt
from models.DFG_label import DFGLabel
from models.YOLOv5_object import YOLOv5Object
from models.YOLOv5_label import YOLOv5Label

logging.basicConfig(level=logging.DEBUG)


def convert(dfg_labels_grouped: dict[str, list[DFGLabel]]) -> list[YOLOv5Label]:
    logging.info("Converting DFG labels to yolov5 format...")

    yolov5_labels_output = []
    for filename, dfg_labels_in_same_image in dfg_labels_grouped.items():
        yolov5_objects_in_same_image = []
        for dfg_label in dfg_labels_in_same_image:
            dfg_x = dfg_label.bbox[0]
            dfg_y = dfg_label.bbox[1]
            dfg_width = dfg_label.bbox[2]
            dfg_height = dfg_label.bbox[3]

            x_center = dfg_x + (dfg_width / 2)
            y_center = dfg_y + (dfg_height / 2)

            x_center_normalized = x_center / dfg_label.image.width
            y_center_normalized = y_center / dfg_label.image.height
            width_normalized = dfg_width / dfg_label.image.width
            height_normalized = dfg_height / dfg_label.image.height

            yolov5_object = YOLOv5Object(x_center_normalized, y_center_normalized, width_normalized, height_normalized)
            yolov5_objects_in_same_image.append(yolov5_object)

        yolov5_label = YOLOv5Label(filename, yolov5_objects_in_same_image)
        yolov5_labels_output.append(yolov5_label)

    return yolov5_labels_output


parser = argparse.ArgumentParser(description="Converting labels from DFG dataset to YOLOv5 format.")
parser.add_argument("--filename", help="Path to json file with DFG dataset annotations")
arg = parser.parse_args()

if arg.filename is None:
    logging.error("Argument --filename not specified")
else:
    dfg_labels = parse_to_dfg_labels(arg.filename)
    yolov5_labels = convert(dfg_labels)
    yolov5_labels_to_txt(yolov5_labels)
