module SimpleForm
  module FormButtons
    include Alchemy::TranslationHelper

    def form_buttons(*args, &block)
      template.content_tag :div, :class => "control_group buttons" do
        template.content_tag :div, :class => "input" do
          options = args.extract_options!
          options[:class] = ['btn primary', options[:class]].compact
          args << options

          if cancel = options.delete(:cancel)
            submit(*args, &block) + cancel_button(*args, &block)
          else
            submit(*args, &block)
          end
        end
      end
    end

    def cancel_button(*args, &block)
      options = args.extract_options!
      options[:cancel_button_options] ||= {}
      options[:cancel_button_options][:class] ||= []

      template.content_tag :button, options[:cancel_button_options] do
        get_string(:cancel)
      end
    end

  end
end

SimpleForm::FormBuilder.send :include, SimpleForm::FormButtons
