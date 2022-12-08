# LAPINE
> Motivation: Adverse drug reactions (ADRs) are a major issue in drug development and clinical pharmacology. As the most of ADRs are caused by unintended activity at off-targets of drugs, the identification of drug targets responsible for ADRs becomes a key process for resolving ADRs. Recently, with the increase in the number of ADR-related data sources, several computational methodologies have been proposed to analyze ADR-protein relations. However, the identification of ADR-related proteins on a large scale with high reliability remains an important challenge.

>Results:  In this paper, we suggest a computational approach, Large-scale ADR related Proteins Identification with Network Embedding (LAPINE). LAPINE combines a novel concept called single-target compound with network embedding techniques to enable a large-scale analysis of relations with ADRs for any proteins in the protein-protein interaction network. We analyzed benchmark datasets to confirm the need for such wide scope of potential target proteins, as well as LAPINE’s capability for high recovery of known ADR-related proteins. Moreover, LAPINE provides more reliable predictions for ADR-related proteins (Value-added positive predictive value = 0.12), compared to a previously proposed method (p < 0.001). Furthermore, two case studies showed that most predictive proteins related to ADRs in LAPINE are supported by several literature evidence. Overall, LAPINE can provide reliable insights into the relationship between ADRs and proteome to understand mechanism of ADRs leading to its prevention.

## Dependencies
- python 2.7 (for embedding.py)
  - Embedding process uses BioNEV [(Yue et al., 2019)](https://academic.oup.com/bioinformatics/article/36/4/1241/5581350)
  - <pre><code>$ pip install git+ https://github.com/xiangyue9607/BioNEV.git</code></pre>
  
- python 3.xx (for other python files)
  - Numpy
  - Pandas
  - scikit-learn


## Usage

1.data_download.py

2.data_reader.py

3.network.py

4.
<pre><code>$ bionev --input './result/network.edgelist' --output './result/emb.txt' --method 'node2vec' --workers 40 --dimension 128 --directed True --p 4 --q 0.5 </code></pre>

5.model.py

## Output
