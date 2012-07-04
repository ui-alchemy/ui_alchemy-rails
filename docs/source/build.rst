======
Build
======

Provided are examples of how a project might choose to build and package ConvergeUI to be incorporated as part of a larger project.

-------------
Requirements
-------------

We recommend installing *tito* for use when building RPMs.

-------------------
Stand-alone RPM
-------------------

ConvergeUI can be built as a stand-alone RPM that can then be included within a repository for use as part of a larger project either at build or deployment time depending on the requirements and constraints of the project.  

First, clone ConvergeUI.

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


-------------------------------------------
RPM BuildRequires when using Git Submodule
-------------------------------------------

When incorporating ConvergeUI via a git submodule per :doc:`development`, the base project will be set against a particular git hash of ConvergeUI.  In order to incorporate ConvergeUI as a build requires, a ConvergeUI RPM must be generated based off the hash set by the base project.  Assuming a setup similar to :doc:`development`:

.. code-block:: bash

   git clone --recursive <base_project_repository>
   cd <base_project>/vendor/converge-ui
   tito build --test --rpm
   rpm -Uvh /tmp/tito/noarch/converge-ui-devel*.rpm

Now the base project's spec file can be built.
