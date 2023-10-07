from models.image_file import ImageFile


class DFGLabel:
    def __init__(self, image: ImageFile, bbox):
        self.image = image
        self.bbox = bbox
