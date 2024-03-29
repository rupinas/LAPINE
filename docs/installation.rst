Installation
============

LAPINE was developed using Python, and requires a Python environment to run. The entire source code of LAPINE is open to the public on the ``GitHub`` repository.

Enviroments
-----------

Python
''''''

LAPINE needs Python enviroment. 
If you don't have a python environment set up we recommend you to use `Conda <https://docs.conda.io/en/latest/>`_. 
Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux.

- Python : 3.7.2

Packages
''''''''

LAPINE requires the following Python packages and you can install them using ``conda``.

- Numpy : 1.18.5
- Pandas : 1.3.0
- scikit-learn : 0.23.1

.. code-block::

    $ conda install numpy=1.18.5 (example)

BioNEV
''''''
LAPINE uses ``BioNEV`` [1] in embedding process.

You can install Bionev by ``git`` command.

.. code-block::

    $ git clone https://github.com/xiangyue9607/BioNEV.git
    $ cd BioNEV
    $ pip install -e
    
Detailed documnetation about ``BioNEV`` is available at https://github.com/xiangyue9607/BioNEV.


Acquire LAPINE
--------------

You can acquire source code of LAPINE by using git from our github repository at https://github.com/rupinas/LAPINE.

you can easily clone by ``git`` command. No other installation process is required.

.. code-block::

    $ git clone https://github.com/rupinas/LAPINE.git

If you are not familar to ``git`` , you can download `zip file <https://github.com/rupinas/LAPINE/archive/refs/heads/main.zip/>`_ and unzip it to your working directory.

Reference
---------

[1] `Yue, Xiang, et al. "Graph embedding on biomedical networks: methods, applications and evaluations." Bioinformatics 36.4 (2020): 1241-1251. <https://doi.org/10.1093/bioinformatics/btz718/>`_
