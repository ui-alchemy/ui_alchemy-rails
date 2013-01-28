$.editable.custom_inputs = (function($){

    $.editable.addInputType('select', {
       element : function(settings, original) {
            var select = $('<select />');
            $(this).append(select);
            return(select);
        },
        content : function(data, settings, original) {
            var json = data,
                key;

            for (key in json) {
                if (json.hasOwnProperty(key)) {
                    if ('selected' == key) {
                        continue;
                    } 
                    var option = $('<option />').val(key).append(json[key]);
                    $('select', this).append(option);
                }
            }
                    
            /* Loop option again to set selected. IE needed this... */ 
            $('select', this).children().each(function() {
                if ($(this).val() == json['selected'] || 
                    $(this).text() == $.trim(original.revert)) {
                        $(this).attr('selected', 'selected');
                }
            });
        }
    });

    $.editable.addInputType('number', {
       element  :   function(settings, original){
            var width       = settings.width ? settings.width : '40px',
                $original   = $(original),
                input       = jQuery('<input type="number" ' +
                                    'min="' + $original.data('min') + '"' +
                                    'max="' + $original.data('max') + '"' + 
                                    'value="" style="width:' + width + 'px;">');

            $(this).append(input);
            if ($original.data('unlimited') !== undefined) {
                var label = jQuery('<div class="control"><input type="checkbox" value=""/><label class="control_label">' + i18n.unlimited + '</label></div>');
                $(this).append(label);
                var unlimited = label.find("input");
                $(unlimited).bind('click', function(){
                    if($(unlimited).is(":checked")){
                        $(input).val('');
                        $(input).attr("placeholder", "\u221E");
                        $(input).attr("disabled", true);
                    } else {
                        $(input).val(1);
                        $(input).removeAttr('disabled');
                    }
                });
            }
            return(input);    
       },

        content : function(string, settings, original) {
            var text_input = $('input', this).first();

            text_input.val(string);
            if ($(original).data('unlimited') == $(original).data('value')) {
                var check_input = $('input', this).last();
                if (string === settings.unlimited || string === i18n.unlimited) {
                    text_input.val('');
                    check_input.attr('checked', 'checked');
                    text_input.attr("disabled", true);
                } else {
                    check_input.removeAttr('checked');
                    text_input.removeAttr('disabled');
                }
            } else {
                text_input.val($(original).data('value'));
            }
        },

        submit  : function(settings, original) {
            var $original = $(original);

            if( $original.data('unlimited') !== undefined ) {
                var text_input = $('input', this).first();
                if (text_input.val() === '') {
                    text_input.val($original.data('unlimited'));
                }
            }
        },
    });

    $.editable.addInputType('password', {
        element : function(settings, original) {
            var input=$('<input type="password">');
            if(settings.width!='none') {
                input.width(settings.width);
            }
            if(settings.height!='none') {
                input.height(settings.height);
            }
            input.attr('autocomplete','off');
            $(this).append(input);
            return(input);
        }
    });

    // Create a custom input type for checkboxes
    $.editable.addInputType("checkbox", {
        element : function(settings, original) {
            var input = $('<input type="checkbox">');
            $(this).append(input);

            // Update <input>'s value when clicked
            $(input).click(function() {
                //var value = $(input).attr("checked") ? i18n.checkbox_yes : i18n.checkbox_no;
                var value = $(input).attr("checked") ? true : false;
                $(input).val(value);
            });
            return(input);
        },
        content : function(string, settings, original) {
            var checked = string.indexOf(i18n.checkbox_yes)!= -1 ? 1 : 0;
            var input = $(':input:first', this);
            $(input).attr("checked", checked);
            var value = $(input).attr("checked") ? i18n.checkbox_yes : i18n.checkbox_no;
            //var value = $(input).attr("checked") ? true : false;

            $(input).val(value);
        }
    });

})(jQuery);
