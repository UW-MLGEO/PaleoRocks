# ESS 469/569: Machine Learning in the Geosciences

## PaleoRocks
A machine learning approach to fossil identification and quantification

### Members

#### ESS 569

Laura Thomas
Lucy Helms

#### ESS 469

Dahlia Gietka
Sophia Robillard

## Objectives
Throughout the geosciences, and particularly in the realm of paleontology, point counting is the standardized method for quantifying the bulk composition of a rock from a single thin section (Flügel et al. 2010, Pruss and Clemente 2011). It is a particularly powerful tool for analyzing skeletal abundance through time. However, point counting is time consuming, lacks a uniform understanding of sources of error, and can be susceptible to observer bias resulting from different experience and confidence levels. Machine learning and AI tools have the potential to resolve many of these issues, allowing for the analysis of larger datasets and longer periods of time.

## Research Question
Can we leverage AI/ ML to build a model that can identify fossils and point count as well as an expert?

## Training Data
Our training data are a subset of 217 thin section images from member Lucy Helms. These 217 images come from 83 samples. We will create code to generate random patches of size 200 x 200. We will work as a group to classify these images after reducing resolution to 10% of the origina, from 4000x6000 pixels to 400x600. We will then augment the data by rotating and reflecting these images after classifying. 

## Testing Data
Our testing data comprises images of thin sections from the same locality as our training data and images of thin sections from entirely different time periods and geologic units, downloaded from CarbonateWorld.

## Repository Structure
- Chart explaining the organization of our repository
## Contents
- Summarize what each individual file contains

### Glossary

Sample: A piece of rock that represents a discrete period of time.

Thin section: Part of a rock sample glued to a piece of glass and finely ground down so that light can pass through and the rock can be analyzed under a microscope.

Point Counting: Image-based method of identifying and quantifying the composition of a whole sample from a thin section.

Locality: A study site

Geologic Unit: A package of rocks characterized and/ or binned by common features. These features can be a shared period of time, similar lithologies, similar fossil contents, similar environments, etc. It is a general descriptive term for when and where your rocks come from
- e.g. Lucy Helms' rock samples come from unit Opb, Opc, Opd, Ope, and Opf (geologic units) of the Arrow Canyon Range (locality) in southwest Nevada, U.S.A..

### References
Flügel, E., 2010, Microfacies of Carbonate Rocks: Springer, Berlin, Heidelberg. http://link.springer.com/10.1007/978-3-662-08726-8. Checked March 2024.

Pruss, S.B., and Clemente, H., 2011, Assessing the Role of Skeletons in Early Paleozoic Carbonate Production: Insights from Cambro-Ordovician Strata, Western Newfoundland, in Laflamme, M., Schiffbauer, J.D., and Dornbos, S.Q., eds., Quantifying the Evolution of Early Life: Numerical Approaches to the Evaluation of Fossils and Ancient Ecosystems: Springer Netherlands, Dordrecht, p. 161–183. https://doi.org/10.1007/978-94-007-0680-4_7. Checked April 2024.
