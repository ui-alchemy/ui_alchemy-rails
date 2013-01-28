var ALCH = ALCH || {};


ALCH.i18n = (function(){
    var strings = {},

        localize = function(data){
            var key;

            for (key in data) {
                if( data.hasOwnProperty(key) ){
                    strings[key] = data[key];
                }
            }
        },
        get_string = function(string) {
            return strings[string];
        };

    return {
        localize        : localize,
        get_string      : get_string,
        strings         : strings
    }

})();
