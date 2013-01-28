class EditableInput < EditableBase
  include Rails.application.routes.url_helpers

  def input
    options = self.options

    options[:class] ||= []
    options[:class].concat(["edit_field"])
    
    super
  end


end
