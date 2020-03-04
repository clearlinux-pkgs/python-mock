#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-mock
Version  : 4.0.1
Release  : 78
URL      : https://files.pythonhosted.org/packages/1c/fd/141c477591ab50e27cd16a4969c957f915f4fb3c6323a624c548f38b507f/mock-4.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/fd/141c477591ab50e27cd16a4969c957f915f4fb3c6323a624c548f38b507f/mock-4.0.1.tar.gz
Summary  : Mocking and Patching Library for Testing
Group    : Development/Tools
License  : BSD-2-Clause
Requires: python-mock-license = %{version}-%{release}
Requires: python-mock-python = %{version}-%{release}
Requires: python-mock-python3 = %{version}-%{release}
Requires: wheel
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : six
BuildRequires : wheel

%description
mock is a library for testing in Python. It allows you to replace parts of
your system under test with mock objects and make assertions about how they
have been used.

%package license
Summary: license components for the python-mock package.
Group: Default

%description license
license components for the python-mock package.


%package python
Summary: python components for the python-mock package.
Group: Default
Requires: python-mock-python3 = %{version}-%{release}
Provides: pypi(mock)

%description python
python components for the python-mock package.


%package python3
Summary: python3 components for the python-mock package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-mock package.


%prep
%setup -q -n mock-4.0.1
cd %{_builddir}/mock-4.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583295483
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-mock
cp %{_builddir}/mock-4.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-mock/2eec66c59087d1cf096a35fc620161b222591e05
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-mock/2eec66c59087d1cf096a35fc620161b222591e05

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
