#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : oslo.config
Version  : 8.2.0
Release  : 77
URL      : http://tarballs.openstack.org/oslo.config/oslo.config-8.2.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.config/oslo.config-8.2.0.tar.gz
Source1  : http://tarballs.openstack.org/oslo.config/oslo.config-8.2.0.tar.gz.asc
Summary  : Oslo Configuration API
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.config-bin = %{version}-%{release}
Requires: oslo.config-license = %{version}-%{release}
Requires: oslo.config-python = %{version}-%{release}
Requires: oslo.config-python3 = %{version}-%{release}
Requires: PyYAML
Requires: debtcollector
Requires: netaddr
Requires: oslo.i18n
Requires: requests
Requires: rfc3986
Requires: stevedore
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : debtcollector
BuildRequires : netaddr
BuildRequires : oslo.i18n
BuildRequires : pbr
BuildRequires : requests
BuildRequires : rfc3986
BuildRequires : stevedore
Patch1: 0001-stateless.patch

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the oslo.config package.
Group: Binaries
Requires: oslo.config-license = %{version}-%{release}

%description bin
bin components for the oslo.config package.


%package license
Summary: license components for the oslo.config package.
Group: Default

%description license
license components for the oslo.config package.


%package python
Summary: python components for the oslo.config package.
Group: Default
Requires: oslo.config-python3 = %{version}-%{release}

%description python
python components for the oslo.config package.


%package python3
Summary: python3 components for the oslo.config package.
Group: Default
Requires: python3-core
Provides: pypi(oslo.config)
Requires: pypi(debtcollector)
Requires: pypi(netaddr)
Requires: pypi(oslo.i18n)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(rfc3986)
Requires: pypi(stevedore)

%description python3
python3 components for the oslo.config package.


%prep
%setup -q -n oslo.config-8.2.0
cd %{_builddir}/oslo.config-8.2.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592585247
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.config
cp %{_builddir}/oslo.config-8.2.0/LICENSE %{buildroot}/usr/share/package-licenses/oslo.config/b9a131284bb03c49a33f0ade435e87c1bff4394b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-config-generator
/usr/bin/oslo-config-validator

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.config/b9a131284bb03c49a33f0ade435e87c1bff4394b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
