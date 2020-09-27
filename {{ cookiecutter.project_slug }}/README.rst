{{ "#" * (cookiecutter.project_slug | length) }}
{{ cookiecutter.project_slug }}
{{ "#" * (cookiecutter.project_slug | length) }}

.. contents:: Contents:
    :depth: 3

*****
About
*****

{{ cookiecutter.project_slug }}

.. image:: {{ cookiecutter.project_url }}/badges/master/pipeline.svg
    :target: {{ cookiecutter.project_url }}/-/commits/master
    :alt: pipeline status

.. image:: {{ cookiecutter.project_url }}/badges/master/coverage.svg
    :target: {{ cookiecutter.project_url }}/-/commits/master
    :alt: coverage report

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black code style

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: isort imports

************
Installation
************

To install package locally firstly you need to install these:

#. Python 3.7. You can install it with `pyenv <https://github.com/pyenv/pyenv>`_.
   I suggest also to install `virtualenv plugin <https://github.com/pyenv/pyenv-virtualenv>`_.
#. `Poetry <https://python-poetry.org/docs/basic-usage/>`_ to manage dependencies.

.. code-block:: bash

    pyenv install 3.7.4
    pyenv virtualenv 3.7.4 {{ cookiecutter.project_slug }}
    # in project root directory:
    pyenv local {{ cookiecutter.project_slug }}
    # now virtualenv should be active
    poetry install

*****
Notes
*****

#. To view ``.rst`` format use `restview <https://mg.pov.lt/restview/>`_.

   .. code-block:: bash

    # runs restview in background without creating nohup.out file
    nohup restview README.rst > /dev/null 2>&1 &

#. Use following symbols to create headings:

   * H1 - Part - ``#`` with overline
   * H2 - Chapter - ``*`` with overline
   * H3 - Section - ``=``
   * H4 - Subsection - ``-``
   * H5 - Subsubsection - ``^``
   * H6 - Paragraph - ``"``