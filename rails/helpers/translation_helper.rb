module ConvergeUi::TranslationHelper
  # Test for Gettext presence, punt to rails translations otherwise
  if respond_to?(:_)
    include ConvergeUi::GettextTranslations
  else
    include ConvergeUi::RailsTranslations
  end

  def get_string(text_key)
    return @@translations[text_key]
  end

end
