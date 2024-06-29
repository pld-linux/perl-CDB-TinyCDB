#
# Conditional build:
%bcond_with	tests		# do not perform "make test"

%define		pdir	CDB
%define		pnam	TinyCDB
Summary:	CDB::TinyCDB - Perl extension for TinyCDB library to cdb databases
Name:		perl-CDB-TinyCDB
Version:	0.05
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AJ/AJGB/CDB-TinyCDB-%{version}.tar.gz
# Source0-md5:	e77702b031264c6686a6f617e92b9e24
Patch0:		not-pch.patch
URL:		https://metacpan.org/release/CDB-TinyCDB/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	tinycdb-devel
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-NoWarnings
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDB::TinyCDB is a Perl extension for TinyCDB library to query and
create CDB files.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/CDB
%{perl_vendorarch}/CDB/TinyCDB.pm
%dir %{perl_vendorarch}/auto/CDB
%dir %{perl_vendorarch}/auto/CDB/TinyCDB
%attr(755,root,root) %{perl_vendorarch}/auto/CDB/TinyCDB/TinyCDB.so
%{_mandir}/man3/CDB::TinyCDB.3pm*
