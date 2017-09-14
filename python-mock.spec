#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : python-mock
Version  : 2.0.0
Release  : 35
URL      : http://pypi.debian.net/mock/mock-2.0.0.tar.gz
Source0  : http://pypi.debian.net/mock/mock-2.0.0.tar.gz
Source99 : http://pypi.debian.net/mock/mock-2.0.0.tar.gz.asc
Summary  : Rolling backport of unittest.mock for all Pythons
Group    : Development/Tools
License  : BSD-2-Clause
Requires: python-mock-legacypython
Requires: python-mock-python
Requires: funcsigs
Requires: pbr
Requires: six
Requires: unittest2
BuildRequires : linecache2
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
your system under test with mock objects and make assertions about how they
        have been used.
        
        mock is now part of the Python standard library, available as `unittest.mock

%package legacypython
Summary: legacypython components for the python-mock package.
Group: Default

%description legacypython
legacypython components for the python-mock package.


%package python
Summary: python components for the python-mock package.
Group: Default
Requires: python-mock-legacypython

%description python
python components for the python-mock package.


%prep
%setup -q -n mock-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505413416
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover --verbose
%install
export SOURCE_DATE_EPOCH=1505413416
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
