Max Contour
=============




Context:
~~~~~~~~

Contouring is an integral part of feature extraction. With contouring, we can do cool things like finding angles between straight lines!

This code will find the **largest** contour in a thresholded image (no color!) and "draw" it on our original image. 

.. Tip:: create a new variable "img_contoured" so you don't overwrite anything! 

Arguments:
~~~~~~~~
 * Requires your original image (the one usually named "img")
 * A thresholded image!


Code:
~~~~~~~~

.. code:: python
   import cv2
   from LivestockCV import core as lcv

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')
   s = lcv.rgb2gray_hsv(rgb_img=img, channel='s')
   thresholded = lcv.threshold.binary(gray_img=s, threshold=15, max_value=255, object_type='light')
   lcv.contour_max(img, thresholded)
   lcv.contour(img, thresholded)



Results:
~~~~~~~~

.. figure:: /images/pig.png
Original Raw Image

.. figure:: /images/max_contour.png
Original Raw Image
      

   
