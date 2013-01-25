class EditableSelectInput < EditableBase

  def input
    options = self.options

    options[:class] ||= []
    options[:class].concat(["edit_select"])

    if options[:include_blank]
      options[:collection].append('')
    end

    options[:collection]        = options[:collection].merge({ 'selected' => options[:selected][0] })
    options['data-collection']  = options[:collection].to_json
    options[:value]             = options[:selected][1]
    options.delete(:selected)
    options.delete(:collection)
    
    super
  end

end
