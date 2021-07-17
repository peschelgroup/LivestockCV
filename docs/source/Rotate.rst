Rotate
=============




Context:
~~~~~~~~

If you need to quickly rotate your image x degrees, then use the rotate function


Arguments:
~~~~~~~~
 * Requires a path to your image.
 * An angle to rotate

Code:
~~~~~~~~

.. code:: python
   img = cv2.imread('/content/drive/MyDrive/pig.jpg')

   print('                           Original Raw Image')
   LivestockCV_core.plot_image(img)
   print('                           Rotated 90 Degrees')

   rotated_90 = LivestockCV_core.rotate(img, 90)
   LivestockCV_core.plot_image(rotated_90)
   
   print('                           Rotated 30 Degrees')
   rotated_30 = LivestockCV_core.rotate(img, 30)
   LivestockCV_core.plot_image(rotated_30)



Results:
~~~~~~~~

.. figure:: /images/pig.png
Original Raw Image
      
      
.. figure:: /images/rotate90.png
Rotated 90 Degrees


.. figure:: /images/rotate30.png
Rotated 30 Degrees


