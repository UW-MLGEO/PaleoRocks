# <u>ESS 469/569: Machine Learning in the Geosciences</u>

## <u>PaleoRocks</u>
A machine learning approach to fossil identification and quantification

### <u>Team Members</u>

#### ESS 569:

- Laura Thomas
- Lucy Helms

#### ESS 469:

- Dahlia Gietka
- Sophia Robillard

## <u>Objectives</u>
Throughout the geosciences, and particularly in the realm of paleontology, point counting is the standardized method for quantifying the bulk composition of a rock from a single thin section (Flügel et al. 2010, Pruss and Clemente 2011). It is a particularly powerful tool for analyzing skeletal abundance through time. However, point counting is time consuming, lacks a uniform understanding of sources of error, and can be susceptible to observer bias resulting from different experience and confidence levels. Machine learning and AI tools have the potential to resolve many of these issues, allowing for the analysis of larger datasets and longer periods of time.

## <u>Research Question</u>
Can we leverage AI/ ML to build a model that can identify fossils and point count as well as an expert?

## <u>Training Data</u>
Our training data are a subset of 217 thin section images from member Lucy Helms. These 217 images come from 83 samples. We will create code to generate random patches of size 200 x 200. We will work as a group to classify these images after reducing resolution to 10% of the origina, from 4000x6000 pixels to 400x600. We will then augment the data by rotating and reflecting these images after classifying. 

## <u>Testing Data</u>
Our testing data comprises images of thin sections from the same locality as our training data and images of thin sections from entirely different time periods and geologic units, downloaded from CarbonateWorld.

## <u> Repository Structure </u>

```
Paleorocks/
├── Code/
|    ├── CNN/
|        ├── CNN_FirstIteration_CenterClassification.ipynb     # Final center classification model
|        ├── CNN_FirstIteration_WholePatch.ipynb               # Final whole patch model
|        ├── CNN_FirstIteration_Copy.ipynb
|        ├── Lucy_CNN_Attempt.ipynb
|        └── Confusion Matrices/
|            ├── First_Iteration_Confusion_Matrix.ipynb
|            └── Final_Iteration_Confusion_Matrix.ipynb
|    ├── Image Preprocessing/
|        ├── AddCenterDot.ipynb
|        ├── CreatePatches.ipynb
|        ├── Resolution_Updater.ipynb
|        └── ThinSectionExtraction.ipynb
|    └── ReadME.md
├── Documentation/
|   ├── Final_Writeup.md
│   └── ReadME.md                   
├── Figures/
│   ├── Data-Examples/                       
│   ├── Model-Performance/                   
│   ├── 469_Dahlia_Caption.jpg
│   ├── 469_Dahlia_Panel.jpg
│   ├── Dahlia_Figure.pdf
|   ├── Sophia_Final_Figure.png
│   └── ReadME.md
└── ReadME.md                           
```

## <u>Contents</u>

The **code folder** contains all code. The **CNN subfolder** contains all code for CNN, as follows:

- **CNN_FirstIteration_CenterClassification.ipynb**
    - Contains all final code to generate and run a center classification model, along with performance metrics.
- **CNN_FirstIteration_WholePatch.ipynb**
    - Contains all final code to generate and run a center classification model, along with performance metrics.
- **CNN_FirstIteration_Copy.ipynb**
    - Contains initial CNN code that was later modified, kept for documentation of iterations.
- **Lucy_CNN_Attempt.ipynb**
    - Contains initial CNN code that was later modified to randomly select thin section images for testing data.
-  **Confusion Matrices/**
    - This folder contains code to generate confusion matrices based off of test and unseen data. 

The **Image Preprocessing subfolder** contains all code to preprocess thin section images for use in the CNN models: 

- **AddCenterDot.ipynb**
    - Adds dot in the center of a thin section patch, used to classify training data for a center patch classification model.
- **CreatePatches.ipynb**
    - Contains functions for generating image patches from an input thin section on either a grid or at random.  
- **Resolution_Updater.ipynb**
    - Updates the resolution of a given thin section image to a user-specified size.
- **ThinSectionExtraction.ipynb**
    - Initial code to extract thin sections for testing data. A modified version was contained in the final CNN model codes. 

The **Documentation folder** contains the final project writeup, including results of the model runs and discussions on future directions. 

The **Figures folder** contains all relevant figures generated from the code and used in the documentation markdown files. The **Data-Examples subfolder** contains examples of each stage of our data preparation, including an example of patches of our training data, patches of the unseen data from CarbonateWorld, and an example of data augmentation on one patch of our training data. 

The **Model-Performance subfolder** contains all images relevant to model performance, including loss and accuracy plots for both models, ROC plots for both models, confusion matrices, and tables of performance metrics. A full discussion of these results can be found in the **Final_Writeup.md**. 

The figures folder also contains multipanel figures created by group members Dahlia Gietka and Sophia Robillard. Dahlia's figure gives a statistical breakdown of the image patch data used in the training and testing of our model, and Sophia's figure gives a general overview of our model and machine learning approach. 

### <u>Glossary</u>

<u>Sample:</u> A piece of rock that represents a discrete period of time.

<u>Thin section:</u> Part of a rock sample glued to a piece of glass and finely ground down so that light can pass through and the rock can be analyzed under a microscope.

<u>Point Counting:</u> Image-based method of identifying and quantifying the composition of a whole sample from a thin section.

<u>Locality:</u> A study site

<u>Geologic Unit:</u> A package of rocks characterized and/ or binned by common features. These features can be a shared period of time, similar lithologies, similar fossil contents, similar environments, etc. It is a general descriptive term for when and where your rocks come from
- e.g. Lucy Helms' rock samples come from unit Opb, Opc, Opd, Ope, and Opf (geologic units) of the Arrow Canyon Range (locality) in southwest Nevada, U.S.A..

### <u>References</u>

- Chollet, Francois and others, 2015, Keras. https://keras.io

- Flügel, E., 2010, Microfacies of Carbonate Rocks: Springer, Berlin, Heidelberg. http://link.springer.com/10.1007/978-3-662-08726-8. Checked March 2024.

- Marques, C.S., Malafaia, E., Pereira, S., Santos, V.F., and Dufourq, E., 2025, A review of machine learning applications for identification and classification problems in paleontology: Ecological Informatics, v. 91, p. 103329, doi:10.1016/j.ecoinf.2025.103329.

- Pruss, S.B., and Clemente, H., 2011, Assessing the Role of Skeletons in Early Paleozoic Carbonate Production: Insights from Cambro-Ordovician Strata, Western Newfoundland, in Laflamme, M., Schiffbauer, J.D., and Dornbos, S.Q., eds., Quantifying the Evolution of Early Life: Numerical Approaches to the Evaluation of Fossils and Ancient Ecosystems: Springer Netherlands, Dordrecht, p. 161–183. https://doi.org/10.1007/978-94-007-0680-4_7. Checked April 2024.


