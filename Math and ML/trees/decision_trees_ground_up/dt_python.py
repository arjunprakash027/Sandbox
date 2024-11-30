'''
Author : Arjun Prakash
Description : A simple Binary decision tree implementation in python
Date Written: 30/11/24
Last Edited: 30/11/24
'''

import pandas as pd
import numpy as np
from typing import List, Union



def construct_dataset() -> pd.DataFrame:
    '''
    Information about the dataset:

    Dataset has 5 columns -> 4 features and 1 target
    Target variable (idx 0) consists of 3 classes L (balance scale tip to left), R (Balance scale tip to right) and B (Rightly balanced)
    And then there are left weight left distance (idx 1 and 2) and right weight rightt distance (idx 3 and 4)
    There are no missing values and the distribution of target variable is 46% for L and R and 8% for B
    '''

    balance_data = pd.read_csv(
            'https://archive.ics.uci.edu/ml/machine-learning-' +
            'databases/balance-scale/balance-scale.data',
            sep=',', header=None)

    
    print("Dataset Shape: ", balance_data.shape)

    return balance_data

def get_tree_entropy (tree:pd.DataFrame, target: str | int) -> float:

    total_entropy = 0
    #getting the probablity of each target value and finding its entropy    
    target_values = np.unique(tree[target].values.tolist())

    for value in target_values:
        prob = (len(tree[tree[target] == value]) / len(tree[target]))
        entropy = - (prob * np.log(prob))
        total_entropy += entropy
        
    return total_entropy

def calculate_entropy(df:pd.DataFrame, feature: str | int, split_val: float, target: str | int) -> float:
    
    #splitting the tree into left and right and finding the entropy for each of the tree seperately and combining it to get total entropy of the split
    print(f"Split val : {split_val}")
    left_tree = df[df[feature] < split_val]
    right_tree = df[df[feature] >= split_val]

    left_weight = (len(left_tree) / len(df))
    right_weight = (len(right_tree) / len(df))

    left_entropy = get_tree_entropy(tree=left_tree, target=target)
    right_entropy = get_tree_entropy(tree=right_tree, target=target)
    
    print(f"Entropy for left split is {left_entropy} and right is {right_entropy}")

    weighted_entropy = (left_weight * left_entropy) + (right_weight * right_entropy)
    
    return weighted_entropy

def build_tree(df:pd.DataFrame, feature_list:List, target: str) -> None:
    print(f"Column List: {feature_list} <-> Target: {target}")

    current_node = {
        "feature" : None,
        "value" : None,
        "entropy" : np.inf
    }

    #Looping through each of the features to find the feature with best split
    for feature in feature_list:

        #sort the values and get the median value between each positions
        sorted_values = np.unique(df[feature].sort_values().tolist()) #using pd,unique to get unique values to avoid repeated calculations
        
        #find the split values
        split_values = [
            (sorted_values[i - 1] + sorted_values[i]) / 2
             for i in range (1, len(sorted_values))
        ]

        #find the impurity of each split
        for split_val in split_values:
            entropy = calculate_entropy(df=df, feature=feature, split_val=split_val, target=target)
            print(f"Total Entropy for split at {split_val} of {feature} is {entropy}")
        
            if entropy < current_node['entropy']:

                current_node['feature'] = feature
                current_node['value'] = split_val
                current_node['entropy'] = entropy
        
    return current_node


def main() -> None:

    df = construct_dataset()

    # we will ignore the balanced scale for now as I am trying to code only for binary problem
    df = df[df[0] != 'B']
    
    #encoding the string is binary is very important 
    df[0] = df[0].apply(lambda value: 1 if value == 'L' else 0)

    #build feature list and target var
    target = 0
    feature_list = df.columns.tolist()
    feature_list.remove(0)

    best_node = build_tree(df,feature_list=feature_list,target=target)

    print(f"Best node for split is {best_node}")



#running the program
main()
