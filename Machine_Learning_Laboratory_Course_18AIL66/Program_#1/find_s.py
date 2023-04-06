# Encapsulate the above algorithm into

class FindS():
    def train(X, target):
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
        h = ['Φ', 'Φ', 'Φ', 'Φ', 'Φ', 'Φ']

        for idx, x in X.iterrows():
            if target[idx] == "No":
                continue
            x.reset_index(drop=True, inplace=True)
            for i, attr in enumerate(x):
                if h[i] == 'Φ':
                    h[i] = attr
                elif h[i] != attr:
                    h[i] = '?'
        return h
    