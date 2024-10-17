%define realname django-contact-form
%define alphatag 97559a887345

Name:           python-django-contact-form
Version:        0.3
Release:        5
Summary:        An extensible contact-form application for Django

Group:          Development/Python
License:        BSD
URL:            https://bitbucket.org/ubernostrum/django-contact-form/
Source0:        contact_form-%{alphatag}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-django

%description
An extensible contact-form application for Django

%prep
%setup -q -n %{realname}

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


%changelog
* Fri Nov 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3-4mdv2011.0
+ Revision: 593765
- Add souce

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3-3mdv2011.0
+ Revision: 592242
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2010.0
+ Revision: 442094
- rebuild

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 0.3-1mdv2009.1
+ Revision: 349660
- import python-django-contact-form


