import os
import logging
import argparse

from models.DFG_dataset import DFGDataset
from utils.category_mapper import category_map
from PIL import Image

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description="Extracting Traffic Sign samples from DFG dataset")
parser.add_argument("--images_dir", help="Path to directory with images")
parser.add_argument("--data_desc", help="Path to json file with annotations")
arg = parser.parse_args()

if arg.images_dir is None or arg.data_desc is None:
    logging.error("Argument --images_dir or --data_desc not specified")
else:
    images_dir_path = arg.images_dir
    data_desc_path = arg.data_desc
    dfg_dataset = DFGDataset(data_desc_path)

output_dir = 'output'
output_dir_path = os.path.join(os.getcwd(), output_dir)


def determine_category_filename(category_dir_path) -> str:
    dir_list = os.listdir(category_dir_path)

    if not dir_list:
        return '1.jpg'

    sorted_dir_list = sorted(dir_list, key=lambda d: int(d.split('.')[0]))
    last_element = sorted_dir_list[-1]
    filename_index = int(last_element.split('.')[0]) + 1
    return str(filename_index) + '.jpg'


def extract_traffic_signs(image_path, ts_bbox, category_id):
    if not os.path.isfile(image_path):
        logging.warning(f'File {image_path} not found')
        return

    image = Image.open(image_path)
    left = ts_bbox[0]
    upper = ts_bbox[1]
    right = left + ts_bbox[2]
    lower = upper + ts_bbox[3]
    cropped_image = image.crop((left, upper, right, lower))

    category_id_mapped = category_map.get(category_id)
    category_dir = os.path.join(output_dir_path, str(category_id_mapped))

    if not os.path.isdir(category_dir):
        logging.info(f'Creating directory: {category_dir}')
        os.mkdir(category_dir)

    cropped_image.save(os.path.join(category_dir, determine_category_filename(category_dir)))


def export_samples():
    if not os.path.isdir(output_dir_path):
        os.mkdir(output_dir_path)

    for annotation in dfg_dataset.annotations:
        category_id = annotation['category_id']

        if category_id in category_map:
            image_file = dfg_dataset.find_image(annotation['image_id'])
            image_filename = image_file.filename
            ts_bbox = annotation['bbox']
            extract_traffic_signs(os.path.join(images_dir_path, image_filename), ts_bbox, category_id)


export_samples()
