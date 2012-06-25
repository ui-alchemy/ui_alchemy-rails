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
Summary:       A collection of assets
Group:         Applications/System
License:       GPLv2
URL:           http://www.katello.org
Version:       0.6
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
