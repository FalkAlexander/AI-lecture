from concept import Concept
from feature_vector import FeatureVector
import array as arr


class DummyFeatureVector(FeatureVector):
    concept = Concept(1)
    feature = NotImplemented

    def __init__(self, a, b, c, d):
        self.feature = arr.array("i", [a, b, c]) # usage of a dictionary would be much more generic here, not sure though if its a good idea
        self.concept = d
    
    def get_concept(self):
        return self.concept
    
    def get_num_features(self):
        return 3
    
    def get_feature_value(self, i):
        return feature[i]
