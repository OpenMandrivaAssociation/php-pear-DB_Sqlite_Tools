%define		_class		DB
%define		_subclass	Sqlite
%define		_ssclass	Tools
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_%{_ssclass}

Summary:	%{_pearname} - OO interface designed to effectively manage and backup Sqlite databases
Name:		php-pear-%{_pearname}
Version:	0.1.6
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_Sqlite_Tools/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Patch0:		%{name}-path_fix.patch
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
DB_Sqlite_Tools is extends the native PHP-sqlite function by providing
a comprehensive solution for database backup, live replication, export
in XML format, performance optmization and more. It is designed for
the maintenance and optimisation of several sqlite databases.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U
%patch0 -p1

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/%{_ssclass}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_ssclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/%{_ssclass}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml


