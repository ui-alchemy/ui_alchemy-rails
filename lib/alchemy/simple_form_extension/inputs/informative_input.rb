class InformativeInput < SimpleForm::Inputs::Base

  def input
    if options[:wrapper_html].present?
      options[:wrapper_html].merge!(:class => 'informative')
    else
      options[:wrapper_html] = {:class => 'informative'}
    end

    template.content_tag :span, :class => "value" do
      options[:text]
    end
  end

end
