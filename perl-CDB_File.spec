%define module CDB_File

Summary:	Extension for access to cdb databases
Name:		perl-%{module}
Version:	0.96
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's cdb
package.

%prep
%setup -q -n %{module}-%{version} 

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
%{perl_vendorarch}/auto/CDB_File
%{perl_vendorarch}/CDB_File.pm
%{perl_vendorarch}/bun-x.pl
%{_mandir}/*/*

