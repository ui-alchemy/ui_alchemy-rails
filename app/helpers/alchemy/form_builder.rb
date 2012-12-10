#
# Copyright 2012 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.


module Alchemy
  class FormBuilder < ActionView::Helpers::FormBuilder
    include Rails.application.routes.url_helpers

    delegate :content_tag, :tag, :to => :@template

    %w(text_field text_area select file_field password_field email_field number_field search_field url_field).each do |m|
      define_method m do |name, *args|
        base(name, *args) { super(name, *args) }
      end
    end

    def field(name, *args, &block)
      base(name, *args, &block)
    end

    def submit(*args)
      options = args.extract_options!
      options.symbolize_keys!
      options[:tabindex] ||= tabindex
      args.push options
      content_tag :div, :class => "btn primary" do
        super
      end
    end

    def select_field(name)

    end

    def multiselect(name)

    end

    def date_field(name)

    end

    def button(name, *args)
      options = args.extract_options!
      options.symbolize_keys!
      args.push options
      content_tag :fieldset, :class => "control_group buttons" do
        content_tag :div, :class => 'input' do
          content_tag :button, :class => "btn primary" do
            content_tag(:i, "", :class => "processing hidden").concat(name)
          end
        end
      end
    end

    def editable_base(name, *args)
      options = args.extract_options!
      options.symbolize_keys!

      content_tag :fieldset, :class => "control_group" do
        @template.concat label_wrapper(options) { field_label(name, options) }
        @template.concat input_wrapper(name, options) { yield if block_given? }
      end

    end

    def editable_text_field(name, *args)
      options[:class] = []
      options[:class].concat(["editable", "edit_panel_element"])

      options["data-value"] = "#{object.class.name.downcase}[#{name}]"
      #options["data-url"]   = Rails.application.config.action_controller.relative_url_root + polymorphic_path(object)

      editable_base(name, *args) do
        content_tag :div, options do
          object.send(name).blank? ? _("Click to edit") : object.send(name)
        end
      end
    end

    def editable_text_area(name, *args)
      options[:class] = []
      options[:class].concat(["editable", "edit_textarea"])

      options[:html] ||= {}
      options["data-value"] = "#{object.class.name.downcase}[#{name}]"
      #options["data-url"]   = Rails.application.config.action_controller.relative_url_root + polymorphic_path(object)

      editable_base(name, *args) do
        content_tag :div, options do
          object.send(name).blank? ? _("Click to edit") : object.send(name)
        end
      end
    end

    def tabindex
      @tabindex ||= @options[:tabindex] || 0
      @tabindex += 1
    end

    private

    def base(name, *args)
      options = args.extract_options!
      options.symbolize_keys!

      options[:tabindex] ||= tabindex
      options[:wrapper] ||= {}

      required = object.class.validators_on(name).any? do|v|
        v.kind_of? ActiveModel::Validations::PresenceValidator
      end

      control_group = { :class => ["control_group"] }
      control_group[:class] << "required" if options[:required]

      content_tag :div, :id => options[:wrapper][:id], :class => control_group[:class] do
        @template.concat label_wrapper(options) { field_label(name, options) }
        @template.concat input_wrapper(name, options) { yield if block_given? }
      end

    end

    def label_wrapper(options)
      content_tag(:div, :class => 'label') { yield }
    end

    def input_wrapper(name, options, include_message=true)
      content_tag :div, :class => 'input' do      
        @template.concat yield
        @template.concat content_tag(:span, content_tag(:ul, ""), :class => "message hidden", 
  'data-message_for' => "#{object.class.name.downcase}[#{name}]") if include_message
      end
    end

    def field_label(name, options)
      label(name, options[:label])
    end

    def objectify_options(options)
      super.except(:label, :label_wrapper, :input_wrapper, :grid, :wrapper)
    end

  end
end
