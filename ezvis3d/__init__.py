

from ._config import load_js_libs
from ._vis3d import Vis3d


__all__ = ['Vis3d']


load_js_libs()
print('Open console to check js libs were loaded in page')


