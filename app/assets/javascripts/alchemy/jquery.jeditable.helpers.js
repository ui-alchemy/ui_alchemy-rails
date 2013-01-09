/**
 Copyright 2011 Red Hat, Inc.

 This software is licensed to you under the GNU General Public
 License as published by the Free Software Foundation; either version
 2 of the License (GPLv2) or (at your option) any later version.
 There is NO WARRANTY for this software, express or implied,
 including the implied warranties of MERCHANTABILITY,
 NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
 have received a copy of GPLv2 along with this software; if not, see
 http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
*/

/**
 * Helper functions that may be included and used from pages using
 * inline editing via jeditable.
 */
$(document).ready(function() {
    var common_settings = {
            method          :  'PUT',
            cancel          :  $('<button/>', { html : i18n.cancel }),
            submit          :  $('<button/>', { html : i18n.save, 'type' : 'submit', class : "primary" }),
            indicator       :  i18n.saving,
            tooltip         :  i18n.clickToEdit,
            placeholder     :  i18n.clickToEdit,
            cssclass        :  'form control_group',
            submitdata      :  $.extend({ authenticity_token: AUTH_TOKEN }, KT.common.getSearchParams()),
            onerror         :  function(settings, original, xhr) {
                original.reset();
                $("#notification").replaceWith(xhr.responseText);
                notices.checkNotices();
            },
            onblur          : function(){}
        };

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
            var width = settings.width ? settings.width : '40',
                input = jQuery('<input type="number" ' +
                                'min="' + settings.min + '"' +
                                'max="' + settings.max + '"' + 
                                'value="' + settings.value + 
                                '" style="width:' + width + 'px;">');

            $(this).append(input);
            if (settings.unlimited !== undefined) {
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
            $(original).css('background-image', 'none');
            return(input);    
       },

        content : function(string, settings, original) {
            var text_input = $('input', this).first();

            text_input.val(string);
            if (settings.unlimited !== undefined) {
                var check_input = $('input', this).last();
                if (string === settings.unlimited || string === i18n.unlimited) {
                    text_input.val('');
                    check_input.attr('checked', 'checked');
                    text_input.attr("disabled", true);
                } else {
                    check_input.removeAttr('checked');
                    text_input.removeAttr('disabled');
                }
            }
        },

        submit  : function(settings, original) {
            if (settings.unlimited != undefined) {
                var text_input = $('input', this).first();
                if (text_input.val() === '')
                    text_input.val(settings.unlimited);
            }
        },
    });

    $('.ajaxfileupload').each(function() {
        $(this).editable($(this).attr('url'), {
            type        :  'ajaxupload',
            method      :  'PUT',
            name        :  $(this).attr('name'),
            cancel      :  i18n.cancel,
            submit      :  i18n.upload,
            indicator   :  i18n.uploading,
            tooltip     :  i18n.clickToEdit,
            placeholder :  i18n.clickToEdit,
            submitdata  :  {authenticity_token: AUTH_TOKEN},
            onerror     :  function(settings, original, xhr) {
            original.reset();
                $("#notification").replaceWith(xhr.responseText);
            }
        });
    });

    $('.edit_panel_element').each(function() {
        var settings = {
            type        :  'text',
            width       :  270,
            name        :  $(this).attr('name'),
            onsuccess   :  function(result, status, xhr) {
                var id = $('#panel_element_id');
                KT.panel.list.refresh(id.attr('value'), id.attr('data-ajax_url'));
            }
        };
        $(this).editable($(this).attr('data-url'), $.extend(common_settings, settings));
    });

    $('.edit_password').each(function() {
        var settings = {
            type        :  'password',
            width       :  270,
            name        :  $(this).attr('name')
        };
        $(this).editable($(this).attr('data-url'), $.extend(common_settings, settings));
    });

    $('.edit_textfield').each(function() {
        var settings = {
            type        :  'text',
            width       :  270,                  
            name        :  $(this).attr('name')
        };
        $(this).editable($(this).attr('data-url'), $.extend(common_settings, settings));
    });

    $('.edit_textarea').each(function() {
        var settings = { 
                type            :  'textarea',
                name            :  $(this).attr('name'),
                rows            :  8,
                cols            :  36
        }; 
        $(this).editable($(this).attr('data-url'), $.extend(common_settings, settings)); 
    });
   
   	$('.edit_select').each(function(){
   		var element = $(this);
   		var settings = { 
            type            :  'select',
            name            :  element.attr('name'),
            data   			:  element.data('collection'),
            onsuccess       :  function(result, status, xhr){
            	var data = element.data('collection');
            	
            	data["selected"] = result;
            	element.html(data[result]);
            }
        };
        $(this).editable($(this).attr('data-url'), $.extend(common_settings, settings));
  	});
    
    $('.edit_number').each(function() {
        var element = $(this);
        var settings = {
            method          :  'POST',
            data            :  '',
            type            :  'number',
            value           :  $.trim($(this).html()),
            height          :  10,           
            width           :  35,       
            onblur          :  'ignore',
            cssclass        :  'form control_group checkbox inline',
            name            :  $(this).attr('name'),
            min             :  $(this).data('min'),
            max             :  $(this).data('max'),
            unlimited       :  $(this).data('unlimited'),
            image           :  $(this).css('background-image'),
            submitdata      :  {authenticity_token: AUTH_TOKEN},
            onsuccess       :  function(result, status, xhr){
                element.css('background-image', settings.image);
                if ($(this).data('unlimited') !== undefined) {
                    if (result === $(this).data('unlimited').toString()){
                        element.html(i18n.unlimited);
                    } else {
                        element.html(result);
                    }
                } else {
                    element.html(result);
                }
            },
            onresetcomplete : function(settings, original){
                element.css('background-image', settings.image);
            }
        };
        element.editable(element.attr('data-url'), $.extend(common_settings, settings));
    });
});
