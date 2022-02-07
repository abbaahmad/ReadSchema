import unittest

from GetSchema import parse_data, parse_dict, parse_item, parse_list, parse_primitives

test_data_1= {
    "name":"hello", 
    "age":100,
    "message":{"msg1": "Functions returns appropriately",
                "msg2":["Or", "maybe", "not"]}, 
    "temp":100
}
test_data_2 = ("key",100.0)

test_dict_data = ("message",{"key1": "Functions returns appropriately",
                "key2":100.0})

test_list_data = ("message", [{"msg1": "Functions returns appropriately",
                "msg2":["Or", "maybe", "not"]}]   
)
test_primitive = 100

output_1 = {"msg1":{"type": "STRING", "tag":"", "description":""}, "msg2":{"type":"ENUM", "tag":"", "description":""}}
output_2 = {"type": "NUMBER", "tag":"", "description":""}
output_test_dict = {"message":{"type":"OBJECT", "tag":"", "description":"", 
                    "properties":{"key1":{"type": "STRING", "tag":"", "description":""},
                                  "key2":{"type":"NUMBER", "tag":"", "description":""}},
                    "required":["key1", "key2"]}
                }
output_test_list = {"message":{"type":"ARRAY", "tag":"", "description":"", 
                    "items":{"msg1":{"type": "STRING", "tag":"", "description":""},
                             "msg2":{"type":"ENUM", "tag":"", "description":""}},
                    "required":["msg1", "msg2"]}
                }
output_test_primitive = {"type": "INTEGER", "tag":"", "description":""}


class TestMethods(unittest.TestCase):
    def read_file(self, filename):
        self.testdata = open(filename).readlines()

    def test_parse_data(self):
        assert parse_data(test_data_1) == output_1

    def test_parse_item(self):
        assert parse_item(test_data_2[0], test_data_2[1]) == output_2

    def test_parse_dict(self):
        assert parse_dict(test_dict_data[0], test_dict_data[1]) == output_test_dict

    def test_parse_list(self):
        assert parse_list(test_list_data[0], test_list_data[1]) == output_test_list
    
    def test_parse_primitives(self):
        assert parse_primitives(test_primitive) == output_test_primitive

if __name__ == "__main__":
    unittest.main()