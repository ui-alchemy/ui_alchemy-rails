$:.push File.expand_path("../lib", __FILE__)

# Maintain your gem's version:
require "alchemy/version"

# Describe your gem and declare its dependencies:
Gem::Specification.new do |s|
  s.name        = "alchemy"
  s.version     = Alchemy::VERSION
  s.authors     = [""]
  s.email       = [""]
  s.homepage    = ""
  s.summary     = ""
  s.description = ""

  s.files = Dir["{app,vendor,lib}/**/*"] + ["LICENSE", "Rakefile", "README.md"]
  s.test_files = Dir["test/**/*"]

  s.add_dependency "rails", '~> 3.2.6'
  s.add_dependency "simple_form", '~> 2.0.3'
  s.add_dependency "compass", '>= 0.11.5'
end
