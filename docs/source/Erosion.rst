Erosion
====================

Context:
--------



Arguments:
----------

 * Image path
 * Erosion parameter 1
 * Erosion parameter 2


Code:
-----

.. code:: python

   import cv2
   from LivestockCV import core as lcv

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')


   eroded = lcv.erode(img, 10, 1)
   lcv.show_image(eroded)




Results:
--------

.. figure:: /images/pig.png
   
   **Original Raw Image**
   

.. figure:: /images/erode.png
   
   **Eroded Raw Image**
