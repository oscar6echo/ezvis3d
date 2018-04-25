
import json
from IPython.display import HTML, display



JS_LIBS_ONE = json.dumps([
    # 'https://cdnjs.cloudflare.com/ajax/libs/vis/4.7.0/vis.js',
    'https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js'
])

JS_LIBS_ONE_sep = ';'.join(map(lambda x: 'console.log("'+x+'")', json.loads(JS_LIBS_ONE)))+';'

# CSS_LIBS_ONE = 'https://cdnjs.cloudflare.com/ajax/libs/vis/4.7.0/vis.css'
CSS_LIBS_ONE = 'https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css'


JS_LOAD = """<script>
require(%s, function(lib) {
    console.log("The following js libs loaded:");
    %s
    window.vis = jQuery.extend(true, {}, lib);
    console.log('vis js lib accessible as vis');

});
</script>""" % (JS_LIBS_ONE, JS_LIBS_ONE_sep)


def load_js_libs():
	display(HTML(JS_LOAD))



JS_SAVE = [
    'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.17/require.js',
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js',
]


API_DIR = 'api'
SCRIPTS_DIR = 'scripts'

VIS3D_OPTION_FILE = 'ezvis3d_option.json'
VIS3D_METHOD_FILE = 'ezvis3d_method.json'
VIS3D_DATASET_FILE = 'ezvis3d_dataset.json'

NAME = 'Name'
TYPE = 'Type'
DEFAULT = 'Default'
DESCRIPTION = 'Description'


