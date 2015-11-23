#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.config
Version  : 3.0.0
Release  : 25
URL      : http://tarballs.openstack.org/oslo.config/oslo.config-3.0.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.config/oslo.config-3.0.0.tar.gz
Summary  : Oslo Configuration API
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.config-bin
Requires: oslo.config-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : fixtures-python
BuildRequires : flake8
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : netaddr-python
BuildRequires : oslo.i18n-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
Patch1: 0001-Add-embeded-multi-files-parsing.patch

%description
==========================
Oslo Configuration Library
==========================

%package bin
Summary: bin components for the oslo.config package.
Group: Binaries

%description bin
bin components for the oslo.config package.


%package python
Summary: python components for the oslo.config package.
Group: Default
Requires: six-python
Requires: stevedore

%description python
python components for the oslo.config package.


%prep
%setup -q -n oslo.config-3.0.0
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-config-generator

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
