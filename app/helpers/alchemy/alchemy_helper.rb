module Alchemy
  module AlchemyHelper

    def alchemy_form_for(object, *args, &block)
      simple_form_for(object, *args, &block)
    end

  end
end
