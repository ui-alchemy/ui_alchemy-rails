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

    $('#password_link').click(function(e){
        e.preventDefault();
        $('.card#password_reset').animate({ 'left' : '0px' }, 'slow').css('z-index', 1);
    });
    $('#username_link').click(function(e){
        e.preventDefault();
        $('.card#username_recovery').animate({ 'left' : '0px' }, 'slow').css('z-index', 1);
    });
    $('#password_reset_return_link').click(function(e){
        e.preventDefault();
        $('.card#password_reset').animate({ 'left' : '-360px' }, 'slow', function(){
            $(this).css('z-index', -1);
        });
    });
    $('#username_recovery_return_link').click(function(e){
        e.preventDefault();
        $('.card#username_recovery').animate({ 'left' : '-360px' }, 'slow', function(){
            $(this).css('z-index', -1);
        });
    });
    $('#login_btn').click(function(){
      CUI.Login.Actions.toggleSpinner();
    });
    $(document).bind("ajax:complete",
          function(evt, data, status, xhr){
            if(status == "success") {
              $('form .spinner').fadeOut('fast');
            }
          }
    );
    $('#username').focus();
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
        interstitial_switcher_animation = function(num_orgs, redir_path){
          if(parseInt(num_orgs, 10) > 1){
            $('#interstitial').trigger({type:'login'});
          } else if(redir_path){
            CUI.Login.Actions.toggleSpinner();
            window.location.href = redir_path;
          } else {
            window.location.reload();
          }
        },
        toggleSpinner = function(){
          $('#login_form .spinner').fadeToggle('fast');
        },
        redirecter = function(url){
          if ($.browser.msie){
            window.location = url;
          } else {
            window.location.href = url;
          }
        };

    return {
        show_password   : show_password,
        add_hash_input  : add_hash_input,
        interstitial_switcher_animation : interstitial_switcher_animation,
        redirecter : redirecter,
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
            //if you have an #interstitial container for an interstitial, this will function. otherwise it won't.
            // this is for alchemy
            var interstitial = $('#interstitial');
            if (interstitial.length){
              $('#interstitial').bind('login', function(event){
                CUI.Login.Actions.toggleSpinner();
                interstitial.animate({ 'left' : '0px' }, 'slow').css('z-index', 1);
              });
            }
        };
    return {
        register    : register
    }

})(jQuery, CUI.Login.Actions);
