Dilation
====================

Context:
--------



Arguments:
----------
 * Image path
 * Dilation parameter 1
 * Dilation parameter 2


Code:
-----

.. code:: python

   import cv2
   from LivestockCV import core as lcv

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')


   dilated = lcv.dilate(img, 10, 1)
   lcv.show_image(dilated)





Results:
--------

.. figure:: /images/pig.png
   
   **Original Raw Image**
   

.. figure:: /images/dilate.png
   
   **Dilated Image**
   

   
