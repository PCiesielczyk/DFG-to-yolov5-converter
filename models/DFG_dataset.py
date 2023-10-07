import json
from models.image_file import ImageFile


class DFGDataset:
    def __init__(self, json_filename):
        json_file = open(json_filename)
        dataset = json.load(json_file)
        self.images = dataset["images"]
        self.categories = dataset["categories"]
        self.annotations = dataset["annotations"]

    def find_image(self, image_id: int) -> ImageFile:
        image_dict = next((item for item in self.images if item["id"] == image_id), None)

        filename = image_dict["file_name"]
        width = image_dict["width"]
        height = image_dict["height"]

        return ImageFile(filename, width, height)
