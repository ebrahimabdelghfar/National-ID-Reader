
NationalId - v4 2023-10-16 12:25pm
==============================

This dataset was exported via roboflow.com on October 16, 2023 at 9:27 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 127 images.
-firstname-name-street-gov-city-IdNo- are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Grayscale (CRT phosphor)
* Auto-contrast via histogram equalization

The following augmentation was applied to create 3 versions of each source image:
* Random shear of between -19° to +19° horizontally and -12° to +12° vertically
* Salt and pepper noise was applied to 3 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Random Gaussian blur of between 0 and 5 pixels


