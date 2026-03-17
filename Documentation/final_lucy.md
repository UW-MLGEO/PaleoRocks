# <u>PaleoRocks: A machine learning approach to fossil identification and quantification</u>

## <u>Team Members</u>

### ESS 569:

- <b>Laura Thomas:</b> Second year AMATH Ph.D. student with expertise in numerical linear algebra and algorithms. Led model implementation and contributed immensely to coding, machine learning theory, and model evaluation.

- <b>Lucy Helms:</b> First year ESS Ph.D. student with expertise in sedimentology and paleontology. Led preparation of the training dataset and contributed immensely to project conceptualization, research question development, and preprocessing of image data.

### ESS 469:

- <b>Dahlia Gietka:</b> Fouth year ESS undergraduate with expertise in soils, geohazards, and science communication. Led literature review and motivation and contributed immensely to building training data, researching methods, and model selection.

- <b>Sophia Robillard:</b> Fourth year ESS undergraduate with expertise in isotope geochemistry and carbonate petrography. Led image preprocessing and contributed immensely to model evaluation, building training data, and visualizing results.

## <u> Introduction <u>
Throughout the geosciences, and particularly in the realm of paleontology, point counting is the standardized method for quantifying the bulk composition of a rock from a single thin section (Flügel et al. 2010, Pruss and Clemente 2011). It is a particularly powerful tool for analyzing skeletal abundance through time. However, point counting is time consuming, lacks a uniform understanding of sources of error, and can be susceptible to observer bias resulting from different experience and confidence levels. Machine learning and AI tools have the potential to resolve many of these issues, allowing for the analysis of larger datasets spanning longer periods of time.

## <u> <b> Research Question: </b> </u>
### Can we build a model that can point count as well as an expert?
Or, more specifically:
### Can our model predict if a thin section image does or does not contain a fossil?


## <u> Background & Motivation </u>
### ML in Paleontology
Machine learning approaches are particularly useful in paleontological classifications because it helps overcome some of the challenges mentioned above, such as:
- Observer bias
- Data scarcity
- Subjective interpretations
- Time constraints

Ultimately, machine learning approaches have the potential to increase paleontological classification accuracy and efficiency (Marques et al. 2025).

A review paper by Marques et al. (2025) compiled studies of machine learning in paleontological identification and classification, and found that most existing studies that leverage AI/ML in paleontological research:
- Utilize deep learning (CNN, DNN) and computer vision
- Apply ML for morphological analysis or segmentation
- Are temporally restricted to the Quaternary
- Are spatially restricted to North America and China

## Our ML Approach
With our model, we aim to build on the existing body of ML in paleontology by:
- Utilizing transfer learning with a CNN architecture
- Identify if an object is/ is not an fossil
- <b>Not</b> trying trace or outline the fossil
- Trying to develop a workflow for researchers to apply to their own thin sections, from any time, to identify and (hopefully, later) quantify the fossil composition of a sample

## <u> Model Design </u>
### <u> Inputs </u>
- Thin section images 

### Training Data
- Classified thin section images of samples from the Lower to Middle Ordovician Pogonip Group strata of the Arrow Canyon Range, Nevada
![Dahlia's three panel figure of dataset characterization.](Figures/469_Dahlia_Panel.jpg)
![Caption for Dahlia's three panel figure of dataset characterization.](Figures/469_Dahlia_Caption.jpg)

### Validation Data
- The classified patches were randomly split into 80% training and 20% validation

### Testing Data
- Prior to splitting the patches into training or validation, one sample from each unit (Opb, Opc, Opd, Ope, and Opf) was randomly selected and all images from those samples were withheld. 
    - The model tested on the Arrow Canyon Range thin section images it had never seen before
- Carbonate thin section images were obtained from CarbonateWorld, an online database and teaching tool for carbonate petrography.
    - The model tested on patches generated from 10 different CarbonateWorld thin sections, from different lithofacies and time periods than our own dataset.

### <u> Outputs </u>
- Classification of each patch as fossil or non-fossil
- Metric of model accuracy

## Glossary
- <b> Sample: </b> A piece of rock that represents a discrete period of time.
- <b> Thin section: </b> Part of a rock sample glued to a piece of glass and finely ground down so that light can pass through and the rock can be analyzed under a microscope.
    - The morphological and optical properties of each unique part of the thin section allow for the identification of fossil and non-fossil components, which in turn allows for the classification of the composition of the entire rock sample.
- <b> Point Counting: </b> Image-based method of identifying and quantifying the composition of a whole sample from a thin section.
- <b> Petrography: </b> Study of the classification of rocks, typically utilizing a microscope.
- <b>Geologic Unit:</b> A package of rocks characterized and/ or binned by common features. These features can be a shared period of time, similar lithologies, similar fossil contents, similar environments, etc. It is a general descriptive term for when and where your rocks come from.
    - e.g. Lucy Helms' rock samples come from units Opb, Opc, Opd, Ope, and Opf (geologic units) of the Arrow Canyon Range.
- <b> Strata: </b> The layers of rock comprising a geologic unit.
- <b> Lithofacies: </b> Each unique combination of physical characteristics that denote different rock types.

## References
- Flügel, E., 2010, Microfacies of Carbonate Rocks: Springer, Berlin, Heidelberg. http://link.springer.com/10.1007/978-3-662-08726-8.

- Marques, C.S., Malafaia, E., Pereira, S., Santos, V.F., and Dufourq, E., 2025, A review of machine learning applications for identification and classification problems in paleontology: Ecological Informatics, v. 91, p. 103329, doi:10.1016/j.ecoinf.2025.103329.

- Pruss, S.B., and Clemente, H., 2011, Assessing the Role of Skeletons in Early Paleozoic Carbonate Production: Insights from Cambro-Ordovician Strata, Western Newfoundland, in Laflamme, M., Schiffbauer, J.D., and Dornbos, S.Q., eds., Quantifying the Evolution of Early Life: Numerical Approaches to the Evaluation of Fossils and Ancient Ecosystems: Springer Netherlands, Dordrecht, p. 161–183. https://doi.org/10.1007/978-94-007-0680-4_7.