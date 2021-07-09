Plot Image
=======

Context:
--------

The first step to every image analysis problem is importing your image.

.. admonition:: Take advantage of Google Collab! 
One of the advantages of using Google Collab is that the code is separated into individual blocks that we can run independently of the others. 
This allows us to easily output an image at any step of our code, and check to see exactly what we're doing at each step. 


Arguments:
----------
Requires a path to your image.
.. admonition:: Watch where you're going!
Since I am using Google Collab, I use a path within my Google Drive. Check the tab on "Basics of Google Collab" for more information. 



Code:
-----

import cv2
from LivestockCV import core as LivestockCV_core

img = cv2.imread('/content/drive/MyDrive/pig.jpg')
print('  ')
print('                           Original Raw Image')
** LivestockCV_core.plot_image(img) **



Results:
--------

.. figure:: /images/pig.png
   
   *Original Raw Image*
   
