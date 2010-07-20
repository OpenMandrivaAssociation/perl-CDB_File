%define upstream_name    CDB_File
%define upstream_version 0.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Extension for access to cdb databases
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's cdb
package.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
