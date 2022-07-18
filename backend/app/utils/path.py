import json
import os
from definitions import ROOT_DIR

def read_root_json(name:str):
    FILE_PATH = os.path.join(ROOT_DIR,name)
    return json.loads(open(FILE_PATH).read())