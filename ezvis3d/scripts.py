

JS_JSON_PARSE_OPTION = """
var options = JSON.stringify(options);

var options = JSON.parse(options, function(key, value) {

    if (value && (typeof value==="string")) {

        if (value.substr(0,8) == "function") {
            var startBody = value.indexOf('{') + 1;
            var endBody = value.lastIndexOf('}');
            var startArgs = value.indexOf('(') + 1;
            var endArgs = value.indexOf(')');

            return new Function(value.substring(startArgs, endArgs),
                                value.substring(startBody, endBody));
        }


        if (value.substr(0,9)=="(function") {
            var startBody = value.indexOf('{') + 1;
            var endBody = value.lastIndexOf('}');
            var startArgs = value.indexOf('(', 1) + 1;
            var endArgs = value.indexOf(')');

            var func = new Function(value.substring(startArgs, endArgs),
                                    value.substring(startBody, endBody));
            return func();
        }
    }

    return value;
});
"""


JS_JSON_PARSE_DATA = """
var data = JSON.parse(data);
"""

JS_CREATE_DATASET = """
var dataset = new vis.DataSet();
e = data[0];
if (e.style!==undefined & e.filter!==undefined) {
    for (var i=0; i<data.length; i++) {
        dataset.add( {x: data[i].x, y: data[i].y, z: data[i].z, style: data[i].style, filter: data[i].filter});    
    }
}
else if (e.style!==undefined & e.filter===undefined) {
    for (var i=0; i<data.length; i++) {
        dataset.add( {x: data[i].x, y: data[i].y, z: data[i].z, style: data[i].style});    
    }
}
else if (e.style===undefined & e.filter!==undefined) {
    for (var i=0; i<data.length; i++) {
        dataset.add( {x: data[i].x, y: data[i].y, z: data[i].z, filter: data[i].filter});    
    }
}
else if (e.style===undefined & e.filter===undefined) {
    for (var i=0; i<data.length; i++) {
        dataset.add( {x: data[i].x, y: data[i].y, z: data[i].z});    
    }
}
"""