class EditableInput < EditableBase
  include Rails.application.routes.url_helpers

  def input
    options = self.options

    options[:class] ||= []
    options[:class].concat(["edit_panel_element"])
    
    super
  end


end
