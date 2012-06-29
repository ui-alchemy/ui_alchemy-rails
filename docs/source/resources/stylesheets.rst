============
Stylesheets
============

------------
Organization
------------

^^^^^^^^^^^^^^^
File Structure
^^^^^^^^^^^^^^^

The stylesheets directory is laid out in the following way::

  stylesheets/
        composites/
            shell.scss
            login.scss
        components/
            footer.scss
            header.scss
            content.scss
            normalize.scss
            fonts/
                liberation.scss
                overpass.scss
        partials/
            _base.scss
            _mixins.scss
            _colors.scss
            _vars.scss

^^^^^^^^^^^^^^^^^^^^^
Composite Stylsheets
^^^^^^^^^^^^^^^^^^^^^

Composite stylesheets combine multiple *component stylsheets* to create a larger conceptual entity.  For example, a *composite stylesheet* may combine the header, content and footer components while also including the components used to define typographical and form entities.

^^^^^^^^^^^^^^^^^^^^^
Component Stylesheets
^^^^^^^^^^^^^^^^^^^^^

Component stylesheets represent a singular entity (e.g. header, footer, widget) that may be combined into a *composite stylsheet*.  These stylesheets should include a set of partials that define needed variables, colors, or mixins.

^^^^^^^^^^^^^^^^^^^
Partial Stylesheets
^^^^^^^^^^^^^^^^^^^

Partials are denoted by SCSS files that begin with an underscore (e.g. _vars).  Partials are intended to be included on multiple *component stylesheets* and should therefore not include any direct CSS, but rather, should be limited to the following:

* Variables
* Mixins
* Function Directives

----------------------
SCSS Code Conventions
----------------------
