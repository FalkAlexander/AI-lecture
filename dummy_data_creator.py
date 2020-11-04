from concept import Concept
from feature_vector import FeatureVector
from dummy_feature_vector import DummyFeatureVector
import traceback
import pickle


class DummyDataCreator():
    filename = "DummyData.dat"

    def __init__(self):
        f = []
        f.append(DummyFeatureVector(4, 2, 1, Concept.Stop))
        f.append(DummyFeatureVector(1, 2, 3, Concept.Stop))
        f.append(DummyFeatureVector(4, 5, 6, Concept.Vorfahrt))
        f.append(DummyFeatureVector(1, 5, 3, Concept.RechtsAbbiegen))
        f.append(DummyFeatureVector(3, 2, 5, Concept.Stop))
        f.append(DummyFeatureVector(5, 2, 1, Concept.LinksAbbiegen))

        res = []
        for fv in f:
            res.append(self.__serialize(fv))
        try:
            f = open(self.filename, "w+", encoding="utf-8")
            f.write(str(res));
            f.close()
        except IOError:
            print("DummyDataCreator: Could not create DummyData.dat")
            traceback.print_exc()
    
    def __serialize(self, dummy_feature_vector):
        serialized = []
        serialized.append(dummy_feature_vector.feature)
        serialized.append(dummy_feature_vector.concept)

        return serialized


DummyDataCreator()
