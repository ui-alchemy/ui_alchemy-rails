module Alchemy
  module AlchemyHelper

    def alchemy_form_for(object, *args, &block)
      #options[:builder]             = Alchemy::FormBuilder
      #options[:html]                ||= {}
      #options[:html][:url]          = ""#polymorphic_path(object)
      #options[:html][:novalidate]   = true
      #options[:html][:method]       = object.persisted? ? :put : :post
      #options[:html][:class]        = ["form", "messages_bottom"]
      #options[:html][:class]        << 'new_' + object.class.name.downcase  if !object.persisted?
      #options[:html][:class]        << 'edit_' + object.class.name.downcase if object.persisted?
      #options[:html]["data-id"]     = object.id if object.id
      #options[:html]["data-remote"] = true
      simple_form_for(object, *args, &block)
    end

  end
end
