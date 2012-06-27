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
 
    $('#password_link').click(function(){
        $('#password_recovery_container').animate({ 'left' : '0px' }, 'slow').css('z-index', 1);
    });
    $('#username_link').click(function(){
        $('#username_recovery_container').animate({ 'left' : '0px' }, 'slow').css('z-index', 1);
    });
    $('#password_return_link').click(function(){
        $('#password_recovery_container').animate({ 'left' : '-360px' }, 'slow', function(){
            $(this).css('z-index', -1);
        });
    });
    $('#username_return_link').click(function(){
        $('#username_recovery_container').animate({ 'left' : '-360px' }, 'slow', function(){
            $(this).css('z-index', -1);
        });
    });
    $('#login_btn').click(function(){
      CUI.Login.Actions.toggleSpinner();
    });
});

CUI.Login.Actions = (function($){
    var show_password = function(input_field, input_reveal_field, show){
            var password;

            if( show ){
                password = input_field.val();
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
        },
        org_switcher_animation = function(){
          $('#org_switcher').trigger({type:'login'});
        },
        toggleSpinner = function(){
          $('#login_form .spinner').fadeToggle('fast');
        };


    return {
        show_password   : show_password,
        add_hash_input  : add_hash_input,
        org_switcher_animation : org_switcher_animation,
        toggleSpinner : toggleSpinner
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
            //if you have an #org_switcher container for an interstitial, this will function. otherwise it won't.
            // this is for converge-ui
            var switcher = $('#org_switcher');
            if (switcher.length){
              $('#org_switcher').bind('login', function(event){
                CUI.Login.Actions.toggleSpinner();
                switcher.animate({ 'left' : '0px' }, 'slow').css('z-index', 1);
              });
            }
        };
    return {
        register    : register
    }

})(jQuery, CUI.Login.Actions);
