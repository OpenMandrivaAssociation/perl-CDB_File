%define upstream_name    CDB_File
%define upstream_version 0.97

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.970.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.970.0-1
+ Revision: 653980
- update to new version 0.97

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-2mdv2011.0
+ Revision: 555690
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.0
+ Revision: 402099
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.96-2mdv2009.0
+ Revision: 268372
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.96-1mdv2009.0
+ Revision: 195211
- new version
  drop undocumented patch (doesn't apply anymore)

* Mon Feb 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.95-1mdv2008.1
+ Revision: 165057
- import perl-CDB_File


* Mon Feb 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.95-1mdv2008.1
- initial Mandriva package 
