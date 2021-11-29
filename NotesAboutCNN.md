## CNN

* CNN
* Difference between CNN and ConvNet
* State-of-art accuracy: 
* Popular networks / model : Vgg16, Vgg19, ResNet50, GoogleNet, Resnet, DenseNet;

* [Theory introduction Preparation](https://puneetkhanna777.medium.com/image-classification-using-convolutional-neural-network-89e751416cc3)
* [CNN implementation](https://www.analyticsvidhya.com/blog/2021/01/image-classification-using-convolutional-neural-networks-a-step-by-step-guide/)
* [Futher theory](https://www.learndatasci.com/tutorials/convolutional-neural-networks-image-classification/)
## Conv Layer
The convolutional layer (conv layer) is the central part of a CNN. In a large Input image, a small section of the image is considered and we convolve them into a single output using a filter (Kernel).

## Pooling
Pooling merely means down sampling of an image. It takes small region of the convolutional output as input and sub-samples it to produce a single output. Different pooling techniques like max pooling, mean pooling, average pooling is available. Max pooling takes largest of the pixel values of a region

## Fully Connected Layer and when it is used

* Fully Connected Layer:

* Fully connected (FC) layers are always used as the last layers of a CNN. This layer takes input from all neurons in the previous layer and performs arithmetic sum of the preceding layer of features with individual neuron in the current layer to generate output