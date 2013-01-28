var ALCH = ALCH || {};


(function(namespace, $, i18n) {

    namespace.jeditable = function(settings){
        var common_settings = {
                method          :  'PUT',
                cancel          :  $('<button/>', { html : i18n.strings.cancel, type : 'cancel' }),
                submit          :  $('<button/>', { html : i18n.strings.save, 'type' : 'submit', class : "primary" }),
                indicator       :  i18n.strings.saving,
                tooltip         :  i18n.strings.clickToEdit,
                placeholder     :  i18n.strings.clickToEdit,
                cssclass        :  'form control_group',
                onerror         :  function(settings, original, xhr) {
                    original.reset();
                    $(document).trigger('onerror.jeditable', [this, xhr]);
                },
                onblur          : function(){}
            };

        common_settings = $.extend(common_settings, settings);

        $.editable('.edit_field', $.extend(common_settings, 
            {
                type        :  'text',
                width       :  270,                  
                onsuccess   :  function(result, status, xhr) {
                                    $(document).trigger('onsuccess.jeditable', [this]);
                                }
            }
        ));

        $.editable('.edit_textarea', $.extend(common_settings, 
            {
                type            :  'textarea',
                rows            :  8,
                cols            :  36
            }
        ));
       
        $.editable('.edit_select', $.extend(common_settings, 
            {
                type        :  'select',
                data   		:  'collection',
                onsuccess   :  function(result, status, xhr){
                                    var data = element.data('collection');
                                        
                                    data["selected"] = result;
                                    element.html(data[result]);
                                }
            }
        ));

        $.editable('.edit_password', $.extend(common_settings, 
            {
                type        :  'password',
                width       :  270
            }
        ));
        
        $.editable('.edit_number', $.extend(common_settings, {
            method          :  'POST',
            type            :  'number',
            width           :  '35',
            cssclass        :  'form control_group checkbox inline',
            onsuccess       :  function(result, status, xhr){
                    if ($(this).data('unlimited') !== undefined) {
                        if (result === $(this).data('unlimited').toString()){
                            $(this).data('value', result);
                            $(this).html(i18n.strings.unlimited);
                        } else {
                            $(this).data('value', result);
                            $(this).html(result);
                        }
                    } else {
                        $(this).html(result);
                        $(this).data('value', result);
                    }
                }
            }
        ));

        return this;
    };

})(ALCH, jQuery, ALCH.i18n);
