class EditableInformativeInput < EditableBase

  def input
    options = self.options

    options[:class] ||= []

    
    template.content_tag :span, :class => "value" do
      options[:text]
    end
  end

end
