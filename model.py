#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression as LR
from sklearn.multiclass import OneVsRestClassifier as OVRC
from sklearn.preprocessing import MultiLabelBinarizer

from data_reader import*
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--regularization', type=float, default=0.1, help='Inverse of regularization strength; must be a positive float')
parser.add_argument('--threshold', type=int, default=700, help='threshold value for STRING, STITCH database (0~1000); must be the same value used in network.py')
args = parser.parse_args()

print('Start model.py with inverse of regularization strength:', args.regularization)
print('Start model.py with threshold for STRING, STITCH DB:', args.threshold)


def adr_training_data(SIDER_df, cpi_df, protein_set):
    df = SIDER_df.groupby(['stitch_id_flat'])['umls_cui_from_meddra'].apply('|'.join)
    drug_list = list()
    adr_list = list()
    mlb = MultiLabelBinarizer()

    for i, v in df.iteritems():
        drug_list.append(i)
        adr_list.append(v.split('|'))
    
    adr_binarized = mlb.fit_transform(adr_list)
    adr_header = list(mlb.classes_)
    adr_raw_df = pd.DataFrame(adr_binarized, columns = adr_header, index=drug_list)
    
    # drug has target in stitch
    adr_raw_df = adr_raw_df.loc[set(cpi_df[cpi_df['protein'].isin(protein_set)]['chemical']),:]
    # ADR related at least one drug
    adr_df = adr_raw_df.loc[:, adr_raw_df.sum()[adr_raw_df.sum()>=1].index]
    
    return adr_df

def logistic_regression(X, Y, STC):
    assert list(X.index) == list(Y.index)
    
    clf = OVRC(LR(C=args.regularization, solver='lbfgs', max_iter=10000))           
    clf.fit(X, Y)
    
    Y_STC = clf.predict_proba(STC)
    Y_STC_df = pd.DataFrame(Y_STC, index=STC.index, columns =Y.columns)
    
    return Y_STC_df

def prediction():
    SIDER_df, SIDER_drug = sider_reader()
    ppi_df, protein_set = string_reader(args.threshold)
    cpi_df = stitch_reader(protein_set, SIDER_drug, args.threshold)
    
    id_data = np.load('./result/IDdict.npy', allow_pickle='TRUE').item()
    id_dict = {y:x for x,y in id_data.items()}
    
    emb_raw_df = pd.read_csv('./result/emb.txt', delimiter=' ', skiprows = 1, header=None)
    emb_raw_df[0] = emb_raw_df[0].apply(lambda x : id_dict[x])
    emb_raw_df.set_index(0, inplace=True)
    
    adr_df = adr_training_data(SIDER_df, cpi_df, protein_set)
    drug_df = emb_raw_df.loc[adr_df.index,:]
    STC_df = emb_raw_df.loc[protein_set,:]
    
    result_df = logistic_regression(drug_df, adr_df, STC_df)
    result_df.to_csv('./result/prediction.csv')
    
    print('End model.py')

prediction()

