import unittest 
from plots import parseQuery

class TestCases(unittest.TestCase):    
    def test_valid_query(self):
        features,relations = parseQuery("plot price per carat")
        expected_features = {'Carat': 15, 'Amount': 5}
        expected_relations = {'ratio': 11}
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)

    def test_invalid_query(self):
        features,relations = parseQuery("Hello how are you ?")
        expected_features = {}
        expected_relations = {}
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)
    def test_empty_query(self):
        features,relations = parseQuery("")
        expected_features = {}
        expected_relations = {}
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)

    def test_ratio_plot(self):
        features,relations = parseQuery("plot price per carat")
        expected_features = {'Carat': 15, 'Amount': 5}
        expected_relations = {'ratio': 11}
        expected_val = 'ratio'
        val = ''
        for key in  relations.keys():
            val = key
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)
        self.assertEqual(val,expected_val)

    def test_scatter_plot(self):
        features,relations = parseQuery("show correlation between total depth and stone weight")
        expected_features = {'Carat': 41, 'Total Depth': 25}
        val = ''
        for key in  relations.keys():
            val = key
        expected_relations ={'scatter': 5}
        expected_val = "scatter"
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)
        self.assertEqual(val,expected_val)
    def test_histogram_plot(self):
        features,relations = parseQuery("show spread of stone id")
        expected_features = {'Stone ID': 15}
        expected_relations ={'histogram': 5}
        val = ''
        for key in  relations.keys():
            val = key
        expected_val = "histogram"
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)
        self.assertEqual(val,expected_val)
    def test_line_plot(self):
        features,relations = parseQuery("compare total cost vs relative depth")
        expected_features = {'Amount': 8, 'Total Depth': 22}
        expected_relations ={'line plot': 19}
        val = ''
        for key in  relations.keys():
            val = key
        expected_val = "line plot"
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)
        self.assertEqual(val,expected_val)
    
    def test_no_relation(self):
        features,relations = parseQuery("show plote of stone id")
        expected_features = {'Stone ID': 14}
        expected_relations ={}
        val = ''
        for key in  relations.keys():
            val = key
        expected_val = ""
        self.assertEqual(features,expected_features)
        self.assertEqual(relations,expected_relations)
        self.assertEqual(val,expected_val)

    def test_single_feature(self):
        features,relations = parseQuery("show distribution of relative depth")
        expected_features = {'Total Depth': 21}
        self.assertEqual(features,expected_features)

    def test_more_than_two_features(self):
        features,relations = parseQuery("show plot between relative depth total price and stone weight")
        expected_features = {'Carat': 49, 'Amount': 39, 'Total Depth': 18}
        self.assertEqual(expected_features,features)
    def test_more_than_one_relations(self):
        features,relations = parseQuery("show distribution and correlation between stone weight and price")
        expected_features = {'Carat': 42, 'Amount': 59}
        expected_relations = {'histogram': 5, 'scatter': 22}
        self.assertEqual(expected_features,features)
        self.assertEqual(expected_relations,relations)

    def test_more_feature_more_relations(self):
        features,relations = parseQuery("show distribution and correlation between stone weight and price and total depth")
        expected_features = {'Carat': 42, 'Amount': 59, 'Total Depth': 69}
        expected_relations = {'histogram': 5, 'scatter': 22}
        self.assertEqual(expected_features,features)
        self.assertEqual(expected_relations,relations)

if __name__ == '__main__':
    unittest.main()
