*******
 Fonts
*******

ConvergeUI provides a set of fonts in a variety of formats for cross-browser support.  These fonts are declared in corresponding SCSS files using the font-face directive.

================
 Provided Fonts
================

The fonts and flavors provided by ConvergeUI are:

**Liberation Sans**

* Regular
* Bold
* Italic
* Bold Italic

**Overpass**

* Regular
* Overpass Bold

==================
 Provided Formats
==================

Each font provided by ConvergeUI is provided in the following formats:

* Embedded OpenType (\*.eot)
* Scalable Vector Graphic (\*.svg)
* TrueType (\*.tff)
* Web Open Font Format (\*.woff)

=====================
 Font-Face Directive
=====================

For a given font, an SCSS file is provided that declares the various flavors of the font using the font-face directive.  The following is an example how the 'Liberation Sans Regular' font type would be declared within the 'fonts/liberation.scss' file.  Note this file would also include the declarations for other flavors of the font (e.g. bold, italic).

.. code-block:: css

    @font-face {
            font-family: 'Liberation Sans';
            src: local('Liberation Sans'), local('LiberationSans'), local('Liberation-Sans'),
                 font-url('LiberationSans-Regular-webfont.eot?#iefix') format('eot'),
                 font-url('LiberationSans-Regular-webfont.woff') format('woff'),
                 font-url('LiberationSans-Regular-webfont.ttf') format('truetype'),
                 font-url('LiberationSans-Regular-webfont.svg#webfontLfr8h6FA') format('svg');
            font-weight: normal;
            font-style: normal;
    }
