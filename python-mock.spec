Name     : python-mock
Version  : 1.3.0
Release  : 16
URL      : https://pypi.python.org/packages/source/m/mock/mock-1.3.0.tar.gz
Source0  : https://pypi.python.org/packages/source/m/mock/mock-1.3.0.tar.gz
Summary  : A Python Mocking and Patching Library for Testing
Group    : Development/Tools
License  : BSD-2-Clause
Requires: python-mock-python
Provides: mock-python
BuildRequires : linecache2
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2
BuildRequires : funcsigs

%description
mock is a library for testing in Python. It allows you to replace parts of
your system under test with mock objects and make assertions about how they
have been used.

%package python
Summary: python components for the python-mock package.
Group: Default

%description python
python components for the python-mock package.


%prep
%setup -q -n mock-1.3.0

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover --verbose
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
