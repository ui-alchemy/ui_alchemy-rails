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
var CUI = CUI ? CUI : {};
CUI.Login = {};

$(document).ready(function() {

    CUI.Login.Events.register();
    
});

CUI.Login.Actions = (function($){
    var show_password = function(input_field, input_reveal_field, show){
            var password;

            if( show ){
                password = input_field.val()
                input_field.hide();
                input_reveal_field.val(password).show();
            } else {
                password = input_reveal_field.val();
                input_reveal_field.hide();
                input_field.val(password).show();
            }
        },
        add_hash_input = function(parent){
            if (window.location.hash != "") {
                $('<input>').attr({
                    type: 'hidden',
                    id: 'hash_anchor',
                    name: 'hash_anchor',
                    value: window.location.hash
                }).appendTo(parent);
            }
        };

    return {
        show_password   : show_password,
        add_hash_input  : add_hash_input
    };

})(jQuery);

CUI.Login.Events = (function($, actions){
    var register = function(){
            $('#reveal').change(function(){
                actions.show_password($('#password-input'), $('#password-input-reveal'), $(this).is(':checked'));
            });
            $('#login_form').live('submit', function(e) {
                actions.add_hash_input(this);
            });
        };

    return {
        register    : register
    }

})(jQuery, CUI.Login.Actions);
