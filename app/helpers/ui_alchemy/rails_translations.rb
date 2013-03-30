module UIAlchemy::RailsTranslations
  TRANSLATIONS = {
    :noscript                 => "user_sessions.noscript",
    :username                 => "user_sessions.username",
    :password                 => "user_sessions.password",
    :login                    => "user_sessions.login",
    :recovery_link            => "user_sessions.recovery_link",
    :email_address            => "password_resets.email_address",
    :send_login               => "username_recoveries.recover_usernames",
    :password_unknown         => "password_resets.password_unknown",
    :password_unknown_info    => "password_resets.password_unknown_info",
    :reset_password           => "password_resets.reset_password",
    :username_unknown         => "username_recoveries.username_unknown",
    :username_unknown_info    => "username_recoveries.username_unknown_info",
    :change_password          => "password_resets.change_password",
    :change_password_info     => "password_resets.change_password_info",
    :new_password             => "password_resets.new_password",
    :confirm_password         => "password_resets.confirm_password",
    :passwords_do_not_match   => "user_sessions.passwords_do_not_match"
  }
end
