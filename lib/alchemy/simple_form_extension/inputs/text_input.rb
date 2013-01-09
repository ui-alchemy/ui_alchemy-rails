class TextInput < SimpleForm::Inputs::TextInput

  def input
    if !input_html_options[:size]
      input_html_options[:size] = "40x8"
    end

    super
  end

end
