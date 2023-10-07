import os
import logging
from models.YOLOv5_label import YOLOv5Label

logging.basicConfig(level=logging.DEBUG)


def yolov5_labels_to_txt(yolov5_labels: list[YOLOv5Label]):
    output_dir_name = "output"

    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)
    else:
        logging.info(f"Directory '{output_dir_name}' already exists. Will overwrite")
        clean_dir(output_dir_name)

    logging.info("Saving labels to output directory...")

    for yolov5_label in yolov5_labels:
        with open(f"{output_dir_name}/{yolov5_label.filename}.txt", "w") as file:
            file.write(yolov5_label.__str__())


def clean_dir(dir_name):
    items = os.listdir(dir_name)

    for item in items:
        item_path = os.path.join(dir_name, item)

        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            for root, dirs, files in os.walk(item_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                for directory in dirs:
                    dir_path = os.path.join(root, directory)
                    os.rmdir(dir_path)
