# DFG to YOLOv5 converter
### A tool for converting labels and extracting Traffic Sign samples from [DFG dataset](https://www.vicos.si/resources/dfg/) to YOLOv5 format.

## About
### Labels conversion
DFG Traffic Sign Data Set contains large amount of road images with traffic signs annotatations. It can be used to train traffic signs detection model using YOLOv5,
but to do so, a format conversion is needed. The image below shows the format of the road sign location description for DFG and YOLOv5. 
<img src="/images/parkingSignEng.jpg" alt="locationFormat">

The converter first calculates normalized coordinates and then saves output in created directory. The example of file conversion is shown below.
<img src="/images/fileFormat.png" alt="fileFormat">

### Extracting samples
The tool is also capable to extract samples for specified categories. Samples are grouped in separate directories:
<img src="/images/extractingSamples.png" alt="extractingSamples">

## Usage
### Labels conversion
This repository is submodule for [TSI-DCAI](https://github.com/PCiesielczyk/TSI-DCAI) project. It contains `requirements.txt` file with all necessary dependencies.
To create YOLOv5 labels files based on DFG dataset annotations use:
```
python convert.py --filename "path/annotations.json"
```
`--filename` defines path to json file with annotation. DFG dataset provides those files in `DFG-tsd-annot-json` category.

It is also possible to filter out some categories in conversion by specifying two files in repository root directory
- `classnames.txt`: provided by DFG dataset in `DFG-tsd-category-info` directory. It contains names of directory and its id.
- `forbidden_classes.txt`: category names to be ignored in conversion separated by newlines
`forbidden_classes.txt` example:
```
I-38
I-39-1
I-39-2
I-39-3
III-14
III-14.1
```

To extract samples, first edit `utils/category_mapper.py` and specify categories to be extract and directory names to be set. Extraction is performed with:
```
python extract_samples.py --images_dir "path/to/images/directory" --data_desc "path/annotations.json"
```
`--images_dir` defines path to directory with roads' images from DFG dataset.
`--data_desc` defines path to json file with annotation.
