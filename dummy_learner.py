from concept import Concept
from learner import Learner


"""
a dummy class to implement a learner that will not do any 
learning and will the think, everything corresponds to 
the same concept. 
"""
class DummyLearner(Learner):
    pass

    def learn(self, training_set):
        # wir machen gar nichts und bleiben dumm
        pass

    def classify(self, example):
        # weil wir nichts gelernt haben glauben wir, alles sind Stopschilder
        return Concept.Stop
