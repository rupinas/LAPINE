How to use LAPINE
=================


Download data
-------------

Run data_downlaod.py in your virtual python environment (above 3.7.2) constructed by ``conda`` to download all necessary files from the public database.

Example:

.. code-block:: console

  (.venv) data_download.py
  
  
Network construction
--------------------

Run network.py to parse a network data from protein-protein interactions from STRING database, and chmemical-protein interactions from STITCH database.

.. code-block:: console

  (.venv) network.py --threshold 700

parameters
**********
- threshold : This parameter determines the threshold for the reliability of information included in STRING and STITCH databases. Only inteactions with a confidence score higher than the parameter is used in the analysis. The range of parameters is from 0 to 1000.


  
Network embedding
-----------------

3.Run the following command in the Bionev environments (python 2.7)
  - <pre><code>$ bionev --input './result/network.edgelist' --output './result/emb.txt' --method 'node2vec' --workers 40 --dimension 128 --directed True --p 4 --q 0.5 </code></pre>
  - Code to generate an embedding of the network

ADR-protein relation prediction
-------------------------------

4.Run model.py
  - Code for predicting the association score between ADRs and proteins
 
Output
------

- The output file predictions.csv contains scores for the associated ADRs (columns) for each protein (row).
- The association score ranges from 0 to 1.
- ADR terms are mapped to Preferred Terms (PTs) suggested by MedDRA, and proteins are mapped to Ensembl protein ID.
- <pre><code>$ADR example : C0000727, C0000731 / Protein example : ENSP00000410269, ENSP00000379364 </code></pre>
