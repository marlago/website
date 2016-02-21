Demonstrating RST post
<<<<<<<<<<<<<<<<<<<<<<
:date: 2016-2-19

This is a demonstration of "roles" in RST. In order to use a role, you need to declare
it first. Below is a simple role declaration.

.. role:: error

Notice how it's only visible in the RST file, but not in the html output?
That's because it's an RST internal and contributes to the conversion from RST to HTML
without actually getting rendered itself.

This is supposed to demonstrate the capabilities of restructured text when
it comes to blog posts.


3a) The key to the cabinet is on the table.

3b) The key to the **cabinets** is on the table.

3c) \*The key to the cabinet :error:`are` on the table.

3d) \*The key to the **cabinets** are on the table.

Here's another paragraph of text followed by a centered image.

.. figure:: {filename}/images/attraction_joke.png
  :align: center
  :alt: Agree to Disagree

  ..

  Here's a legend

And what about some text after the image, eh?

Sometimes you might want to combine several formatting styles together.
For instance, maybe you want bold text that's also styled like an error, ie. is red.
The definition you use in this case is a bit more complicated, see below.

.. role:: error_demo(strong)
  :class: error

The first thing that's happening here is that your new role **error_demo** is based on the
**strong** role, that gives you the boldface. In the following line you tell RST to apply
the **error** class (which in CSS is configured to turn text red) to anything you label as
**error_demo**. The result is the desired combination of red and bold font!

And here's how it will look in your text.

These errors are called :error_demo:`agreement attraction errors`. And *"cabinets"*, the noun that the verb wrongly agrees with, is called an **attractor**. This name conveys the intuition that *"cabinets"* deceitfully attracts the verb, making it agree with it in number instead of with the "real" subject head, the noun *"key"*. What we don't know though, is why attraction happens in language. What misleads people into making these errors? You might be thinking *"Jeez, it's obvious: "cabinets" is closer to the verb than "key"! Maybe people just produce a verb that agrees with whatever noun is closer to it".* Ok, this is true, but notice that attraction errors occur even when the attractor does not intervene between the verb and its subject: look at the examples above, where the noun *"errors"* triggers attraction despite the fact that *"classification software"* (the real subject) is closer to the verb. So, linear proximity might facilitate attraction, but it cannot be its only cause.


.. container:: ling-ex

  .. class:: ling-ex-number

  (4a)

  .. container:: ling-ex-sent

    The detective works.

    Dedektif çalıştı.


.. container:: ling-ex

  .. class:: ling-ex-number

  (4b)

  .. container:: ling-ex-sent

    The detectives work.

    Dedektifler çalıştılar.


.. container:: ling-ex bad

  .. class:: ling-ex-number

  (4c)

  .. container:: ling-ex-sent

    The detective work.

    Dedektif çalıştılar.


.. container:: ling-ex bad

  .. class:: ling-ex-number

  (4d)

  .. container:: ling-ex-sent

    The detectives works.

    Dedektifler çalıştı.
