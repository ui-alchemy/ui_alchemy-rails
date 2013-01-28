module SimpleForm
  module Components
    module Editable

      def editable(name, *args, &block)
        options = args.extract_options!
        options = set_type(options)
        options[:required] = false

        self.input(name, options, &block)
      end

      def set_type(options)
        if options[:as]
          options[:as] = "editable_#{options[:as].to_s}".to_sym
        else
          options[:as] = :editable
        end

        return options
      end

    end
  end
end

SimpleForm::FormBuilder.send :include, SimpleForm::Components::Editable
