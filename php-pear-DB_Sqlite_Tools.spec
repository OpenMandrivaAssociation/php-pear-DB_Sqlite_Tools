%define		_class		DB
%define		_subclass	Sqlite
%define		_ssclass	Tools
%define		upstream_name	%{_class}_%{_subclass}_%{_ssclass}

Name:		php-pear-%{upstream_name}
Version:	0.1.7
Release:	1
Summary:	OO interface designed to effectively manage and backup Sqlite databases
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_Sqlite_Tools/
Source0:	http://download.pear.php.net/package/DB_Sqlite_Tools-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
DB_Sqlite_Tools is extends the native PHP-sqlite function by providing
a comprehensive solution for database backup, live replication, export
in XML format, performance optmization and more. It is designed for
the maintenance and optimisation of several sqlite databases.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -f %{buildroot}/pear/generate_package_xml.php

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-8mdv2012.0
+ Revision: 741844
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-7
+ Revision: 679288
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-6mdv2011.0
+ Revision: 613629
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.6-5mdv2010.1
+ Revision: 479296
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.1.6-4mdv2010.0
+ Revision: 441013
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-3mdv2009.1
+ Revision: 321957
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-2mdv2009.0
+ Revision: 236825
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.1.6-1mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-1mdv2008.0
+ Revision: 15899
- fix build
- fix build
- 0.1.6


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-7mdv2007.0
+ Revision: 81506
- Import php-pear-DB_Sqlite_Tools

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-1mdk
- initial Mandriva package (PLD import)


