module Alchemy
  module TranslationHelper
    # Test for Gettext presence, punt to rails translations otherwise
    if respond_to?(:_)
      include Alchemy::GettextTranslations
    else
      include Alchemy::RailsTranslations
    end

    def get_string(text_key)
      return TRANSLATIONS[text_key]
    end

  end
end
