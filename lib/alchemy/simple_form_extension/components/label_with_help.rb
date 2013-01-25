module SimpleForm
  module Components

    module LabelWithHelp
      def label_with_help
        @label_with_help ||= begin
          label_with_help_content = label

          help_text = options[:help]
          help_text = help_text.is_a?(String) ? help_text : translate(:helps)
          if help_text.present?
            label_with_help_content.insert(0, template.content_tag('i', '?'))
            label_with_help_content.insert(-1, template.content_tag('span', help_text))

            if options[:label_wrapper_html].present?
              options[:label_wrapper_html].merge!(:class => 'help')
            else
              options[:label_wrapper_html] = {:class => 'help'}
            end
          end

          label_with_help_content
        end
      end
    end

  end
end

SimpleForm::Inputs::Base.send(:include, SimpleForm::Components::LabelWithHelp)
