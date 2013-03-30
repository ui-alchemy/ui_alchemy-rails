module UIAlchemyRails::GettextTranslations
  if respond_to?(:_)
    TRANSLATIONS = {
      :noscript                 => _("Javascript must be enabled for this application to work properly."),
      :show_password            => _("Show My Password"),
      :example_logo             => _("Logo"),
      :username                 => _("Username"),
      :password                 => _("Password"),
      :login                    => _("Login"),
      :login_information        => _("Login Information"),
      :remembered_login         => _("I remembered my login credentials."),
      :password_unknown         => _("Password Unknown"),
      :email_address            => _("Email Address"),
      :send_login               => _("Send Login"),
      :return_to_login          => _("Return to log in."),
      :password_unknown_info    => _("Enter your username and email address below and instructions on resetting your password will be sent to you."),
      :reset_password           => _("Reset Password"),
      :username_unknown         => _("Username Unknown"),
      :username_unknown_info    => _("If you do not know your username, please enter your email address below and your username information will be sent to you."),
      :change_password          => _("Change Password"),
      :confirm_password         => _("Confirm Password"),
      :save                     => _("Save"),
      :passwords_match          => _("Passwords match."),
      :passwords_do_not_match   => _("Passwords do not match."),
      :recovery_link            => _("Forgot %{username} or %{password}?")
    }
  end
end
