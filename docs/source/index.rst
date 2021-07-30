.. _Welcome!:

LivestockCV's documentation
=======================================
Ryan Jeon, PhD Student, Iowa State University
ryanjeon@iastate.edu


Objective
----------

LivestockCV is one Python package designed to assist animal scientists and agricultural engineers in applying computer vision (CV) techniques to images or videos of livestock animals.
The neat thing about LivestockCV is that we can perform a variety of interesting functions to an image or a video, that would otherwise require several different packages, a hard coded script, or a solid understanding of command line. 

LivestockCV is designed for Google Colab, an interactive online notebook that has many benefits, including a very user friendly interface, the ability to break code into individual blocks, and to output media at any step we want to check to see what our code is doing, a useful application when it comes to computer vision problems.


(1) Mounting your Google Colab Drive
------------------------------------

Log into Google Colab using your Google account in the following link:
https://colab.research.google.com/

The very first step of using Colab is to always mount your drive by clicking the **Folder Mount** |mount| button on the left tab. Below is a screenshot of what my screen looks like.
This allows Colab to access your drive.

.. |mount| image:: /images/mount.png

.. Tip::
    You'll have to perform this step everytime you log back in or whenever Colab times out.

(2) Installing LivestockCV
------------------------------

Add a block of code and download the latest version of LivestockCV using this line:

.. code:: python

   !pip install LivestockCV

.. Tip:: 
   You'll only have to do this once, unless you find that LivestockCV has made a version update.


(3) Accessing your media
------------------------------
Each function in LivestockCV will require a path. This path is used so Colab can find an image.
You can easily copy/paste the path by navigating through the directories of your drive on the left tab. Once you found your image/video, clicking on the set of three dots to the right opens a menu to copy the file path. 

(4) Having fun!
---------------
These are the basics of using Colab, try your hand at some of these basic functions listed below: 
 * Import Image
 * Crop
 * Thresholding 

(5) Other functionalities!
---------------
Here are some cool things we can do with LivestockCV
 * Object detection
 * Calculating angles between lines
 * Measuring distance an animal moved
 * blah blah blah   
   

.. toctree::
   :maxdepth: 20
   :caption: List of LivestockCV's Core Functions
   
   Canny Edge Detection
   Blur (Gaussian)
   CalculateAngle
   Contouring
   Max Contour
   Crop
   Dilation
   Erosion
   Dimensions
   Invert
   Plot Image
   Region of Interest (ROI)
   RGB2Gray
   RGB to HSV
   RGB to CMYK
   RGB to LAB
   Rotate
   Show Image
   Thresholding
   
   
   
   
.. toctree::
   :maxdepth: 2
   :caption: List of Video Functions
   
   Face Detection
   Frame Count

.. toctree::
   :maxdepth: 2
   :caption: List of Deep Learning Functions (TBD)
   
   Typical SAT Math Problem 
   Animal Classifier    


.. toctree::
   :maxdepth: 2
   :caption: Licensing
   
   license
   help

   