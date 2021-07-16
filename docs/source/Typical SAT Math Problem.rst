Typical SAT Math Problem
===============



Not finished yet:
-----------------

Context:
--------

Traditional programming takes rules and data to get answers.

Machine learning however, is taking the answers and data, to give us the rules.

Please read my blog post(?) on "Machine Learning for Animal Scientists"


Here is a typical SAT math problem I remember encountering frequently.
X = -1, 0, 1, 2, 3, 4
Y = -11, -1, 9, 19, 29, 39

Find the formula (f(x) = ____) that satisfies the above.

It doesn't matter what the answer is (Y = 10x - 1) but moreso, how you would have came up with the answer.

You might have noticed that each number was being multiplied by something larger or maybe you took advantage of the zero, but whichever way you did it to figure it out, you had to have checked each number to make sure that the rule was consistent with all the other numbers.

This is how a neural network works. 





.. Tip::
   

Arguments:
----------
Requires:
 * a short snippet of code
 

Code:
-----

Lets take a look at this line of code:

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

We have inputted two parameters (each 1) at units and input_shape. This is the simplest neural network as it has only ONE layer. This layer has ONE neuron. Therefore, the input shape is just ONE.

The next step is to "compile" our neural network. When we do we specify two functions: a loss and an optimizer.

Lets talk about what the loss and optimizer is used for. When we were trying to figure out what the secret formula was, if you were like me, you probably threw in a bad guess just to see what kind of math we were dealing with. Like, "y = x + 1" The LOSS function is what measures how right the formula was, and giving us a percentage error.

But lets say for your second subconcious guess you thought it was y = x - 1. You wouldn't be wrong with that zero since for that instance your formula was technically right. Thats where the optimizer comes in. It'll take your second guess and be like "omg this was right for something- lets keep it". It'll then just continue this loop of random guessues until it finds one that beats the current one. By the end of the number of loops you specificy (which is called epochs) it'll spit out its best result. But you'll find that things don't always work the way you want. Also, there are tons of different kinds of optimizers and LOSS functions that are used for different purposes.


.. code:: python

   import tensorflow as tf
   from tensorflow import keras
   import numpy as np

   # numpy helps us represent data as lists :) 
   model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
   model.compile(optimizer='sgd', loss='mean_squared_error')
   xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
   ys = np.array([-11, -1, 9, 19, 29, 39], dtype=float)
   model.fit(xs, ys, epochs=5)
   print(model.predict([10.0]))

.. Warning::
   Why isn't the answer exactly 99.0?
Results:
--------

TBD

