
import os
import pandas as pd
import datetime as dt
import uuid
from IPython.display import HTML


from _config import JS_LIBS_ONE, CSS_LIBS_ONE, JS_SAVE
from scripts import JS_JSON_PARSE_OPTION, JS_JSON_PARSE_DATA




def html(data, options, center=False, save=False):
    """
    save=True will create a standalone HTML doc under localdir/saved (creating folfer save if necessary)
    center=True will center the plot in the output cell, otherwise left-aligned by default.
    """
    
    def json_dumps(obj):
        return pd.io.json.dumps(obj)

    _options = dict(options)
    _data = data

    def clean_function_str(key, n=10):
        """
        Remove new line characters in the first say 10 characters
        of the value corresponding to key in dictionary _options.
        This value is a string that potentially starts with
        'function' or ' function' or '[newline]function' or '[newline]function', etc
        This cleaning makes js string parsing easier to recognize functions.
        """
        if key in _options.keys():
            new_str = _options[key][:n].replace('\n', '').replace('\r', '') + _options[key][n:]
            _options[key] = new_str


    clean_function_str('tooltip') 
    clean_function_str('xValueLabel') 
    clean_function_str('yValueLabel') 
    clean_function_str('zValueLabel') 


    chart_id = str(uuid.uuid4()).replace('-', '_')


    js_init = """
    var options = %s;
    %s
    window.opt = jQuery.extend(true, {}, options);
    console.log('vis3d options accessible as opt');
    
    var data = %s;
    %s
    window.dta = jQuery.extend(true, [], data);
    console.log('vis3d data accessible as dta');
    """ % (json_dumps(_options), JS_JSON_PARSE_OPTION,
           json_dumps(_data), JS_JSON_PARSE_DATA) 

    
    js_call = """
    var container = document.getElementById('%s');
    console.log(options);
    console.log(data);
    graph3d = new vis.Graph3d(container, data, options);
    """ % (chart_id)



    if center:
        if not 'width' in _options.keys():
            # Explicitly sets width to default value
            _options['width'] = '400px'

        html = """
        <div id="%s" style="margin: auto; width: %s;"></div>
        """ % (chart_id, _options['width'])
    else:
        html = """
        <div id="%s"></div>
        """ % (chart_id)


    css = """
    <link href="%s" rel="stylesheet" type="text/css" />
    """ % (CSS_LIBS_ONE)


    js = """<script>
    require(%s, function(lib) {
        window.vis = jQuery.extend(true, {}, lib);
        %s
        %s
    });
    </script>""" % (JS_LIBS_ONE, js_init, js_call)
    
    if save==True:
        if not os.path.exists('saved'):
            os.makedirs('saved')
        with open(os.path.join('saved', 'plot_'+dt.datetime.now().strftime('%Y%m%d_%H%M%S')+'.html'), 'w') as f:
            contents = """
            <script src="%s"></script>
            <script src="%s"></script>
            %s
            """ % (JS_SAVE[0], JS_SAVE[1], html+js)
            f.write(contents)
    
    return html+css+js

    



def plot(data, options, center=False, save=False):
    contents = html(data, options, center, save)
    return HTML(contents)

  

