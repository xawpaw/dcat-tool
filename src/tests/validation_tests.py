# validation tests for json files
import sys
import os
from os.path import abspath, dirname
import unittest
import pyshacl
from rdflib import Graph, URIRef

# setup the schema file
SCHEMATA_DIR  = os.path.join(dirname(abspath( __file__ )) , "../../schemata")
COLLECT_TTL   = os.path.join(SCHEMATA_DIR, "dhs_collect.ttl")

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# TEST_DIR = dirname(abspath(__file__))

import dcat_tool
import easy_workbook
import dhs_ontology

# setup the test files
TESTFILE_1 = os.path.join(os.path.dirname(__file__), 'test-1.json')
TESTFILE_2 = os.path.join(os.path.dirname(__file__), 'test-2.json')
TESTFILE_3 = os.path.join(os.path.dirname(__file__), 'test-3.json')
TESTFILE_4 = os.path.join(os.path.dirname(__file__), 'test-4.json')
TESTFILE_5 = os.path.join(os.path.dirname(__file__), 'test-5.json')
TESTFILE_6 = os.path.join(os.path.dirname(__file__), 'test-6.json')

TESTFILE_7 = os.path.join(os.path.dirname(__file__), 'test_excel-1.xlsx')

# setup the schema graph
s = Graph().parse(COLLECT_TTL)

def validateJSONGraphs(shaclGraph, testGraph):
    #print('inside validate')
    results = pyshacl.validate(
            testGraph,
            shacl_graph=shaclGraph,
            data_graph_format="json-ld",
            shacl_graph_format="ttl",
            inference="rdfs",
            debug=False,
            serialize_report_graph="ttl",
        )
    conforms, report_graph, report_text = results
    return conforms

def validateExcel(excelFile):
    parser, args = dcat_tool.parse_arguments(['--validate_xlsx', excelFile])
    results = dcat_tool.define_args(args)
    return results

class TestDIPValidation(unittest.TestCase):

    def test_1(self):
        d = Graph().parse(TESTFILE_1)
        validate_test_1 = validateJSONGraphs(s,d)
        self.assertTrue(validate_test_1, True)


    def test_2(self):
        d = Graph().parse(TESTFILE_2)
        validate_test_2 = validateJSONGraphs(s,d)
        self.assertTrue(validate_test_2, True)

    def test_3(self):
        d = Graph().parse(TESTFILE_3)
        validate_test_3 = validateJSONGraphs(s,d)
        self.assertTrue(validate_test_3, True)

    def test_4(self):
        d = Graph().parse(TESTFILE_4)
        validate_test_4 = validateJSONGraphs(s,d)
        self.assertTrue(validate_test_4, True)

    def test_5(self):
        d = Graph().parse(TESTFILE_5)
        validate_test_5 = validateJSONGraphs(s,d)
        self.assertTrue(validate_test_5, True)

    def test_6(self):
        d = Graph().parse(TESTFILE_6)
        validate_test_6 = validateJSONGraphs(s,d)
        self.assertTrue(validate_test_6, True)

    def test_7(self):
        validate_test_7 = validateExcel(TESTFILE_7)
        print("result", validate_test_7)
        self.assertTrue(validate_test_7, True)

if __name__ == '__main__':
    unittest.main()