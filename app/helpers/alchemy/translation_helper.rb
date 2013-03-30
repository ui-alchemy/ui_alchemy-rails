module UIAlchemyRails
  module TranslationHelper
    # Test for Gettext presence, punt to rails translations otherwise
    if respond_to?(:_)
      include UIAlchemyRails::GettextTranslations
    else
      include UIAlchemyRails::RailsTranslations
    end

    def get_string(text_key)
      if respond_to?(:_)
        return _(TRANSLATIONS[text_key])
      else
        return I18n.t TRANSLATIONS[text_key]
      end
    end

  end
end
