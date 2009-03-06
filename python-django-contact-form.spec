%define realname django-contact-form

Name:           python-django-contact-form
Version:        0.3
Release:        %mkrel 1
Summary:        An extensible contact-form application for Django

Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/ubernostrum/django-contact-form/
Source0:        http://django-contact-form.googlecode.com/files/contact_form-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-django

%description
An extensible contact-form application for Django

%prep
%setup -q -n contact_form-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt docs/
%{py_puresitedir}/*
