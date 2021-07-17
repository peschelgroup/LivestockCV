RGB2Gray
=============




Context:
~~~~~~~~

Many functions require your input image to be in grayscale. 
Color images are in the form of RGB, a continuous trait as opposed to discrete values.
This causes problems in analysis, therefore, conversion to discrete values between 0-255 (black pixels - white pixels) is ideal.
Where gray pixels, are any values between black-white.

Arguments:
~~~~~~~~
 * Requires a path to your image.


Code:
~~~~~~~~

.. code:: python
   import cv2
   from LivestockCV import core as LivestockCV_core

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')

   print('                           Original Raw Image')
   LivestockCV_core.plot_image(img)
   grey_img = LivestockCV_core.rgb2gray(img)

   print('            Grey Image')
   LivestockCV_core.plot_image(grey_img)



Results:
~~~~~~~~

.. figure:: /images/pig.png
Original Raw Image
      
      
.. figure:: /images/gray.png
This is what our pig looks like in grayscale



