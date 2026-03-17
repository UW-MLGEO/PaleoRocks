This folder contains all code used in the project. 

All CNN code can be found in the CNN folder, which is differentiated by center and whole patch classification. Each notebook in the CNN folder reads in pre-classified image data and outputs a model with performance metrics. Within each CNN notebook, data is augmented, split, and a model is fit and tested. 

The Image Preprocessing folder contains all code used to preprocess images for input into the CNN code. This includes code to resize the thin section images and to generate patches. 

**Directory**
- CNN/
    - This folder contains all CNN code for each model. 
- Image Preprocessing/
    - This folder contains code to preprocess thin section images for input into a CNN model. 