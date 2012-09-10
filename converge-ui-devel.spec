# vim: sw=4:ts=4:et
#
# Copyright 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.


%global homedir %{_datarootdir}/%{name}

Name:          converge-ui-devel
Summary:       Converging UI's since 2012.
Group:         Applications/System
License:       GPLv2
URL:           http://www.convergeui.org
Version:       1.0.2
Release:       1%{?dist}
Source0:       %{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
A common set of web assets.

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m0755 -d %{buildroot}%{homedir}
install -m0755 -d %{buildroot}%{homedir}/javascripts/
install -m0755 -d %{buildroot}%{homedir}/rails/
install -m0755 -d %{buildroot}%{homedir}/stylesheets/
install -m0755 -d %{buildroot}%{homedir}/images/
install -m0755 -d %{buildroot}%{homedir}/fonts/

cp -R javascripts/* %{buildroot}%{homedir}/javascripts/
cp -R rails/* %{buildroot}%{homedir}/rails
cp -R stylesheets/* %{buildroot}%{homedir}/stylesheets/
cp -R images/* %{buildroot}%{homedir}/images/
cp -R fonts/* %{buildroot}%{homedir}/fonts/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(755, root, root)
%{homedir}
%doc README.rst LICENSE

%changelog
* Mon Sep 10 2012 Eric D Helms <ericdhelms@gmail.com> 1.0.2-1
- Merge pull request #68 from n1zyy/login_page_tweaks_2 (jrist@redhat.com)
- Switch back to using a gradient on the login page (matt.wagner@redhat.com)
- Login tweaks from brand (matt.wagner@redhat.com)
- Added notifications placeholder to user_session_layout (jtomasek@redhat.com)

* Wed Sep 05 2012 Eric D Helms <ericdhelms@gmail.com> 1.0.1-1
- Numerous Fixes:   * Fix for some IE8, IE9+ issues,   * Component
  compilations,   * Rescue for missing redir_path,   * Action-icons favorite
  white background. (jrist@redhat.com)

* Thu Aug 30 2012 Eric D Helms <ericdhelms@gmail.com> 1.0-1
- Changes to accomodate fixes to the login/interstitial. (jrist@redhat.com)
- Merge pull request #60 from jsomara/841857 (jsomara@gmail.com)
- 841857 - fixing interestitial scope to display properly in LDAP mode
  (jomara@redhat.com)
- Adds link to convergeui demo and reference site. (ericdhelms@gmail.com)
- Removes github pages reference from readme. (ericdhelms@gmail.com)
- focus outline states for header navigation and anchors - also added the
  clickable helper class (andyfitz@redhat.com)
- Adds a set of color palette definitions. (ericdhelms@gmail.com)
- Added fadeOut of spinner if ajax returns 200. (jrist@redhat.com)
- Merge pull request #35 from ehelms/master (jrist@redhat.com)
- Replaces use of background-position-x and background-position-y with a
  definition set for sprites for grey and black.  This is due to the fact that
  Firefox does not support the above CSS directives. (ericdhelms@gmail.com)
- Switches sprite definitions to the anywhere as opposed to starts with class
  attribute selector. (ericdhelms@gmail.com)
- Updates and cleans-up sprites. (ericdhelms@gmail.com)
- Updates forms to let inputs, labels and fieldsets mimic the login page
  inputs. (ericdhelms@gmail.com)
- setup to allow easy build in koji (msuchy@redhat.com)
- alphabatizing javascript list in docs and adding trunk8 (jsherril@redhat.com)
- Adding trunk8 for easier text ellipsis (jsherril@redhat.com)
- adding newer version of tipsy featuring ajax loading (jsherril@redhat.com)

* Thu Aug 30 2012 Eric D Helms <ericdhelms@gmail.com>
- Changes to accomodate fixes to the login/interstitial. (jrist@redhat.com)
- Merge pull request #60 from jsomara/841857 (jsomara@gmail.com)
- 841857 - fixing interestitial scope to display properly in LDAP mode
  (jomara@redhat.com)
- Adds link to convergeui demo and reference site. (ericdhelms@gmail.com)
- Removes github pages reference from readme. (ericdhelms@gmail.com)
- focus outline states for header navigation and anchors - also added the
  clickable helper class (andyfitz@redhat.com)
- Adds a set of color palette definitions. (ericdhelms@gmail.com)
- Added fadeOut of spinner if ajax returns 200. (jrist@redhat.com)
- Merge pull request #35 from ehelms/master (jrist@redhat.com)
- Replaces use of background-position-x and background-position-y with a
  definition set for sprites for grey and black.  This is due to the fact that
  Firefox does not support the above CSS directives. (ericdhelms@gmail.com)
- Switches sprite definitions to the anywhere as opposed to starts with class
  attribute selector. (ericdhelms@gmail.com)
- Updates and cleans-up sprites. (ericdhelms@gmail.com)
- Updates forms to let inputs, labels and fieldsets mimic the login page
  inputs. (ericdhelms@gmail.com)
- setup to allow easy build in koji (msuchy@redhat.com)
- alphabatizing javascript list in docs and adding trunk8 (jsherril@redhat.com)
- Adding trunk8 for easier text ellipsis (jsherril@redhat.com)
- adding newer version of tipsy featuring ajax loading (jsherril@redhat.com)

* Wed Jul 25 2012 Eric D Helms <ehelms@redhat.com> 0.8.3-1
- Fix for the wrong corner of the last tab in the header being rounded.
  (ehelms@redhat.com)
- Fixes default font color to proper shade of black instead of washed out grey.
  (ehelms@redhat.com)
- Removes variables for images that don't currently exist from the sprites
  file.  Sprites file is intended to be used to store icon class definitions
  and should therefore only be included once per page. (ehelms@redhat.com)

* Tue Jul 24 2012 Eric D Helms <ericdhelms@gmail.com> 0.8.2-1
- Adds proper chosen styling and variablizes the chosen sprite url.
  (ericdhelms@gmail.com)
- Adds jQuery chosen. (ericdhelms@gmail.com)
- Updates for adding new placement of back arrow and adding new icon for
  validation error. (ericdhelms@gmail.com)
- Fixes issue with imporper Overpass bold font-face declaration that led to
  bold overpass fonts being bolded instead of using the font itself.
  (ericdhelms@gmail.com)
- Updates styling on change password screen. (ericdhelms@gmail.com)
- Updates to the login pages related to password recovery and username
  recovery. (ericdhelms@gmail.com)
- Fixes typo with import of base partial. (ericdhelms@gmail.com)
- Cleanup. (ericdhelms@gmail.com)
- Updates to header and footer to pull out color variables.
  (ericdhelms@gmail.com)
- Cleanup of colors. (ericdhelms@gmail.com)

* Sun Jul 08 2012 Eric D Helms <ericdhelms@gmail.com> 0.8.1-1
- Updates to user guide documentation. (ericdhelms@gmail.com)
- Updates to layouts and associated documentation. (ericdhelms@gmail.com)
- Header updates to add proper bottom stroke. (ericdhelms@gmail.com)
- Minor fixes. (ericdhelms@gmail.com)
- Merge remote-tracking branch 'origin/master' into docs (ericdhelms@gmail.com)
- Re-organization of docs and updates to Javascript documentation.
  (ericdhelms@gmail.com)
- Removes the minified version of jQuery. (ericdhelms@gmail.com)
- Moves sprites into components section due to defining CSS.
  (ericdhelms@gmail.com)
- Updates to organization of docs and added numbering. (ericdhelms@gmail.com)
- Moves components to use of underscore to prevent direct compilation by
  compass. (ericdhelms@gmail.com)
- Documentation updates. (ericdhelms@gmail.com)
- Updates to build and development documentation. (ericdhelms@gmail.com)
- Spinner on login. (jrist@redhat.com)
- Spacing in javascript documentation. (ericdhelms@gmail.com)
- Updates for fonts documentation. (ericdhelms@gmail.com)
- Updates for fonts and images documentation. (ericdhelms@gmail.com)
- Merge pull request #29 from knowncitizen/master (ericdhelms@gmail.com)
- Abstracting org switcher to just be "interstitial". (jrist@redhat.com)
- Body > Footer css duplication tweak. (jrist@redhat.com)
- Two things - header-widget fix and org interstitial check 1.) Fixing header-
  widget items to float right in the event some are missing due to perms. 2.)
  Org interstitial check on login_layout so that it will not break other
  projects. (jrist@redhat.com)
- More documentation around process and Javascript. Moved Javascript libraries
  form lib to vendor for third party. (ericdhelms@gmail.com)
- Fix for submit remote true not being necessary. (jrist@redhat.com)
- Making org interstitial a var to prevent usage where not needed.
  (jrist@redhat.com)
- Merges utils stylesheet into helpers. (ericdhelms@gmail.com)
- Treats each partials as stand-alone to be collected in base.
  (ericdhelms@gmail.com)
- Adds normalize SCSS. (ericdhelms@gmail.com)
- Org switcher interstitial changes to include a header. (jrist@redhat.com)
- Changes to login to accomodate an org switcher interstitial.
  (jrist@redhat.com)
- Updates to component and compsite stylesheets. (ehelms@redhat.com)
- Initial re-organization and documentation defining new organization and
  terms. (ehelms@redhat.com)
- Adds new docs structure. (ehelms@redhat.com)

* Mon Jun 25 2012 Eric D Helms <ehelms@redhat.com> 0.7-1
- Fix for images and fonts in converge-ui spec. (jrist@redhat.com)
- More SCSS, CSS duplication reduction.  Faster loading, better fonts, a few
  fixes. (jrist@redhat.com)
- Updates for org switcher and header. (jrist@redhat.com)
- Merge pull request #26 from ehelms/master (jtomasek@redhat.com)
- Action icons updates. (ehelms@redhat.com)
- removed image references not used by converge-ui from _sprites.scss, added
  common images to converge-ui (jtomasek@redhat.com)
- Updates action-icons and corresponding sprite declarations.
  (ehelms@redhat.com)

* Mon Jun 18 2012 Mike McCune <mmccune@redhat.com> 0.6-1
- update to fix the incorrect %%doc README filename (mmccune@gmail.com)

* Mon Jun 18 2012 Mike McCune <mmccune@redhat.com> 0.5-1
- rolling back to 0.3-1 so I can fix the forgotten tag (mmccune@redhat.com)
- Adds short list of supported libraries to test documentation workflow.
  (ehelms@redhat.com)
- Removes documentation build directory from source tree. (ehelms@redhat.com)
- Updates to README (ehelms@redhat.com)
- Automatic commit of package [converge-ui-devel] release [0.4-1].
  (ehelms@redhat.com)
- Updates to README. (ehelms@redhat.com)
- Fixing some settings. (ehelms@redhat.com)
- Re-build docus. (ehelms@redhat.com)
- Adding new test documentation. (ehelms@redhat.com)
- Initial crack at using Sphinx to generate docs. (ehelms@redhat.com)
- Updates to internationalization of string that generates the recovery link.
  (ehelms@redhat.com)
- Updates a few strings for consistency around login vs username.
  (ehelms@redhat.com)
- Merge branch 'master' of git://github.com/Katello/converge-ui
  (ehelms@redhat.com)
- More clean-up of unused code and adding a link back to the login screen from
  the change password screen. (ehelms@redhat.com)
- Org switcher and other small changes. (jrist@redhat.com)
- Re-factors colors within login styling to define default variables to make
  them overrideable by a parent project. (ehelms@redhat.com)
- Updates change password screen to new html structure. (ehelms@redhat.com)
- Updates to color and styling of outer sign on box. (ehelms@redhat.com)
- Re-works the login screen to include slide-out panels for password and
  username recovery. (ehelms@redhat.com)
- Splits the password recovery page into two seperate pages - one for username
  recovery and one for password recovery. (ehelms@redhat.com)
- Adds an instance variable that allows for the disabling of the password
  recovery link.  This may be useful if the project has not implemented
  password recovery or is using a central password store like LDAP.
  (ehelms@redhat.com)
- Removes forms.scss from shell styling until form element styling is
  finalized. (ehelms@redhat.com)
- Merge branch 'master' of git://github.com/Katello/converge-ui
  (ehelms@redhat.com)
- Clean up and re-factor around login javascript and fixing up the favicon
  path. (ehelms@redhat.com)
- Updates to styling to put login page inline with newest design proposals.
  (ehelms@redhat.com)
- Changes to using font-url and assumes that the project using the fonts will
  setup proper font-url configuration variables. (ehelms@redhat.com)
- Fix for details icon in wrong place.  Should not float left.
  (jrist@redhat.com)
- Adds a base.scss file to store and import common variables, mixins and
  utilities.  Updates all scss files to use new base file and includes some
  minor updates to shell and footer styling. (ehelms@redhat.com)
- Merge branch 'master' into login (ehelms@redhat.com)
- Updates the yield blocks for javascript and stylesheets to be less likely to
  clash with an applications declarations. (ehelms@redhat.com)
- Fix for bad url calls on some images. (jrist@redhat.com)
- Merge pull request #14 from knowncitizen/master (eric.d.helms@gmail.com)
- Fix to abstract app name. Allows user of converge-ui to pass in any string.
  (jrist@redhat.com)
- Double position declaration removal. (jrist@redhat.com)
- Relative image urls using compass. (jrist@redhat.com)
- Additional refactoring for decreasing duplicate CSS directives.
  (jrist@redhat.com)
- Updates to get login, password reset and change password basic javascript
  support working. (ehelms@redhat.com)
- Adds footer to user session layout. (ehelms@redhat.com)
- Refactoring for to pull out common bits amongst user session layouts.
  (ehelms@redhat.com)
- Touch-ups to the login screen. (ehelms@redhat.com)
- Updates change password layout to conform with general styling and adds more
  translations for text used on both reset and change pages.
  (ehelms@redhat.com)
- jquery - multiselect & filter - add new widgets (bbuckingham@redhat.com)
- Adds updated password reset screen with translations and formatting.
  (ehelms@redhat.com)
- Merge pull request #11 from knowncitizen/master (eric.d.helms@gmail.com)
- Fix for tab highlight on currently selected tab. (jrist@redhat.com)

* Sat Jun 16 2012 Eric D Helms <ehelms@redhat.com> 0.4-1
- Updates to README. (ehelms@redhat.com)
- Fixing some settings. (ehelms@redhat.com)
- Re-build docus. (ehelms@redhat.com)
- Adding new test documentation. (ehelms@redhat.com)
- Initial crack at using Sphinx to generate docs. (ehelms@redhat.com)
- Updates to internationalization of string that generates the recovery link.
  (ehelms@redhat.com)
- Updates a few strings for consistency around login vs username.
  (ehelms@redhat.com)
- Merge branch 'master' of git://github.com/Katello/converge-ui
  (ehelms@redhat.com)
- More clean-up of unused code and adding a link back to the login screen from
  the change password screen. (ehelms@redhat.com)
- Org switcher and other small changes. (jrist@redhat.com)
- Re-factors colors within login styling to define default variables to make
  them overrideable by a parent project. (ehelms@redhat.com)
- Updates change password screen to new html structure. (ehelms@redhat.com)
- Updates to color and styling of outer sign on box. (ehelms@redhat.com)
- Re-works the login screen to include slide-out panels for password and
  username recovery. (ehelms@redhat.com)
- Splits the password recovery page into two seperate pages - one for username
  recovery and one for password recovery. (ehelms@redhat.com)
- Adds an instance variable that allows for the disabling of the password
  recovery link.  This may be useful if the project has not implemented
  password recovery or is using a central password store like LDAP.
  (ehelms@redhat.com)
- Removes forms.scss from shell styling until form element styling is
  finalized. (ehelms@redhat.com)
- Merge branch 'master' of git://github.com/Katello/converge-ui
  (ehelms@redhat.com)
- Clean up and re-factor around login javascript and fixing up the favicon
  path. (ehelms@redhat.com)
- Updates to styling to put login page inline with newest design proposals.
  (ehelms@redhat.com)
- Changes to using font-url and assumes that the project using the fonts will
  setup proper font-url configuration variables. (ehelms@redhat.com)
- Fix for details icon in wrong place.  Should not float left.
  (jrist@redhat.com)
- Adds a base.scss file to store and import common variables, mixins and
  utilities.  Updates all scss files to use new base file and includes some
  minor updates to shell and footer styling. (ehelms@redhat.com)
- Merge branch 'master' into login (ehelms@redhat.com)
- Updates the yield blocks for javascript and stylesheets to be less likely to
  clash with an applications declarations. (ehelms@redhat.com)
- Fix for bad url calls on some images. (jrist@redhat.com)
- Merge pull request #14 from knowncitizen/master (eric.d.helms@gmail.com)
- Fix to abstract app name. Allows user of converge-ui to pass in any string.
  (jrist@redhat.com)
- Double position declaration removal. (jrist@redhat.com)
- Relative image urls using compass. (jrist@redhat.com)
- Additional refactoring for decreasing duplicate CSS directives.
  (jrist@redhat.com)
- Updates to get login, password reset and change password basic javascript
  support working. (ehelms@redhat.com)
- Adds footer to user session layout. (ehelms@redhat.com)
- Refactoring for to pull out common bits amongst user session layouts.
  (ehelms@redhat.com)
- Touch-ups to the login screen. (ehelms@redhat.com)
- Updates change password layout to conform with general styling and adds more
  translations for text used on both reset and change pages.
  (ehelms@redhat.com)
- jquery - multiselect & filter - add new widgets (bbuckingham@redhat.com)
- Adds updated password reset screen with translations and formatting.
  (ehelms@redhat.com)
- Merge pull request #11 from knowncitizen/master (eric.d.helms@gmail.com)
- Fix for tab highlight on currently selected tab. (jrist@redhat.com)

* Wed May 16 2012 Eric D Helms <ehelms@redhat.com> 0.3-1
- First tag of converge-ui-devel.

* Thu Mar 29 2012 Eric D Helms <ehelms@redhat.com> 0.2-1
- new package built with tito

* Wed Mar 28 2012 Eric D Helms <ehelms@redhat.com> 0.1-1
- Changes to spec file. (ehelms@redhat.com)
