E001F - Getting Started
=======================

In this exercise, you learn about some basic concepts of programming, commonly used tools, and how to write and execute a script. You may come across some important vocabulary that you are not yet familiar with. **We will explore this with modern Fortran (programming language).**

Information
-----------

+----------------------+--------------------------------------------------------+
| Topic                                                                         |
+======================+========================================================+
|**Concepts**          |                                                        |
|                      |   * programme                                          |
|                      |   * compilers                                          |
|                      |   * IDE, code highlighting, terminal emulator          |
|                      |   * data types                                         |
|                      |   * modules (Fortran)                                  |
+----------------------+--------------------------------------------------------+
|**Skills**            |                                                        |
|                      |   * code with only a text editor and terminal emulator |
|                      |   * create, compile and execute a programme            |
|                      |   * declaring parameters and variables                 |
|                      |   * using built-in functions                           |
+----------------------+--------------------------------------------------------+

.. topic:: What to Submit

      Submit your script for the final task of this exercise. The script should be named *[your student number]_e001.[ext]*, where *[ext]* is the file extension. In case of Python, this would be *.py*, for modern Fortran it is *.f90*, etc.











.. code-block:: fortran

    program expr2
    implicit none

    integer :: x  ! comment

    x = (2+3)*5
    print *, x
    end program

The console should have returned *"wow, many print"*. In this case, the input argument was *"wow, many print"*, i.e. the value to be displayed, and the function *print* displayed it.
