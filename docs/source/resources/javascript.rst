************
 Javascript
************

==============
 Organization
==============

ConvergeUI provides Javacript in two forms.  First, a set of vendor libraries are supplied that a project can optionally pull into their project for use.  Second, ConvergeUI supplies some Javascript functionality along with the provided layouts.

---------------------
 Available Libraries
---------------------

The Javascript directory, and thus provided libraries, is laid out in the following way::

  javascripts/
        login.js

        vendor/
            rails.js
            underscore-1.3.1.js

            jquery/
                jquery-1.6.2.min.js

                plugins/
                    flot-0.7/
                    jquery.ajaxfileupload.js        
                    jquery.jscrollpane.js         
                    jquery.text-overflow.js
                    jquery.ba-bbq.js                
                    jquery.ba-resize.js             
                    jquery.timepickr.js
                    jquery.linkHover.js           
                    jquery.timers.js
                    jquery.cookie.js                
                    jquery.loadmask.min.js        
                    jquery.tipsy.js
                    jquery.easing.1.3.js            
                    jquery.mousewheel.js          
                    jquery.treeTable.js
                    jquery.fancyqueries.js          
                    jquery.multiselect.js         
                    jquery.multiselect.filter.js  
                    jquery.ui.multiselect.js
                    jquery.ui.spinner.js
                    jquery.ui.totop.js
                    jquery.flash.js                 
                    jquery.uitablefilter.js
                    jquery.form.js                  
                    jquery.pack.js                
                    jquery.hoverIntent.js           
                    jquery.periodicalupdater.js   
                    jquery.jeditable.js             
                    jquery.jeditable.ajaxupload.js  
                    jquery.sortElements.js
                    jquery.sparkline.min.js


=====================================
 Project Javascript Code Conventions
=====================================

This document contains conventions for programming Javascript that should be followed in an effort to increase readability, performance and re-usability.  As builds are run against the [http://www.jslint.com/ JSLint Code Quality Tool], an effort should be made to conform to the guidelines set forth by JSLint.

---------
 General
---------

 * Always use ''==='' for comparison
 * Place semicolons wherever they are required.  While missing semicolons may not throw an error, they can cause unintended behaviors.
 * Try to avoid or limit the usage of global objects. (Variables declared outside of a function)

-----------------------------
 ConvergeUI Global Namespace
-----------------------------

Since ConvergeUI provides some JavaScript functionality with the provided layouts, a project wide global object exists that all custom code is attached to.  This is done in order to prevent global namespace collission and make debugging easier.  The project uses the top level global namespace (CUI).  The CUI object is declared in the top level of each ConvergeUI custom JavaScript file such that it is guaranteed to be loaded and exist on every page before any other custom scripts.  All modules should be attached to the CUI global object with appropriate namespacing.  For example, we can attach a module named ''login'' to the top level global CUI object and a sub-module to ''login'' for holding password specific functionality:

.. code-block:: javascript

    CUI.login = (function($){
        var hello_world = "hello World";
      
        return {
            hello_world   :  hello_world
        };
    }(jQuery));

    CUI.login.password = (function($){
        var create = function(){};

        return {
            create   :  create
        };
    }(jQuery));

--------------------
 Syntax Conventions
--------------------

The following are coding conventions related to Javascript syntax in an effort to enhance readability and adhere to the semantics of the language itself.

----------------------
 Variable Declaration
----------------------

All variable declarations should be placed at the top of a function and a single ''var'' statement with comma separated variables should follow.

Correct

.. code-block:: javascript

    var add = function(list){
        var sum = 0,
            length = list.length,
            i;
           
        for( i=0; i < length; i += 1){
            sum += list[i];
        }

        return sum;
    };

Incorrect

.. code-block:: javascript

    var add = function(list){
        var sum = 0;
           
        var length = list.length;
        for(var i=0; i < length; i += 1){
            sum += list[i];
        }

        return sum;
    };

-------------------------
 Object Attribute Access
-------------------------

Javascript supports both the dot-operator (myobject.foo) and index-style (myobject{{{[}}}"foo"{{{]}}}) object attribute access.  While the former can be slightly cleaner or more traditional when calling object methods, the latter allows for dynamic properties and can avoid reserved keyword clashes.  For example, ''package'' is a reserved word such that myobject.package can cause errors while myobject{{{[}}}'package'{{{]}}} will not.  Methods may be called using index-style notation as well - ''myobject{{{[}}}'add_package'{{{]}}}()''.
