############
Cookiecutter
############

.. contents:: Contents:
    :depth: 3

*****
About
*****

Проект, чтобы быстро создать python проект по шаблону с помощью `cookiecutter
<https://github.com/cookiecutter/cookiecutter>`_.

Docs: `<https://cookiecutter.readthedocs.io/en/latest/>`_.

*****
Usage
*****

First you need cookiecutter to be installed:

.. code-block:: bash

    pip install --user cookiecutter

You have 2 options:

#. Create project from vcs repository:

   .. code-block:: bash

        cookiecutter https://gitlab.com/artslob/cookiecutter-python

#. Or you can use the already cloned project by path:

   .. code-block:: bash

        git clone https://gitlab.com/artslob/cookiecutter-python
        cookiecutter cookiecutter-python

***********
Development
***********

.. code-block:: bash

    # create project from template in output dir
    cookiecutter -f --no-input -o output/ .


*****
Notes
*****

#. Use following symbols to create headings:

   * H1 - Part - ``#`` with overline
   * H2 - Chapter - ``*`` with overline
   * H3 - Section - ``=``
   * H4 - Subsection - ``-``
   * H5 - Subsubsection - ``^``
   * H6 - Paragraph - ``"``
