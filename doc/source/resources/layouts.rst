*********
 Layouts
*********

ConvergeUI uses HAML to define a set of layouts that, when combined with their styling counterparts, provide components common to web applications.  The layouts are designed to provide a particular look and feel when combined with the appropriate styling; however, since the layouts and styling are seperate, a need look can be applied while maintaing the overall structure.  The layouts are designed to be have configurable content via the use of *content_for* blocks.  Example:

Layout

.. code-block:: ruby

  %body{:id => section_id}
    = yield :body
    = yield :javascripts_block
    = yield :extra

Implemetation

.. code-block:: ruby

    = content_for(:body) do
      #wrapper
        = render :partial => "layouts/converge-ui/header_layout"
        %article#maincontent
          %section.maincontent
            = yield :content
      %footer
        = yield :footer

===================
 Component Layouts
===================

--------
 Header
--------

The header layout provides a thick header with area for a left aligned-logo, content tabs along the header baseline, and widgets in the upper right hand corner.  All header content is centered horizontally with the page.

---------
 Foooter
---------

The footer layout provides a small ribbon that is "sticky" to the bottom of the page as content grows vertically.  Place is provided for copyright, footer links, logo and versioning information.

===================
 Composite Layouts
===================

-------
 Shell
-------

The shell layout combines the header, footer and adds a centered *application* area for all application content.

--------------
 User Session
--------------

The user sessoin layout provides a centered modal-like container for user session interactions combined with the footer layout.
