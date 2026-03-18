This folder contains all code used in the project. 

All CNN code can be found in the CNN folder, which is differentiated by center and whole patch classification. Each notebook in the CNN folder reads in pre-classified image data and outputs a model with performance metrics. Within each CNN notebook, data is augmented, split, and a model is fit and tested. 

The Image Preprocessing folder contains all code used to preprocess images for input into the CNN code. This includes code to resize the thin section images and to generate patches. 

**Directory**
```
├── Code/
    ├── CNN/
        ├── CNN_FirstIteration_CenterClassification.ipynb     # Final center classification model
        ├── CNN_FirstIteration_WholePatch.ipynb               # Final whole patch model
        ├── CNN_FirstIteration_Copy.ipynb
        ├── Lucy_CNN_Attempt.ipynb
        └── Confusion Matrices/
            ├── First_Iteration_Confusion_Matrix.ipynb
            └── Final_Iteration_Confusion_Matrix.ipynb
    ├── Image Preprocessing/
        ├── AddCenterDot.ipynb
        ├── CreatePatches.ipynb
        ├── Resolution_Updater.ipynb
        └── ThinSectionExtraction.ipynb
    └── ReadME.md
```