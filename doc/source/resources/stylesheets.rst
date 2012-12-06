*************
 Stylesheets
*************

=======================
 Available Stylesheets
=======================

The stylesheets directory is laid out in the following way::

  stylesheets/
        composites/
            shell.scss
            login.scss

        components/
            _footer.scss
            _header.scss
            _helpers.scss
            _media.scss
            _login.scss
            _text.scss
            _forms.scss
            _content.scss
            _normalize.scss
            _sprites.scss

            fonts/
                _liberation.scss
                _overpass.scss

        partials/
            _base.scss
            _mixins.scss
            _colors.scss
            _vars.scss

==================
 Stylesheet Types
==================

----------------------
 Composite Stylsheets
----------------------

Composite stylesheets combine multiple *component stylsheets* to create a larger conceptual entity.  For example, a *composite stylesheet* may combine the header, content and footer components while also including the components used to define typographical and form entities.

-----------------------
 Component Stylesheets
-----------------------

Component stylesheets represent a singular entity (e.g. header, footer, widget) that may be combined into a *composite stylsheet*.  These stylesheets should include a set of partials that define needed variables, colors, or mixins.  Component stylesheets also use the underscore notation to prevent Compass from compiling them directly.

---------------------
 Partial Stylesheets
---------------------

Partials are denoted by SCSS files that begin with an underscore (e.g. _vars).  Partials are intended to be included on multiple *component stylesheets* and should therefore not include any direct CSS, but rather, should be limited to the following:

* Variables
* Mixins
* Function Directives

=======================
 SCSS Code Conventions
=======================

The SCSS code conventions adopted by ConvergeUI are an effort to increase readability, performance and re-usability.

-----------------
 Classes and IDs
-----------------

Use underscores to break apart logical elements of the name.  This helps to differentiate custom CSS from standard CSS provided by the browser.

Examples::

    .card_container
    #password_recovery_form

----------------------
 Variables and Mixins
----------------------

The general format for the naming convention is to use underscores to separate the name and to use a dash to tack on a property of the variable, image or mixin::

    <the_name_separated_by_underscores>-<property>

Where:
 * <the_name_separated_by_underscores>: Use of underscores to separate logical pieces of the name
 * <property>: Denotes "what" a particular variable, or mixin is, typically the name of the CSS property it represents

Examples::

    $login_container-width: 280px;
    $login_container-height: 125px;
    $logo_link-left: 45px;

    mixin header-background {
      background: red;
    }

    .lock_icon-grey
    .lock_icon-white
