%define real_name CDB_File

Summary:	Extension for access to cdb databases
Name:		perl-%{real_name}
Version:	0.96
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{real_name}-%{version}.tar.gz
Patch0:		CDB_File-perl510.diff
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's cdb
package.

%prep

%setup -q -n %{real_name}-%{version} 
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLEDGE CHANGES COPYRIGHT README
%dir %{perl_vendorarch}/auto/CDB_File
%{perl_vendorarch}/auto/CDB_File/*.so
%{perl_vendorarch}/*.p*
%{_mandir}/*/*

