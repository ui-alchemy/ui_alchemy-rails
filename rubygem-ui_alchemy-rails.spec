%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# vim: sw=4:ts=4:et
#
# Copyright 2011 Red Hat, Inc.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%global gem_name ui_alchemy-rails

%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} < 19
%define rubyabi 1.9.1
%endif


%if 0%{?rhel} == 6 && "%{?scl}" == ""
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%endif

BuildRequires: %{?scl_prefix}rubygems-devel

Name:          %{?scl_prefix}rubygem-%{gem_name}
Summary:       Mixing up the best that web technologies have to offer.
Group:         Applications/System
License:       MIT
Version:       1.0.12
Release:       1%{?dist}
URL:           http://www.ui-alchemy.org
Source0:       %{pkg_name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if 0%{?fedora} > 18
Requires:       %{?scl_prefix}ruby(release)
%else
Requires:       %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires:       %{?scl_prefix}ruby(rubygems) 
Requires:       %{?scl_prefix}rubygem(compass)
%if 0%{?fedora} > 18
BuildRequires:       %{?scl_prefix}ruby(release)
%else
BuildRequires:       %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires:  %{?scl_prefix}ruby(rubygems) 
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Rails engine providing a set of web assets.

%prep
%setup -n %{pkg_name}-%{version} -q

%build
%{?scl:scl enable %{scl} - << \EOF}
LANG=en_US.utf-8 gem build %{gem_name}.gemspec
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} "}
gem install \
     --local \
     --install-dir %{buildroot}%{gem_dir} \
     --force \
     %{gem_name}-%{version}.gem
%{?scl:"}

mkdir -p %{buildroot}%{gem_dir}

rm -rf %{buildroot}%{gem_instdir}/.yardoc


%files
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/lib
%{gem_instdir}/app
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md


%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Aug 27 2013 Eric D Helms <ehelms@redhat.com> 1.0.12-1
- Version bump to 1.0.12 (ehelms@redhat.com)
- Updating UnderscoreJS to 1.5.1 (ehelms@redhat.com)
- Removed an unused spec macro (paji@redhat.com)
- Changes to get alchemy building on f19 (paji@redhat.com)
- Adding a build target for Fedora 19 (paji@redhat.com)

* Thu Jun 20 2013 Eric D Helms <ehelms@redhat.com> 1.0.11-1
- Updating spec. (ehelms@redhat.com)
- Version bump to 1.0.11 (ehelms@redhat.com)
- Spec: Enabling SCL prefixes in spec. (ehelms@redhat.com)
- Merge pull request #163 from ehelms/vendor-update (ericdhelms@gmail.com)
- Alchemy-header update. (ericdhelms@gmail.com)
- Fonts: Make setting the font_path optional. (ericdhelms@gmail.com)
- Added support for maxlength attribute for jeditable textarea
  (mtapaswi@redhat.com)
- Version bump. (ehelms@redhat.com)
- Merge pull request #159 from ehelms/component-updates (ericdhelms@gmail.com)
- Bumping the version of Alchemy header included. (ericdhelms@gmail.com)

* Mon May 06 2013 Eric D Helms <ehelms@redhat.com> 1.0.9-1
- Version bump. (ehelms@redhat.com)
- Updating alchemy-tables and alchemy-header. (ehelms@redhat.com)
- Adding angular-resource to alchemy rails. (walden@redhat.com)

* Mon Apr 22 2013 Eric D Helms <ehelms@redhat.com> 1.0.8-1
- Version bump 1.0.8. (ehelms@redhat.com)
- Header and Tables - Updates to both components to address issues when
  attempting to minify. (ericdhelms@gmail.com)
- Version bump to 1.0.7. (ehelms@redhat.com)
- Initializer - Fix for the paths initializer that can be ignored by projects
  that set config.assets.initialize_on_precompile = false (ehelms@redhat.com)
- Removing unneeded CSS file that doesn't exist from Alchemy repo.
  (ehelms@redhat.com)
- Updating font urls to be relative to engine namespace. (ehelms@redhat.com)
- Updating Alchemy Tables to include infinite scroll support for loading more
  rows. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- Adding alchemy-header as a carried library. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- Updates to move references to the alchemy component. (ehelms@redhat.com)
- Removing forms and partials in favor of their components. (ehelms@redhat.com)
- Adding component repositories via bower. (ehelms@redhat.com)

* Fri Mar 29 2013 Eric D Helms <ehelms@redhat.com> 1.0.4-1
- new package built with tito

* Thu Mar 28 2013 Eric D Helms <ehelms@redhat.com> 1.0.3-1
- Bumping to meet gem version.

* Thu Mar 28 2013 Eric D Helms <ehelms@redhat.com> 1.0.2-1
- Version bump. (ehelms@redhat.com)
- Merge pull request #151 from ehelms/flot-cleanup (ericdhelms@gmail.com)
- Removes Flot development cruft. (ehelms@redhat.com)
- Fix chosen-sprite relative path (hbrock@redhat.com)
- Merge pull request #147 from abenari/select (ericdhelms@gmail.com)
- Updates Normalize to the most recent version. (ehelms@redhat.com)
- Adds HandlebarsJS templating library (ehelms@redhat.com)
- make select box the same size and same border and background color as the
  edit box. (abenari@redhat.com)
- fixed latest comments. (abenari@redhat.com)
- Moves engine declaration into explicit file. Adds helper functions for
  stylesheets and javascript to ensure child views declaring a stylesheet or
  javascript requirement are appended. (ehelms@redhat.com)
- added danger button (jcoufal@redhat.com)
- Merge pull request #145 from abenari/minor-fixes (email@jaromircoufal.cz)
- Merge pull request #142 from mbacovsky/login_screen_padding
  (email@jaromircoufal.cz)
- fixed fieldset lable width. (abenari@redhat.com)
- removed clear after btn-group, because it brakes multiple btn-group in a
  single toolbar (abenari@redhat.com)
- seting the login logo size (abenari@redhat.com)
- fix image re-size for the logo. This fix enables using a large image for the
  logo that looks good in close-up. (abenari@redhat.com)
- Added btn-success (abenari@redhat.com)
- added support for single button in a button group (abenari@redhat.com)
- fixed var usage in url (abenari@redhat.com)
- added aliases for bootstrap compatibility: primary, btn-primary warning, btn-
  warning btn_group, btn-group lable, control-lable (abenari@redhat.com)
- Update alchemy.gemspec (jtomasek@redhat.com)
- make colors default in order to be easily overwritten (jcoufal@redhat.com)
- Avoid footer overlaping over login form on narrow screen
  (mbacovsk@redhat.com)
- Merge pull request #141 from xsuchy/pull-req-f18 (jrist@redhat.com)
- Version bump. (ehelms@redhat.com)
- allow to build under F18 (msuchy@redhat.com)
- Adds Media object as a component. (ehelms@redhat.com)

* Tue Jan 15 2013 Eric D Helms <ehelms@redhat.com> 1.0.1-1
- Spec - Updates to use any version of compass available. (ehelms@redhat.com)
- Added default to component variables + fixed btn primary color at hover
  (jcoufal@redhat.com)
- Templates - Updates to make templates more usuable outside alchemy.
  (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- Removes the jquery ui development bundle. (ehelms@redhat.com)
- Encoding - A character exists in the comments that causes Rails asset
  pipeline to explode. (ehelms@redhat.com)
- SCSS - Moves from relative pathing in SCSS imports to be based off the
  alchemy namespacing for proper imports by parent applications using the
  engine. (ehelms@redhat.com)
- Removing redundant string. (jrist@redhat.com)
- Fix for get_string to translate for gettext properly (jrist@redhat.com)

* Thu Dec 06 2012 Eric D Helms <ehelms@redhat.com> 1.0.0-1
- new package built with tito

