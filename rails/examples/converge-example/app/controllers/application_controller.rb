class ApplicationController < ActionController::Base
  include FastGettext::Translation

  protect_from_forgery
  before_filter :set_locale

  def set_locale
    FastGettext.available_locales = ['en']
    FastGettext.text_domain = 'app'
    session[:locale] = I18n.locale = FastGettext.set_locale(params[:locale] || session[:locale] || request.env['HTTP_ACCEPT_LANGUAGE'] || 'en')
  end
  
end
