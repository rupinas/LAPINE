#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd

def stitch_flat_to_pubchem(cid):
    assert cid.startswith('CID1')
    return 'CIDm'+cid[4:]

def stitch_stereo_to_pubchem(cid):
    assert cid.startswith('CID0')
    return 'CIDs'+cid[4:]

def sider_reader():
    se_columns = ['stitch_id_flat','stitch_id_stereo','umls_cui_from_label',
                  'meddra_type','umls_cui_from_meddra','side_effect_name']
    sider_raw_df = pd.read_csv('./data/drug_adr.tsv', delimiter='\t', names=se_columns)
    sider_raw_df['stitch_id_flat'] = sider_raw_df['stitch_id_flat'].apply(stitch_flat_to_pubchem)
    sider_raw_df['stitch_id_stereo'] = sider_raw_df['stitch_id_stereo'].apply(stitch_stereo_to_pubchem)

    sider_pt_df = sider_raw_df[sider_raw_df['meddra_type']=='PT']
    drug_flat_set = set(sider_pt_df['stitch_id_flat'])
    
    return sider_pt_df, drug_flat_set

def string_reader(threshold):
    ppi_raw_df = pd.read_csv('./data/protein_protein.txt', delimiter=' ')
    ppi_raw_df = ppi_raw_df[(ppi_raw_df['experiments']>0)|(ppi_raw_df['database']>0)]
    ppi_df = ppi_raw_df[ppi_raw_df['combined_score']>threshold].copy()
    
    ppi_df['protein1'] = ppi_df['protein1'].apply(lambda x: x[5:])
    ppi_df['protein2'] = ppi_df['protein2'].apply(lambda x: x[5:])
    
    protein_set = set(ppi_df['protein1']) | set(ppi_df['protein2'])
    
    return ppi_df, protein_set

def stitch_reader(protein_set, SIDER_drug, threshold):
    cpi_raw_df = pd.read_csv('./data/protein_chemical.tsv', delimiter='\t')
    cpi_raw_df = cpi_raw_df[(cpi_raw_df['experimental']>0)|(cpi_raw_df['database']>0)]
    cpi_df = cpi_raw_df[cpi_raw_df['combined_score']>threshold].copy()

    cpi_df['protein'] = cpi_df['protein'].apply(lambda x: x[5:])
    cpi_df = cpi_df[cpi_df['chemical'].isin(SIDER_drug)]
    
    return cpi_df

