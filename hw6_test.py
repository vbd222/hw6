from hw6 import *
import hw6, inspect
import unittest, json, numpy as np, pandas as pd
from compare_pandas import *

'''
Required files:
    hw6.py
    compare_pandas.py
    data/
        trump_231005_730am.json
        trump_231006_330pm.json
        biden_231005_730am.json
        biden_231006_330pm.json
    test_data/
        sm.pkl
'''


class TestFns(unittest.TestCase):

    def test_get_sentiment(self):
        params = [
            [0.10482020785051088, 0.23619557126248156],
            [0.039277879055940275, 0.1852053154329358],
            [0.14831412441326233, 0.2387056959278045],
            [0.11372175006366181, 0.18231861786718978],
        ]
        self.assertTrue(compare_lists(params[0],
                                      get_sentiment("data/trump_231005_730am.json")))
        self.assertTrue(compare_lists(params[1],
                                      get_sentiment("data/trump_231006_330pm.json")))
        self.assertTrue(compare_lists(params[2],
                                      get_sentiment("data/biden_231005_730am.json")))
        self.assertTrue(compare_lists(params[3],
                                      get_sentiment("data/biden_231006_330pm.json")))

    def test_get_ct_sentiment_frame(self):
        correct = pd.read_pickle("test_data/sm.pkl")
        self.assertTrue(compare_frames(correct, get_ct_sentiment_frame(), 0.005))
        text = inspect.getsource(get_ct_sentiment_frame)
        self.assertTrue("pkl" not in text)


if __name__ == "__main__":
    test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFns)
    results = unittest.TextTestRunner().run(test)
    print("Correctness score = ",
          str((results.testsRun - len(results.errors) - len(results.failures))
              / results.testsRun * 60) + " / 60")
    hw6.main()
