"""
Encapsulates algorithms such as FIND-S and LIST-THEN-ELIMINATE into respective classes

Created on Sun Apr  9 22:49:04 2023

@author: Pradip Kumar Das
"""

import pandas as pd
import itertools

class FindS():
    """
    Finds specific hypothesis against positive training examples
    """
        
    def train(self, X, target):
        """
        Implements Find-S algorithm for concept learning over the given training data and returns the specific hypothesis

        Attributes
        ----------
        X: dataframe
            instances of training examples
        target: series
            the label against each instance

        Returns
        --------
        list
            Specific hypothesis
        """
        
        # Let's set the hypothesis with the most specific one
        self.h = ['Φ', 'Φ', 'Φ', 'Φ', 'Φ', 'Φ']

        # Iterates through all exampples and tries to generatize from most specific
        for idx, x in X.iterrows():            
            if target[idx] == "No":     # Skips negative examples
                continue
            
            x.reset_index(drop=True, inplace=True)  # Resets existing index
            for i, attr in enumerate(x):            # Enumerates each attribute of example
                if self.h[i] == 'Φ':
                    self.h[i] = attr
                elif self.h[i] != attr:
                    self.h[i] = '?'
    
class ListThenEliminate():
    """
    From all possible hypotheses space, finds Vector Space containing hypotheses 
    each of which is consistent with all the training examples
    """
        
    def train(self, X, target):
        """
        Attributes
        ----------
        X : DataFrame
            Training examples with all attributes (except target concept)
        
        target: Series
            Target concept of training examples in X

        Returns
        --------
        list
            A Vector Space consisting hypotheses each of which is consistent of
            all the training examples in X
        """
        
        self.__unique_attributes = [list(li) for li in list(X.apply(pd.Series.unique))]
        for li in self.__unique_attributes:
            li.append('?')
            li.append('Φ')
        self.__H = list(itertools.product(*self.__unique_attributes))
        
        # Vector Space containg hypotheses each consistent of all the training examples
        self.VectorSpace = []
        
        for h in self.__H:
            if self.__is_consistent(h, (X, target)) == True:
                self.VectorSpace.append(h)
    
    def __is_consistent(self, h, D):
        """
        Checks if the hypothesis h is consistent with all the training exampes in D
        
        Attributes
        -----------
            h: list
                Hypothesis to test against D
            D: tuple
                A tuple of all training example with attributes (X: DataFrame) and their repstive concepts (c: Series)
            
        Returns
        --------
            True if hyposthesis is consistent with training examples in D, or False otherwise
        """
        
        for idx, x in D[0].iterrows():
            self.__prediction = self.__predict(h, x)
            if self.__prediction == True and D[1][idx] == False:
                return False
            if self.__prediction == False and D[1][idx] == True:
                return False
                    
        return True
    
    def __predict(self, h, x):
        """
        Predicts instance x to be positive or negative against hypothesis h
        
        Atributes
        ----------
            h: list
                Hypothesis to predict against
            x: list
                Instance to predict for
            
        Returns
        --------
            bool
                True if the hypothesis h predicts the instance positive, or False otherwise
            
        """
        
        for i, attr in enumerate(x):
            if h[i] == 'Φ':
                return False
            if h[i] == '?':
                continue
            if h[i] != x[i]:
                return False
            
        return True