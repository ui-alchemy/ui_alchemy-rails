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
CUI.Password = {};

$(document).ready(function() {
    var actions = CUI.Password.Actions($('#save_password'));
    CUI.Password.Events.register(actions);

   ratings =[
        {'minScore': 0,
        'className': 'meterFail',
        'text': i18n.very_weak
        },
        {'minScore': 25,
        'className': 'meterWarn',
        'text': i18n.weak
        },
        {'minScore': 50,
        'className': 'meterGood',
        'text': i18n.good
        },
        {'minScore': 75,
        'className': 'meterExcel',
        'text': i18n.strong
        }
    ];
});

CUI.Password.Events = (function($){
    var register = function(actions) {
            $('#password_field').live('keyup', function(){
                var password        = $('#password_field').val(),
                    confirm         = $('#confirm_field').val(),
                    conflict_tag    = $('#password_conflict');

                actions.verifyPassword(password, confirm, conflict_tag);
            });
            $('#confirm_field').live('keyup', function(){
                var password        = $('#password_field').val(),
                    confirm         = $('#confirm_field').val(),
                    conflict_tag    = $('#password_conflict');

                actions.verifyPassword(password, confirm, conflict_tag);
            });
            $('#save_password').live('click', function(){
                var password = $('#password_field').val();

                actions.changePassword(password);
            });
        };

    return {
        register : register
    }

})(jQuery);


CUI.Password.Actions = function(save_button){
    var resetPassword = false,

        verifyPassword = function(password, confirm, conflict_tag) {
            if( password !== confirm ){
                conflict_tag.removeClass('invisible');
                save_button.addClass("disabled");
            }
            else {
                conflict_tag.addClass('invisible');
                save_button.removeClass("disabled");
            }
        },
        changePassword = function(password) {
            var button = save_button,
                url = button.attr("data-url");

            if( !button.hasClass("disabled") ){
                button.addClass("disabled");

                $.ajax({
                    type: "PUT",
                    url: url,
                    data: { "user":{"password":password}},
                    cache: false,
                    success: function(data, textStatus, xhr) {
                        button.removeClass("disabled");
                        if (resetPassword && xhr.status < 400) {
                            // this is a password reset, so we'll redirect the user to the login page
                            window.location.replace(KT.routes.root_path());
                        }
                    },
                    error: function(e) {
                        button.removeClass('disabled');
                    }
                });
            }
        },
        resettingPassword = function(resetValue) {
            resetPassword = resetValue;
        };

    return {
        verifyPassword: verifyPassword,
        changePassword: changePassword,
        resettingPassword: resettingPassword
    };

};
