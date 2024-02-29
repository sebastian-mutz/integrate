Dictionary
==========

This page contains a glossary of terms you often come across in the world of programming. It is subdivided into general terminology and more Python specific terminology. There are different ways, in which some of these terms are used. This course uses the definitions below.

Programming 
-----------

* **Array** - a collection of variables or values. (In Python, this includes lists, tuples and dictionaries.)
* **Class** - a code template for creating objects; it consists of object attribute variables and methods (functions).
* **Comparison Operator** - allows you to compare a value to another reference value to examine their relation. These include:

    +------------------------+--------------------------------------------------------+
    | Operator               | Meaning                                                | 
    +========================+========================================================+
    | `==`                   | equal to                                               |  
    +------------------------+--------------------------------------------------------+  
    | `!=`                   | not equal to                                           |  
    +------------------------+--------------------------------------------------------+    
    | `<`                    | less than                                              | 
    +------------------------+--------------------------------------------------------+
    | `<=`                   | less than or equal to                                  |
    +------------------------+--------------------------------------------------------+
    | `>`                    | greater than                                           |
    +------------------------+--------------------------------------------------------+
    | `>=`                   | greater than or equal to                               |
    +------------------------+--------------------------------------------------------+

* **Console (Interface)** - command line interface; allows user to issue successive text commands to the computer, which are interpreted by the shell/terminal emulator, which handle the interface.
* **Data Types** - are categories for data, which specify which type of value a variable can take. These include:

    +------------------------+--------------------------------------------------------+---------------------------------+
    | Data Type              | Explanation                                            | Examples                        |
    +========================+========================================================+=================================+
    | Integer                | whole numbers                                          | 42, 451                         |
    +------------------------+--------------------------------------------------------+---------------------------------+  
    | Float                  | (floating point) numbers with decimal points           | 20.77, 19.84, 2.312             |
    +------------------------+--------------------------------------------------------+---------------------------------+  
    | Boolean                | representing the two values of boolean logic           | True, False                     |
    +------------------------+--------------------------------------------------------+---------------------------------+  
    | String                 | alphanumeric characters                                | *dogge*, *system_shock_2019*    |
    +------------------------+--------------------------------------------------------+---------------------------------+  

* **Function** - a flexible unit/section of code performing a specific task. Functions typically take one or several input arguments and return a value that is the result of performing the task under conditions set by the input arguments. Here, we use it synonymously for procedure and (sub)routine. 
* **IDE** - Integrated Development Environment; software that includes necessary tools for a programmer, incl. a source code editor (text editor), debugger and console.
* **Index Number** - the location of a specific value stored in a vector, matrix or tensor variable. (The first index value is always *0 for Python*, but can also be 1 for languages like Fortan.)
* **Library** - a collection (or package) of functions/routines that a programme can use, a set of modules.
* **Module** - part of a programme (a component) that contains one or several functions/routines. Several modules may be combined into one library.
* **Object** - a class instance, a combination of (object attribute) variables, functions and data.
* **Programme** - collection of instructions for the computer; code is compiled.
* **Script** - programme written for a specific run-time environment; code is interpreted. (Python script files have the *.py* file extension, Matlab scripts have the *.m* file extension).
* **Terminal Emulator** - or shell; software allowing access to command line/console interfaces and text user interfaces.
* **Variable** - like a mathematical variable, it stores values and has a specific name (anything from *x* to *u_wot_m8*). It can hold values for very different data types (see data types). 

Python
------

* **Dictionary** - an *unordered, indexed, changeable* array that can store any type of data values (integers, strings, etc.); You can define a list using curly brackets, e.g.::

    dictionaryName = {'place':'EARTH','year':2160}

* **List** - an *ordered, changeable* array that can store any type of data values (integers, strings, etc.); You can define a list using square brackets, e.g.::

    listName = ['E', 'A', 'R', 'T', 'H', 2, 1, 5, 0]
    
* **Tuple** - an *ordered, unchangeable* array that can store any type of data values (integers, strings, etc.); You can define a list using rounded brackets, e.g.::

    tupleName = ('E', 'A', 'R', 'T', 'H', 2, 1, 4, 0)

* **Anaconda** - a Python distribution, including Spyder IDE, numpy and matplotlib. 
    
* **matplotlib** - a 2D Python plotting library.
    
* **numPy** - a standard Python package for linear algebra and other important elements of scientific computing.

* **Spyder** - an integrated development environment (IDE) for Python.
