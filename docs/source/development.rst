============
Development
============

-----------
Repository
-----------

The upstream ConvergeUI repository is hosted on Github: https://github.com/ehelms/converge-ui

--------
Process
--------

The ConvergeUI project supports the pull request method for supplying updates and new features.

---------------------------------------------------
Using ConvergeUI as a Git Submodule in Development
---------------------------------------------------

Given that ConvergeUI is a set of assets, and that your project, in production mode, will want to combine stylesheets and javascript into concatenated files that are then minified and compressed, treating ConvergeUI as a development dependency naturally makes sense.  This can easily be accomplished by adding ConvergeUI as a git submodule into your repository and establishing symlinks where appropriate.  This allows you to configure and use the assets in ConvergeUI in a flexible way, tailored to your projects needs and layout.

In your project root:

.. code-block:: bash

   git submodule add git@github.com:Katello/converge-ui.git vendor/converge-ui
   git submodule update --init

Now that the submodule has been added as part of your git config, and been initialized, the various assets can be linked up via symlinks to the proper areas.  For example, a Rails 3.0 application might symlink in the following way:

.. code-block:: bash

   my-app/
      src/
        app/
          stylesheets/
            converge-ui/ --> ../../vendor/converge-ui/stylesheets/
          views/
            layouts/
              converge-ui/ --> ../../../vendor/converge-ui/rails/layouts/
        public/
          javascripts/
            converge-ui/ --> ../../vendor/converge-ui/javascripts/
          images/
            converge-ui/ --> ../../vendor/converge-ui/images/
        vendor/
          converge-ui/ (this is the submodule checkout)
