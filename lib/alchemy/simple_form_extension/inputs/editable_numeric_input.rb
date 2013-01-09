class EditableNumericInput < EditableBase

  def input
    options = self.options

    options[:class] ||= []
    options[:class].concat(["edit_number"])

    if options[:unlimited]
      options['data-min'] ||= 1
      options[:disabled] = (object.send(attribute_name) == -1)
      options['data-unlimited'] = '-1'
      options[:value] ||= 'Unlimited'
      options.delete(:unlimited)
    end
    
    super
  end

end
