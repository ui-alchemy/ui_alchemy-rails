module UIAlchemy
  class Engine < ::Rails::Engine
    isolate_namespace UIAlchemy

    initializer "ui_alchemy.assets.paths" do |app|
      app.config.assets.paths << "#{self.root}/vendor/assets"
      app.config.assets.paths << "#{self.root}/vendor/assets/ui_alchemy"
    end
  end
end
