class Learner():
    """The training method, that changes the internal state of the learner 
    such that it will classify examples of a similar set (i.e. the testSet better.

    Args:
        training_set (list): trainingSet contains feature vectors and corresponding concepts
            to provide experience to learn from
    """
    def learn(self, training_set):
        pass

    """find the concept of the example from the internal knowledge 
    of the lerner this method must not consider example.getConcept() at all!!

    Args:
        example (FeatureVector): is a feature vector

    Returns:
        concept: the concept of the examplke as learned by this before
    """
    def classify(self, example):
        pass
