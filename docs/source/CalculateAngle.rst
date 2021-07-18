Calculating Angles
==================




Context:
~~~~~~~~

Finding angles between two lines can be useful when analyzing images of bones, physiological traits, or MRI scans. 
This function requires three coordinates, and can calculate the angle when provided. 
Use this in tandem with the contour functions! 

Arguments:
~~~~~~~~
 * Three coordinates
 


Code:
~~~~~~~~

.. code:: python

   full_circle = LivestockCV_core.CalculateAngle([0,0],[0,0],[0,0])
   flat_line = LivestockCV_core.CalculateAngle([0,0],[0,90],[0,180])
   ninety_degrees = LivestockCV_core.CalculateAngle([0,0],[90,0],[90,90])

   print("Full Circle: ", full_circle)
   print("Flat Line: ", flat_line)
   print("90 Degrees: ", ninety_degrees)


Results:
~~~~~~~~

.. figure:: /images/angles.png
Output
      
      
