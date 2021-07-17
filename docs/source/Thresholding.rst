Thresholding
=============




Context:
~~~~~~~~

Often times we might found ourselves needing to make a silhouette of our animal in question. Perhaps we'd like to analyze features of a contour. Maybe we want to hide extraneous details lurking in the background. 
Thresholding is a simplification technique we can apply to images. In the most simplest terms, we first take an RGB image, and convert it to grayscale.
What grayscale conversion does is it transforms the values of all the pixels into a scale of 0-255. By setting a threshold value we can uniformly convert values below our threshold to black. 

.. note::
   Total black is the absence of light, therefore, the pixel value of pitch black is 0. 
   Conversely, 255 is the illumination of pure white. 

Arguments:
~~~~~~~~
 * Requires a path to your image.
 * Requires converting a RGB image to gray scale
 * Requires a thresholding value 

Code:
~~~~~~~~



.. code:: python

   import cv2
   from LivestockCV import core as LivestockCV_core

   img = cv2.imread('/content/drive/MyDrive/pig.jpg')
   print('  ')
   print('                           Original Raw Image')
   LivestockCV_core.plot_image(img)

   s = LivestockCV_core.rgb2gray_hsv(rgb_img=img, channel='s')
   LivestockCV_core.plot_image(s)

   print('Threshold = 255 (Nothing gets through filter)')
   s_thresh_test_high = LivestockCV_core.threshold.binary(gray_img=s, threshold=255, max_value=255, object_type='light')
   LivestockCV_core.plot_image(s_thresh_test_high)
   print('')
   print('')
   print('Threshold = 150')
   s_thresh_test_high = LivestockCV_core.threshold.binary(gray_img=s, threshold=150, max_value=255, object_type='light')
   LivestockCV_core.plot_image(s_thresh_test_high)

   print('')
   print('')
   print('Threshold = 105')
   s_thresh_test_med = LivestockCV_core.threshold.binary(gray_img=s, threshold=105, max_value=255, object_type='light')
   LivestockCV_core.plot_image(s_thresh_test_med)
   print('')
   print('')
   print('Threshold = 35')
   s_thresh_test_low = LivestockCV_core.threshold.binary(gray_img=s, threshold=35, max_value=255, object_type='light')
   LivestockCV_core.plot_image(s_thresh_test_low)
   print('')
   print('')
   print('Threshold = 0')
   s_thresh_test_min = LivestockCV_core.threshold.binary(gray_img=s, threshold=0, max_value=255, object_type='light')
   LivestockCV_core.plot_image(s_thresh_test_min)
   print('')
   print('')
   print('Threshold = 15')
   s_thresh_test_justright = LivestockCV_core.threshold.binary(gray_img=s, threshold=15, max_value=255, object_type='light')
   LivestockCV_core.plot_image(s_thresh_test_justright)



Results:
~~~~~~~~

.. figure:: /images/pig.png
Original Raw Image
      
      
.. figure:: /images/t255.png
Threshold = 255 (Here, every pixel is filtered as black) 


.. figure:: /images/t150.png
Threshold = 150


.. figure:: /images/t105.png
Threshold = 105


.. figure:: /images/t35.png
Threshold = 35
   
   
.. figure:: /images/t15.png
Threshold = 15 (Perfect!)


.. figure:: /images/t0.png
Threshold = 0 (Looks like a threshold of 0 causes some pixelation) 