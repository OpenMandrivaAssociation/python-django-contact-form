%define module django-contact-form
%define oname django_contact_form

Name:		python-django-contact-form
Version:	5.2.0
Release:	1
Summary:	An extensible contact-form application for Django
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/ubernostrum/django-contact-form
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(django)
# Declare an explicit Require here as the module itself does not.
Requires:	python%{pyver}dist(django)

%description
An extensible contact-form application for Django

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}.dist-info
