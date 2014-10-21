# $Id: Palm-ListDB.spec.in,v 1.1 2003/09/11 20:13:47 jv Exp $

%define modname Palm-ListDB-Writer
%define modversion 1.10
%define modpath authors/id/J/JV/JV/%{modname}-%{modversion}.tar.gz
%define modreq perl

Name: perl-%{modname}
Version: %{modversion}
Release: 1
Source: ftp://ftp.cpan.org/pub/CPAN/%{modpath}

URL: http://www.cpan.org/
BuildArch: noarch
BuildRoot: %{_tmppath}/rpm-buildroot-%{name}-%{version}-%{release}
Prefix: %{_prefix}

Summary: Module to create Palm 'List' databases.
License: Artistic or GPL
Group: Application / Databases
Requires: %{modreq}
BuildPrereq: %{modreq}
Packager: jv@cpan.org

%description
Palm::ListDB is a module that constructs databases for the Palm
utility List. List is written by Andrew Low (roo@magma.ca,
http://www.magma.ca/~roo).

An utility program csv2pdb is included, that can generate List DBs
from comma-separated value files (CSVs).

See http://www.magma.ca/~roo for more information on the List utility.

%define __find_provides /usr/lib/rpm/find-provides.perl
%define __find_requires /usr/lib/rpm/find-requires.perl

%prep
%setup -q -n %{modname}-%{modversion}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL \
	PREFIX=%{buildroot}%{_prefix} INSTALLDIRS=vendor
make
make test

%install
rm -rf %buildroot
make install_vendor

[ ! -x /usr/lib/rpm/brp-compress ] || /usr/lib/rpm/brp-compress

find %buildroot \( -name perllocal.pod -o -name .packlist \) -exec rm -vf {} \;
find %{buildroot}%{_prefix} -type f -print | sed 's|^%{buildroot}||' > rpm-files
[ -s rpm-files ] || exit 1

%clean
rm -rf %buildroot

%files -f rpm-files
%defattr(-,root,root)
