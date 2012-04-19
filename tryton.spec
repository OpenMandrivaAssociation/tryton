Name:		tryton
Summary:	The client of the Tryton application platform
Version:	2.2.1
Release:	1
License:	GPLv3+
Group:		Development/Python
Source0:	http://pypi.python.org/packages/source/t/trytond/%{name}-%{version}.tar.gz
%py_requires -d
BuildArch:	noarch

%description
The client of the Tryton application platform.
A three-tiers  high-level general purpose application platform
written in Python and use Postgresql as main database engine.
It is the core base of an Open Source ERP.
It provides modularity, scalability and security.

%package -n python-%{name}
Summary:	Python modules for %{name}
Group:		Development/Python

%description -n python-%{name}
Python modules for %{name}

%prep
%setup -q

%build
python setup.py build

%install
NDONTWRITEBYTECODE=  python setup.py install --root=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%doc CHANGELOG COPYRIGHT README TODO
%{_datadir}/pixmaps/%{name}

%files -n python-%{name}
%doc CHANGELOG COPYRIGHT README TODO
%{py_sitedir}/*