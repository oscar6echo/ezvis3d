
import os
import json
from ._config import VIS3D_OPTION_FILE, VIS3D_METHOD_FILE, VIS3D_DATASET_FILE, \
                    API_DIR


def load_resource(src):
    _dir = os.path.dirname(__file__)
    object_builder_file = os.path.join(_dir, API_DIR, src)
    with open(object_builder_file, encoding='UTF-8') as obj_build:
        return json.load(obj_build)


class State(object):
    """
    Contains all 'ezvis3d' API, options and methods
    """

    def __init__(self):
        self._OPTION = load_resource(VIS3D_OPTION_FILE)
        self._METHOD = load_resource(VIS3D_METHOD_FILE)
        self._DATASET = load_resource(VIS3D_DATASET_FILE)

state_VIS3D = State()

