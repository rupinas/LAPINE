How to use LAPINE
=================


Download data
-------------

1.Run data_download.py
  - Code to download all necessary files from public database
  
Network construction
--------------------

2.Run network.py
  - Code for parsing a network file from a database
  
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
