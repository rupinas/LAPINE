#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import get
import gzip
import shutil

def download(url, file_name):
    with open(file_name,'wb') as file:  
        response = get(url)             
        file.write(response.content)
        
download('http://sideeffects.embl.de/media/download/meddra_all_se.tsv.gz', './data/drug_adr.gz')
download('http://stitch.embl.de/download/protein_chemical.links.detailed.v5.0/9606.protein_chemical.links.detailed.v5.0.tsv.gz', './data/protein_chemical.gz')
download('https://stringdb-static.org/download/protein.links.full.v11.5/9606.protein.links.full.v11.5.txt.gz', './data/protein_protein.gz')

with gzip.open('./data/drug_adr.gz', 'rb') as f_in:
    with open('./data/drug_adr.tsv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
        
with gzip.open('./data/protein_chemical.gz', 'rb') as f_in:
    with open('./data/protein_chemical.tsv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
        
with gzip.open('./data/protein_protein.gz', 'rb') as f_in:
    with open('./data/protein_protein.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

