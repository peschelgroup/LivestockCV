Frame Count
=======

Context:
--------

Working with videos is similar to working with images, since a video is simply a series of images, otherwise known as **frames**. 
One of the first pre-processing steps with video is to count how many frames are in a video.



Arguments:
----------
Requires a path to your video.

Use the following line whenever you need to import a video

.. code:: python

   my_video = cv2.VideoCapture("Path to my Video")


.. Warning::
   Importing video is different from importing images!!  



Code:
-----

.. code:: python

   from LivestockCV import core as LivestockCV_core
   my_video = cv2.VideoCapture("/content/drive/MyDrive/ballvid.mov")
   LivestockCV_core.frame_count(my_video)



Results:
--------

.. code:: python

   785
   
.. Tip::
   Your video will have a different frame count than this!  


