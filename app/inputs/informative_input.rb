class InformativeInput < SimpleForm::Inputs::Base

  def input
    if options[:wrapper_html].present?
      options[:wrapper_html].merge!(:class => 'informative')
    else
      options[:wrapper_html] = {:class => 'informative'}
    end

    template.content_tag :span, :class => "value" do
      if options[:text]
        options[:text]
      else
        object.send(attribute_name)
      end
    end
  end

end
