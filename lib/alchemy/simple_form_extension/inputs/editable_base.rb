class EditableBase < SimpleForm::Inputs::Base
  include Rails.application.routes.url_helpers

  def input
    options = self.options

    options[:class] ||= []
    options[:class].concat(["editable_input"])

    options["name"] = "#{object.class.name.underscore}[#{attribute_name}]"
    options["data-url"] = Rails.application.config.action_controller.relative_url_root.to_s + polymorphic_path(object)

    value = options[:value] ? options[:value] : object.send(attribute_name)
    value = value.blank? ? _("Click to edit") : value
    options.delete(:value)
    options.delete(:as)

    template.content_tag :div, options do
      value
    end
  end

end
