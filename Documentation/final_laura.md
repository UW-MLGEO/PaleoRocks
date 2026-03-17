## <u> ML Approach</u>
### <u>CNN with Transfer Learning</u>
For our model, we chose to use a convolutional neural network (CNN) with *transfer learning*. Transfer learning allowed us to use a pre-constructed model architecture with pre-trained weights, which we called the **base model**. We then added our own layers to this model, which we called our **top layers**. 

We chose this type of model architecture because CNN is standard across the literature, yet transfer learning is a powerful but underutilized tool, as only about 32% of existing paleontological machine learning studies use transfer learning. (Marques et al. 2025) This type of architecture allowed us to save computational resources because we did not have to train our model from scratch. 

We used the Xception model as our base model, and it was trained on the ImageNet dataset, a dataset of millions of pre-classified images. We made these choices because they are standard in the field and promote computational efficiency (Marques et al. 2025). Other models that could be implemented and explored are VGG16, VGG19, ResNet, and EfficientNet. 

In our code, we utilized the **Keras** package in **Python**. This package has these models (and others!) built in and pre-trained on the ImageNet dataset. 

### <u>Training Two Models</u>

We trained two models in our approach. Our initial model classified based on whether or not there was a fossil anywhere within each thin section patch. To more accurately simulate point counting, we developed a second model, which classified based on whether or not there was a fossil within the exact center of each patch. We found the exact center using code that can be found in AddCenterDot.ipynb. 

### <u>Data Augmentation</u>
To promote robustness of our model and to increase the size of our training dataset, we implemented data augmentation techniques. Data augmentation is another underutilized tool in paleontological machine learning studies, with only around 32% of existing studies augmenting their data (Marques et al. 2025). 



## <u>Results</u>

## <u>Discussion</u>

## <u>Future Work</u>