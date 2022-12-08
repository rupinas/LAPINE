# LAPINE
> Motivation: Adverse drug reactions (ADRs) are a major issue in drug development and clinical pharmacology. As the most of ADRs are caused by unintended activity at off-targets of drugs, the identification of drug targets responsible for ADRs becomes a key process for resolving ADRs. Recently, with the increase in the number of ADR-related data sources, several computational methodologies have been proposed to analyze ADR-protein relations. However, the identification of ADR-related proteins on a large scale with high reliability remains an important challenge.

>Results:  In this paper, we suggest a computational approach, Large-scale ADR related Proteins Identification with Network Embedding (LAPINE). LAPINE combines a novel concept called single-target compound with network embedding techniques to enable a large-scale analysis of relations with ADRs for any proteins in the protein-protein interaction network. We analyzed benchmark datasets to confirm the need for such wide scope of potential target proteins, as well as LAPINE’s capability for high recovery of known ADR-related proteins. Moreover, LAPINE provides more reliable predictions for ADR-related proteins (Value-added positive predictive value = 0.12), compared to a previously proposed method (p < 0.001). Furthermore, two case studies showed that most predictive proteins related to ADRs in LAPINE are supported by several literature evidence. Overall, LAPINE can provide reliable insights into the relationship between ADRs and proteome to understand mechanism of ADRs leading to its prevention.

## Dependencies
- python 2.7 (for embedding.py)
  - Embedding process uses BioNEV [(Yue et al., 2019)](https://academic.oup.com/bioinformatics/article/36/4/1241/5581350)
  - <pre><code>$ pip install git+ https://github.com/xiangyue9607/BioNEV.git</code></pre>
  
- python 3.xx (for other python files)
  - Numpy : 1.18.5
  - Pandas : 1.3.0
  - scikit-learn : 0.23.1

## Usage

1.Run data_download.py
  - Code to download all necessary files from public database
2.Run network.py
  - Code for parsing a network file from a database

3.Run the following command in the Bionev environments (python 2.7)
  - <pre><code>$ bionev --input './result/network.edgelist' --output './result/emb.txt' --method 'node2vec' --workers 40 --dimension 128 --directed True --p 4 --q 0.5 </code></pre>
  - Code to generate an embedding of the network

4.Run model.py
  - Code for predicting the association score between ADRs and proteins
 
## Output
- The output file predictions.csv contains scores for the associated ADRs (columns) for each protein (row).
- The association score ranges from 0 to 1.
- ADR terms are mapped to Preferred Terms (PTs) suggested by MedDRA, and proteins are mapped to Ensembl protein ID.
- <pre><code>$ADR example : C0000727, C0000731 / Protein example : ENSP00000410269, ENSP00000379364 </code></pre>

## License
-  LAPINE is licensed under the MIT License.
