*******
 Build
*******

Provided are examples of how a project might choose to build and package ConvergeUI to be incorporated as part of a larger project.

==============
 Requirements
==============

We recommend installing *tito* for use when building RPMs.

=================
 Stand-alone RPM
=================

ConvergeUI can be built as a stand-alone RPM that can then be included within a repository for use as part of a larger project either at build or deployment time depending on the requirements and constraints of the project.  

First, clone ConvergeUI

.. code-block:: bash

   git clone http://github.com/Katello/converge-ui.git
   cd converge-ui

In order to build the latest tagged version:

.. code-block:: bash

   tito build


In order to build the current checked out hash:

.. code-block:: bash

   tito build --test --rpm

Look at the end of the *tito* output to find the location of the newly created RPM.

=====================================
 Using ConvergeUI as a Git Submodule
=====================================

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
          fonts/
            converge-ui/ --> ../../vendor/converge-ui/fonts/
        vendor/
          converge-ui/ (this is the submodule checkout)

--------------------------------------------
 RPM BuildRequires when using Git Submodule
--------------------------------------------

When incorporating ConvergeUI via a git submodule, the base project will be set against a particular git hash of ConvergeUI.  In order to incorporate ConvergeUI as a build requires, a ConvergeUI RPM must be generated based off the hash set by the base project.  Assuming a setup similar to the previous section:

.. code-block:: bash

   git clone --recursive <base_project_repository>
   cd <base_project>/vendor/converge-ui
   tito build --test --rpm
   rpm -Uvh /tmp/tito/noarch/converge-ui-devel*.rpm

Now the base project's spec file can be built.
