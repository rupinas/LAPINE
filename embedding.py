#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m = 'node2vec'
input_file = './result/network.edgelist'
output_file = './result/emb.txt'
get_ipython().system('bionev --input {input_file} --output {output_file} --method {m} --workers 40 --dimension 128 --directed True --p 4 --q 0.5')

