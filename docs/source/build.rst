======
Build
======

Provided are examples of how a project might choose to build and package ConvergeUI to be incorporated as part of a larger project.

-------------
Requirements
-------------

We recommend installing *tito* for use when building RPMs.

----
RPM
----

-------------------
Stand-alone RPM
-------------------

ConvergeUI can be built as a stand-alone RPM that can then be included within a repository for use as part of a larger project either at build or deployment time depending on the requirements and constraints of the project.  

Clone ConvergeUI

.. code-block:: bash

   git clone http://github.com/Katello/converge-ui.git
   cd converge-ui

Build Latest Tagged Version

.. code-block:: bash

   tito build


Build Against HEAD

.. code-block:: bash

   tito build --test --rpm

Look at the end of the *tito* output to find the location of the newly created RPM.


-----------------------------
RPM when using Git Submodule
-----------------------------
