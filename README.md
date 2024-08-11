Please download model from 




Black and white image colorization with OpenCV.
Table of Content

    Demo
    Overview
    Motivation
    Technical Aspect
    Installation And Run
    Directory Tree
    To Do
    Bug / Feature Request
    Technologies Used
    Team
    License
    Credits

Demo

Alt Text
Overview

Image colorization is the process of taking an input grayscale (black and white) image and then producing an output colorized image that represents the semantic colors and tones of the input (for example, an ocean on a clear sunny day must be plausibly “blue” — it can’t be colored “hot pink” by the model).
Motivation

When I learned linear algebra and came to know about how the machine inteprets pictures as tensors and concept of image segmentation. I remember there were some movies which was restored and picutured in theatre. I just came across Research papers of University of california in image colorization. And most iimportantly when I colorized photos of my Grandmother with gorgeous saree, that smile in my mother's face worth it.

Here is a photo of Che guevara from 60's colorized:

Technical Aspect

    The technique we’ll be covering here today is from Zhang et al.’s 2016 ECCV paper, Colorful Image Colorization. Developed at the University of California, Berkeley by Richard Zhang, Phillip Isola, and Alexei A. Efros.

    Previous approaches to black and white image colorization relied on manual human annotation and often produced desaturated results that were not “believable” as true colorizations.

    Zhang et al. decided to attack the problem of image colorization by using Convolutional Neural Networks to “hallucinate” what an input grayscale image would look like when colorized.

    To train the network Zhang et al. started with the ImageNet dataset and converted all images from the RGB color space to the Lab color space.

    Similar to the RGB color space, the Lab color space has three channels. But unlike the RGB color space, Lab encodes color information differently:
        The L channel encodes lightness intensity only
        The a channel encodes green-red.
        And the b channel encodes blue-yellow.

    As explained in the original paper, the authors, embraced the underlying uncertainty of the problem by posing it as a classification task using class-rebalancing at training time to increase the diversity of colors in the result. The Artificial Intelligent (AI) approach is implemented as a feed-forward pass in a CNN (“Convolutional Neural Network”) at test time and is trained on over a million color images.

    The color photos were decomposed using Lab model and “L channel” is used as an input feature and “a and b channels” as classification labels as shown in below diagram.

    The trained model (that is available publically and in models folder of this repo or download it by clicking here), we can use it to colorize a new B&W photo, where this photo will be the input of the model or the component “L”. The output of the model will be the other components “a” and “b”, that once added to the original “L”, will return a full colorized image.

The entire (simplified) process can be summarized as:

    Convert all training images from the RGB color space to the Lab color space.
    Use the L channel as the input to the network and train the network to predict the ab channels.
    Combine the input L channel with the predicted ab channels.
    Convert the Lab image back to RGB.

Installation And Run

1.The Code is written in Python 3.7. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt

    Run the file with:

$ streamlit run app.py

Directory Tree

|   app.py  
+---Input_images
|       che-guevara-.jpg
|       pexels-pixabay-141651.jpg
|       pexels-pixabay-36755.jpg      
+---models
|       colorization_release_v2.caffemodel
|       models_colorization_deploy_v2.prototxt
|       pts_in_hull.npy     
\---Result_images
        colored_c1.jpg
        colored_c7.jpg
        colored_c8.jpg

To Do

    To Convert the application to colorize black and white videos.

Bug / Feature Request

If you find a bug , kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
Technologies Used

Team
Dhananjayan
License

Apache license

Copyright 2020 Dhananjayan R

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
Credits
