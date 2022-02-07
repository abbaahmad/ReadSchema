import json

datatypes = {"<class 'int'>":'INTEGER', "<class 'str'>":'STRING', "<class 'float'>": 'NUMBER', 
             "<class 'bool'>":'BOOLEAN', "<class 'dict'>":'OBJECT', 'strArr':'ENUM', 'jsonArr':'ARRAY'}


def parse_dict(key,values):
    '''
        Returns: Dictionary with schema of all values pairs of a given key
        Args:
            + key -> dictionary key
            + values -> corresponding values of key in dictionary
    '''
    data_dict = {}
    data_dict[key] = {"type":datatypes[str(type(values))], "tag":"", "description":"", "properties":{},"required":[]}
    data_dict[key]["properties"] = {k:parse_item(k, v) for k,v in values.items()}
    data_dict[key]["required"] = [k for k in values.keys()]
    return data_dict

def parse_list(key, values):
    '''
    Returns: Dictionary with schema of all content of values list
    Args:
        + key -> dictionary key
        + values -> corresponding values of key in dictionary 
    '''
    if type(values[0]) == dict:
        data_dict = {}
        data_dict[key] = {"type":datatypes['jsonArr'], "tag":"", "description":"", "items":{}, "required":[]}
        data_dict[key]["items"] = {k:parse_item(k,v) for entry in values for k,v in entry.items()}
        data_dict[key]["required"] = list(values[0].keys())
        return data_dict
    return parse_primitives(values[0], datatypes["strArr"])

def parse_primitives(value, strlist=""):
    '''
    Returns: Dictionary with schema of a value
    Args:
        + value -> Given value
        + strlist -> if value is from a list of strings 
    '''
    return {"type":datatypes[str(type(value))] if strlist == "" else strlist, 
            "tag":"", "description":""}

def parse_item(k,v):
    '''
    Returns: Dictionary with schema of all content of value
    Args:
        + k -> dictionary key
        + v -> corresponding value of key in dictionary 
    '''
    if type(v) == dict:
        return parse_dict(k,v)
    elif type(v) == list:
        return parse_list(k,v)
    elif type(v) == int or type(v) == float or type(v) == bool or type(v) == str:
        return parse_primitives(v)

def parse_data(data):
    '''
    Returns: Dictionary with schema of all content of 'message' body
    Args:
        + data -> content of 'message' body from json payload 
    '''
    assert type(data) == dict, "[ERROR] Format of input data {type(data)}. Expected type <dict>"
    message_data = data['message']
    # import pdb; pdb.set_trace()
    data_dict = {key:parse_item(key, value) for key, value in message_data.items()}
    return data_dict

def read_file(filename):
    '''
        Returns: json payload from file
        Args:
            + filename -> JSON filename with data 
    '''
    content = []
    assert filename.endswith('json'), "[ERROR] File should be JSON"
    with open(filename, 'r') as f:
        content = json.load(f)
    return content

