# National-ID-Reader
## Objective
The objective of this code is to create a program that can read and extract information from a national ID card in a specific format. The national ID card is assumed to have predefined slots for various information like the person's name, city, governorate, and ID number. The code's purpose is to process an image of the national ID card and extract the relevant information from these slots.
## Methods
The code achieves its objective by employing the following methods:
### Imports
- The code starts by importing necessary libraries and modules such as easyocr, cv2 (OpenCV), numpy, and skimage.morphology.
- It also imports the YOLO model for object detection using the ultralytics library.
### Class Definition
- The code defines a class named national_Id_reader to encapsulate all the functionality required for reading the national ID.
- Inside the class, various methods are defined to perform specific tasks.
### Initialization
- In the constructor (__init__ method), the class initializes the YOLO models for card segmentation and division, and the OCR (Optical Character Recognition) reader.
- It sets up the YOLO models for detecting card boundaries and dividing the card into slots.
- It configures the OCR reader to recognize text in the Arabic language and utilizes the GPU for acceleration.
### Cropping Methods
- The class defines two methods, cropLocations and cropImage, to crop specific regions of an image based on bounding box coordinates.
- These methods are used to isolate the individual slots on the national ID card.
### Getting ID Card Bounding Box
- The `Get_the_Id_bbox` method utilizes the card segmentation YOLO model to predict the bounding box of the entire national ID card.
- The method returns the coordinates of the bounding box.
### Getting Slot Content
- The `Get_the_Id_content` method uses the card division YOLO model to predict the locations of various slots on the national ID card.
- It returns a dictionary containing the names of slots as keys and their coordinates as values.
### Image Filtering
- The code includes two methods, `FilterStack` and `FilterStack2Id`, for filtering the images of the individual slots.
- These filters apply operations like grayscale conversion, blurring, thresholding, and morphological operations to enhance the text readability.
### Information Extraction
- The `extract_information` method is the core of the code and is responsible for extracting information from the national ID card.
- It follows these steps:
  - Gets the bounding box of the card.
  - Crops the image to focus on the card.
  - Predicts the locations of various slots on the card.
  - Crops each slot.
  - Resizes and filters each slot's image.
  - Uses OCR to read text from each slot, extracting the person's name, city, governorate, and ID number.
# Conclusion
The code's objective is to automate the extraction of information from a national ID card by leveraging object detection and OCR techniques. It provides a structured approach to handle the different components of the card and enhance the readability of text in each slot. The extracted information can then be used for various purposes, such as identity verification or data entry.
