#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:09:23 2023

@author: Pradip Kumar Das
"""

import numpy as np

class Node:
    def __init__(self):
        self.value = ""
        self.children = []
        self.entropy = 0.0
        self.sample_count = 0
        self.isLeaf = False
        self.prediction = ""

class ID3DecisionTreeClassifier:
    """
    Iterative Dichotomiser 3 (ID3) algorithm based Decision Tree classifier
    
    """
    def entropy(self, data, target_attrib_name):
        """
        Measures the impurity in a collection of examples
        
        Parameters
        ----------
        data: DataFrame
            Data set to compute the entropy against
            
        target_attrib_name: str
            Target attribute of the data set
            
        Returns
        -------
            float
                Entropy of the data set with respect to target attribute
        """

        entropy = 0.0                   # Initializes entropy
        examples_count = data.shape[0]  # Observation count in data set

        # Sums entropy for each unique value in target attribute
        for target_value in data[target_attrib_name].unique():
            filtered_examples_count = data[data[target_attrib_name] == target_value].shape[0]     
            entropy += -filtered_examples_count/examples_count * np.log2(filtered_examples_count/examples_count)

        return entropy
        
    def info_gain(self, data, attrib_name, target_attrib_name):
        """
        Measures the reduction in entropy caused by partitioning the examples by specified attribute
        """

        # Gets entropy of the data set with respect to target attribute
        entropy = self.entropy(data, target_attrib_name)

        sum_entropy_subsets = 0
        for attrib_val in data[attrib_name].unique():
            data_subset = data[data[attrib_name] == attrib_val]
            sum_entropy_subsets += data_subset.shape[0]/data.shape[0] * self.entropy(data_subset, target_attrib_name)

        # Returns the reduction of entropy
        return entropy - sum_entropy_subsets

    def fit(self, data, target_attrib_name):
        """
        Fits the classifier to the data

        Parameters
        ----------
        data : DataFrame
            Data set to fit the model against.
        target_attrib_name : str
            Target attribute of the data set.

        Returns
        -------
            None.

        """
        
        # Gets decision tree
        self.__tree = self.__ID3(
            data,                                                                   # the data set
            [attrib for attrib in data.columns if attrib != target_attrib_name],    # Attributes except the target
            target_attrib_name)                                                     # Target attribute of the data set
    
    def __ID3(self, data, attrib_names, target_attrib_name):
        """
        Creates ID3 based decision tree out of data, attributes and target

        Parameters
        ----------
        data : DataFrame
            Data set to create decision tree out of.
        attrib_names : List
            List of attributes of the data set to consider.
        target_attrib_name : str
            Target attribute of the data set.

        Returns
        -------
        root : Node
            Decision tree.

        """
        
        # Creates node and sets basic information such as entroy and sample count in each node
        root = Node()
        root.entropy = self.entropy(data, target_attrib_name)
        root.sample_count = data.shape[0]
        
        # If entropy is zero, then marks the node leaf and sets prediction
        if root.entropy == 0.0:
            root.isLeaf = True
            root.prediction = data[target_attrib_name].unique()
            return root
        
        # If entroy is not zero, then finds the best best attribute to split the data set into
        
        best_info_gain = 0.0
        best_attrib = ""
        
        for attrib_name in attrib_names:
            info_gain = self.info_gain(data, attrib_name, target_attrib_name)
            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_attrib = attrib_name
                
        # Best attribute name is set as node value and child nodes each representing split
        # from the best attribute are created
        
        root.value = best_attrib  # Best attribute on which node splits is set in node property
        
        attrib_unique_values = data[best_attrib].unique()
        for attrib_unique_value in attrib_unique_values:
            data_subset = data[data[best_attrib] == attrib_unique_value]
            new_attrib_names = attrib_names.copy()
            new_attrib_names.remove(best_attrib)
            
            # Each item in children list is tuple consisting attribute value (representing node edge) and the child node
            root.children.append({attrib_unique_value: self.__ID3(data_subset, new_attrib_names, target_attrib_name)})

        return root
    
    def predict(self, data):
        """
        Predicts the target of the input data

        Parameters
        ----------
        data : dict
            Data sample consisting of collection of pair of attribute and its value.

        Returns
        -------
        array
            The prediction.

        """
        return self.__predict(self.__tree, data)
    
    def __predict(self, root: Node, data):
        """
        Predicts the target of the input data

        Parameters
        ----------
        root : Node
            The decision tree.
        data : dict
            Data sample consisting of collection of pair of attribute and its value.

        Returns
        -------
        array
            The prediction.

        """
        
        # For leaf node, prediction is returned from its prediction property
        if root.isLeaf == True:
            return root.prediction
        # for non-leaf node, it finds node against attribute and 
        # its value and gets prediction through that child node
        else:
            for child in root.children:
                if list(child.keys())[0] == data[root.value]:
                    return self.__predict(list(child.values())[0], data)

    def print_tree(self, offset = 0):
        """
        Prints the decision tree

        Parameters
        ----------
        offset : int, optional
            Horizontal offset from left from which the decision tree starts printing its root an child node(s). The default is 0.

        Returns
        -------
        None.

        """
        self.__print_tree(self.__tree, offset)
        print("\nLEGENDS:")
        print("e: entropy, s: sample count, p: prediction")
            
    def __print_tree(self, root: Node, offset = 0):
        """
        Prints the decision tree

        Parameters
        ----------
        root : Node
            The decision tree.
        offset : int, optional
            Horizontal offset from left from which the decision tree starts printing its root an child node(s). The default is 0.

        Returns
        -------
        None.

        """
        
        # Prints tabs as offset from left
        for i in range(offset):
            print("\t", end="")
            
        # For leaf node, node properties including prediction are printed
        if root.isLeaf == True:
            print("('LEAF') [e: {:.2f}, s: {}, p: {}]".format(root.entropy, root.sample_count, root.prediction))
        
        # For non-leaf node, both edge (attribute value) and child node are printed using recursion
        else:
            print("({}) [e: {:.2f}, s: {}]".format(root.value, root.entropy, root.sample_count), end="")
            print()
            for child in root.children:
                for i in range(offset + 1):
                    print("\t", end="")
                print(list(child.keys())[0])                            # prints edge
                self.__print_tree(list(child.values())[0], offset + 2)  # prints child node