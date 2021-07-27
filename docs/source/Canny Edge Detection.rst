Canny Edge Detection
====================

Context:
--------



Arguments:
----------


Code:
-----

.. code:: python

   import cv2
   from LivestockCV import core as lcv

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')

   canny = lcv.cannyedge_detector(img)
   lcv.show_image(canny)


Results:
--------

.. figure:: /images/pig.png
   
   **Original Raw Image**

.. figure:: /images/canny.png
   
   **Original Raw Image**

   
