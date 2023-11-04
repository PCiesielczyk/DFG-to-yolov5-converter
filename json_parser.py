from models.DFG_dataset import DFGDataset
from models.DFG_label import DFGLabel
from utils.category_filter import forbidden_classes_ids
import logging

logging.basicConfig(level=logging.DEBUG)


def parse_to_dfg_labels(filename) -> dict[str, list[DFGLabel]]:
    grouped_dfg_labels: dict[str, list[DFGLabel]] = {}
    dataset = DFGDataset(filename)

    logging.info("Deserializing json...")

    classnames_file_path = "classnames.txt"
    forbidden_classnames_file_path = "forbidden_classes.txt"
    forbidden_classes = forbidden_classes_ids(classnames_file_path, forbidden_classnames_file_path)

    for annotation in dataset.annotations:

        if annotation["category_id"] in forbidden_classes:
            continue

        image = dataset.find_image(annotation["image_id"])
        bbox = annotation["bbox"]

        if image.filename in grouped_dfg_labels:
            grouped_dfg_labels[image.filename].append(DFGLabel(image, bbox))
        else:
            grouped_dfg_labels[image.filename] = [DFGLabel(image, bbox)]

    return grouped_dfg_labels
