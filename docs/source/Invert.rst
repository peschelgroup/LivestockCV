Invert
=============




Context:
~~~~~~~~

After thresholding or grayscaling, you may find particular use in inverting the image. 
White values are black and black values are white. 
Gray pixel values are also inverted.
 

Arguments:
~~~~~~~~
 * Requires a path to your image.
 * Grayscaled image. Using a RGB image will be spooky! 


Code:
~~~~~~~~

.. code:: python
   import cv2
   from LivestockCV import core as LivestockCV_core

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')

   print('                           Original Raw Image')
   LivestockCV_core.plot_image(img)
   grey_img = LivestockCV_core.rgb2gray(img)
   inverted_pig = LivestockCV_core.invert(grey_img)


   print('            Inverted Image')
   LivestockCV_core.plot_image(inverted_pig)



Results:
~~~~~~~~

.. figure:: /images/pig.png
Original Raw Image
      
      
.. figure:: /images/gray.png
This is what our pig looks like in grayscale

.. note::
notice the inversion of the background and the pigs eye

.. figure:: /images/invert.png
This is what our pig looks like inverted!

