# Project 5: Using a neural network to classify images of intertidal invertebrates

My Metis project 5.

## 1. Background
During my master's research, I spent lots of time tidepooling. I was conducting phylogenetic analysis on a species of sea star, and I would frequently spend multiple hours in intertidal habitats trying to identify various species. This is a perfect machine learning problem, and in this project, I used a pre-trained neural network to build an image classifier able to classify six different phyla of intertidal invertebrates.

My goal was to see if my model could successfully take in images of different intertidal invertebrate groups and identify them.

## 2. Workflow
- Downloaded training images from Google images using the ["Download all images" plugin](https://chrome.google.com/webstore/detail/download-all-images/nnffbdeachhbpfapjklmpnmjcgamcdmm?hl=en)
- Considered 6 classes:
  - [Anemones](https://en.wikipedia.org/wiki/Sea_anemone)
  - [Barnacles](https://en.wikipedia.org/wiki/Barnacle)
  - [Bivalves](https://en.wikipedia.org/wiki/Bivalvia)
  - [Crabs](https://en.wikipedia.org/wiki/Crab)
  - [Nudibranchs](https://en.wikipedia.org/wiki/Nudibranch)
  - [Sea stars](https://en.wikipedia.org/wiki/Starfish)
- Utilized pre-trained [YOLO v3](https://pjreddie.com/darknet/yolo/) convolutional neural network
  - Utilized [Darknet](https://pjreddie.com/darknet/) framework
  - Utilized [openCV](https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/) python module
- Trained model on 1102 images total across 6 classes
  - Batch size = 64
  - Max batches = 12,000
  - Number of epochs ~ 700
- Tested model on ~25 images across all class
- Conducted partial retrain from iteration 6000 to improve performance on bivalve and crab classes
- Constructed [visualization](https://intertidal-invert-identifier.herokuapp.com/) in [Streamlit](https://www.streamlit.io/), deployed on [Heroku](https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=CjwKCAiA_Kz-BRAJEiwAhJNY72Pjw-dMX1joPj11t2zgyeOBsDu9k5nLeEnMLsn7xDCOVookgaWOHxoC6woQAvD_BwE)

## 3. Results summary
- Good performance on all classes!
- Model can struggle on images that contain multiple different class or images that contain other objects

## 4. Takeaways and future work
Overall, the model performed well! I was able to achieve good performance on each class. 

Future work would involve a larger testing set, to start. Due to the nature of the problem, I chose testing images to test that were not used for training; however, a system compiling of a testing image set would allow for more thorough vetting of the model. Additionally, varied images of each class would be beneficial. However, this is subjective, and I tested this model on images that were available.

Ultimately, I would like this model to be able to identify individual organisms, rather than simply different phyla. This idea is similar to the existing app [iNaturalist](https://www.inaturalist.org/), but using machine learning instead of relying on other users to respond to your queries. However, that would require a lot of training images and was outside the scope of this project -- this is a proof of concept that an existing neural network can be trained to recognize intertidal invertebrates.

## 5. Tools and techniques used
- [Jupyter](https://jupyter.org/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true)
- [YOLO convolutional neural network model](https://pjreddie.com/darknet/yolo/)
  - [Darknet](https://pjreddie.com/darknet/)
  - [OpenCV](https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/)
- [Streamlit](https://www.streamlit.io/)
- [Heroku](https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=CjwKCAiA_Kz-BRAJEiwAhJNY72Pjw-dMX1joPj11t2zgyeOBsDu9k5nLeEnMLsn7xDCOVookgaWOHxoC6woQAvD_BwE)
- Other useful tutorials:  
  -[Training the YOLO model using a GPU in Colab walkthrough](https://www.youtube.com/watch?v=10joRJt39Ns&feature=emb_logo) and [notebook](https://colab.research.google.com/drive/1Mh2HP_Mfxoao6qNFbhfV3u28tG8jAVGk) from [The AI Guy](https://www.youtube.com/channel/UCrydcKaojc44XnuXrfhlV8Q) on YouTube  
  -[Image detection with openCV](https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html#load-the-yolo-network)  
  -[Another great YOLO image detection walkthrough](https://pysource.com/2020/04/02/train-yolo-to-detect-a-custom-object-online-with-free-gpu/)  
  

Check out the app [here](https://intertidal-invert-identifier.herokuapp.com/) or watch a demo of it in the .mov file above! Blog post incoming.

Special thanks to Brian McGarry and Richard Chiou for assistance with experimental design and implementation, and to Ryan Werth and Neda Saleem for assistance with tutorials and troubleshooting!
