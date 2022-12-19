How to use LAPINE
=================

All LAPINE code must be run in the Conda virtual environment built during the installation process. However, as an exception, the network embedding process must be executed in the BioNev virtual environment.

Download data
-------------

Run data_downlaod.py in your virtual python environment (above 3.7.2) constructed by ``conda`` to download all necessary files from the public database.

Example:

.. code-block::

  (.venv) python data_download.py
  
  
Network construction
--------------------

Run network.py to parse a network data from protein-protein interactions from STRING database, and chmemical-protein interactions from STITCH database.

.. code-block:: 

  (.venv) python network.py --threshold 700

parameters
**********

- threshold : This parameter determines the threshold for the reliability of information included in STRING and STITCH databases. Only interactions with a confidence score higher than the parameter is used in the analysis. Therefore, a high parameter value means the use of limited high-reliability information only. The range of parameters is from 0 to 1000.


Network embedding
-----------------

Run the following command in the BioNEV environments (python 2.7) to generate the embedding of the constructed network.

.. code-block:: 

  (.venv) conda activate bionev
  (bionev) bionev --input './result/network.edgelist' --output './result/emb.txt' --directed True --method 'node2vec' --dimension 128  --p 4 --q 0.5

parameters
**********
- input : path of input file (do not change)
- output : path of output file (do not change)
- directed : consider network as the directed network (do not change)
- method : name of algorithm for the network embededing. Default vaule 'node2vec' is optimzed by cross-validation
- dimension : the dimensions of embedding for each node. The default is 128 which is optimzed by cross-validation
- p, q : two parameters that control the biased random-walk procedure. A high p-value ensures that the walker is less likely to the visited node. A high q value ensures that the walker is more likely to visit the node which is close to the node walker just passed. The default values of p, q are 4 and 0.5 which is optimzed by cross-validation.

more details are vailable at https://github.com/xiangyue9607/BioNEV

ADR-protein relation prediction
-------------------------------

Run model.py to predict the association score between ADRs and proteins.

.. code-block:: 

  (.venv) python network.py --regularization 0.1 --threshold 700
  
parameters
**********
- regularization : Inverse of regularization strength of logistic regression; must be a positive float
- threshold : This parameter determines the threshold for the reliability of information included in STRING and STITCH databases. (must be the same value used in network.py)

 
Output
------

- The output file predictions.csv contains scores for the associated ADRs (columns) for each protein (row).
- The association score ranges from 0 to 1.
- ADR terms are mapped to Preferred Terms (PTs) suggested by MedDRA, and proteins are mapped to Ensembl protein ID.

.. code-block:: 

  ADR example : C0000727, C0000731 / Protein example : ENSP00000410269, ENSP00000379364
