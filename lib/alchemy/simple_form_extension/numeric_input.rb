class NumericInput < SimpleForm::Inputs::NumericInput

  def input
    if options[:unlimited]
      numeric_value = object.attributes[attribute_name.to_s]
      check_box_name = input_html_options[:id] || 'unlimited_quantity'
    
      input_html_options[:min] ||= 1
      input_html_options[:disabled] = !numeric_value.present? || numeric_value == -1
      input_html_options[:placeholder] = "\u221E"
      input_html = super

      if options[:wrapper_html].present?
        options[:wrapper_html].merge!(:class => 'checkbox inline')
      else
        options[:wrapper_html] = { :class => 'checkbox inline' }
      end

      input_html += template.content_tag(:div, :class => 'control') do
        template.check_box_tag(check_box_name, 1, !numeric_value.present? || numeric_value == -1) +
          template.label_tag(check_box_name, _("Unlimited"), :class => 'control_label')
      end
    else
      super
    end
  end

end
