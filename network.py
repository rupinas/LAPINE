#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import csv

from data_reader import*


# In[2]:


def network_construction():
    SIDER_df, SIDER_drug = sider_reader()
    ppi_df, protein_set = string_reader()
    cpi_df = stitch_reader(protein_set, SIDER_drug)

    id_dict = dict(); current_id = 0
    with open('./result/network.edgelist', 'w') as result:
        for i, row in ppi_df.iterrows():
            protein1 = 'REAL_'+row['protein1']
            protein2 = 'REAL_'+row['protein2']

            if protein1 not in id_dict: 
                id_dict[protein1] = current_id
                current_id += 1

            if protein2 not in id_dict: 
                id_dict[protein2] = current_id
                current_id += 1

            protein1_id = str(id_dict[protein1])
            protein2_id = str(id_dict[protein2])

            result.write(protein1_id+' '+protein2_id+'\n')
            result.write(protein2_id+' '+protein1_id+'\n')

        for i, row in cpi_df.iterrows():
            if row['protein'] not in protein_set: continue 
            protein = 'REAL_'+row['protein']
            drug = row['chemical']

            if protein not in id_dict: 
                id_dict[protein] = current_id
                current_id += 1

            if drug not in id_dict: 
                id_dict[drug] = current_id
                current_id += 1

            protein_id = str(id_dict[protein])
            drug_id = str(id_dict[drug])


            result.write(drug_id+' '+protein_id+'\n')

        for protein in (protein_set): 
            STD = protein
            protein = 'REAL_'+protein

            if STD not in id_dict: 
                id_dict[STD] = current_id
                current_id += 1

            protein_id = str(id_dict[protein])
            STD_id = str(id_dict[STD])

            result.write(STD_id+' '+protein_id+'\n')

    np.save('./result/IDdict.npy', id_dict)


# In[3]:


network_construction()

