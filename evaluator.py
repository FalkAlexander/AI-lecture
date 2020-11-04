from concept import Concept
from dummy_learner import DummyLearner
import sys


class Evaluator():
    """
    the percentage (between 0 und 100) of vectors from the data to be used for the test
    """
    test_rate = 40

    def __init__(self, filename):
        vectors = self.__read_data(filename)

        learner = DummyLearner()

        # TODO: folgendes muss zur Evaluierung mehrfach ausgeführt werden
		# Verschiedene Teilmengen finden und Verschiedene Reihenfolgen festlegen,
		# wie oft, das hängt vom gewünschten Vertrauensintervall ab
        # TODO: eine andere Abbruchbedingung verwenden
        while True:
            vectors = self.__mix_data(vectors)
            sets = self.__extract_training_data(vectors)
            learner.learn(sets[0])
            result = self.__evaluate(sets[1], learner)
            self.__eval_result(result)
    
    """Evaluate the reulst from the test for output or furthjer considerations

    Args:
        result (list): a Vector containing 3 values: a) right classification ba used learner, 
            b) lerner could not decide or c) learner found wrong concept
    """
    def __eval_result(self, result):
        # TODO: hier muss mehr Auswertung passieren, insbes: Vertrauensintervalle etc
        print("Learning result: \n correct: %s \n unknown: %s \n wrong: \n" % result[0], result[1], result[2])

    """evaluate the learner with a given test set. 

    Args:
        list (list): The set of test examples containing the correct concept
        learner (Learner): The learner to be tests
    
    Returns:
        res (list): a vector containing the test results: success, unknown, false
    """
    def __evaluate(self, list, learner):
        success = 0;
        unknown = 0;
        fault = 0;

        for fv in list:
            c = learner.classify(fv)
            if c == Concept.Unknown:
                unknown += 1
            elif c == fv.get_concept():
                success += 1
            else:
                fault += 1
        
        res = []
        res.append([0, success])
        res.append([1, unknown])
        res.append([2, fault])
        return res
    
    """
    Args:
        vectors (list): vectors a list of vectors
    
    Returns:
        vectors (list): list containing the same vectors as parameter but (usually) in different order
    """

    def __mix_data(self, vectors):
        # TODO: die Reihenfolge der Elemente zufällig verändern
        return vectors
    
    """Split the set of festure vectors in a set of traing data and a set of test data.
	   For representative results it is essential to mix the order of vectors 
	   before splitting the set

    Args:
        vectors (list): a List fo Feature Vectors we can use for the test

    Returns:
        result (list): a List containt two Lists: first the training data, second the test data they are disjunct subsets of vector 
    """

    def __extract_training_data(self, vectors):
        result = [] # maybe use "from collections import deque" instead, not sure right now
        training_data = [] # maybe use "from collections import deque" instead, not sure right now
        test_data = [] # maybe use "from collections import deque" instead, not sure right now

        cut = int(self.test_rate / 100 * len(vectors)) - 1 # not sure here
        training_data.extend(vectors[0:cut])
        test_data.extend(vectors[cut + 1:len(vectors) - 1])

        result.append(training_data)
        result.append(test_data)

        return result

    """
    Args:
        filename (str): the file with this name should contain a serialized List<FeatureVector> containt all the data
    Returns:
        vectors (list): all the data
    """

    def __read_data(self, filename):
        vectors = None
        try:
            f = open(filename, "r", encoding="utf-8")
            vectors = f.read().split(",")
            f.close()
        except IOError:
            print("Could not read Data from file: %s" % filename)
            sys.exit()
        return vectors


"""run the program with training set provided in file with 
    name given in first parameter
"""

filename = None
if len(sys.argv) <= 1:
    print("No data file provided, using dummy data: DummyData.dat")
    filename = "DummyData.dat"
else:
    filename = sys.argv[1]

Evaluator(filename)
