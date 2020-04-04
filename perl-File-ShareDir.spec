%{?scl:%scl_package perl-File-ShareDir}

%if ! (0%{?scl:1})
%bcond_without perl_File_ShareDir_enables_optional_runtime
%else
%bcond_with perl_File_ShareDir_enables_optional_runtime
%endif


Name:           %{?scl_prefix}perl-File-ShareDir
Version:        1.116
Release:        7%{?dist}
Summary:        Locate per-dist and per-module shared files
# other files:              GPL+ or Artistic
## not in binary packages
# inc/latest/private.pm:    ASL 2.0
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-ShareDir
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-ShareDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(File::ShareDir::Install)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(IO::Dir)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Class::Inspector) >= 1.12
BuildRequires:  %{?scl_prefix}perl(constant)
# Optional run-time
%if %{with perl_File_ShareDir_enables_optional_runtime}
BuildRequires:  %{?scl_prefix}perl(List::MoreUtils) >= 0.428
BuildRequires:  %{?scl_prefix}perl(Params::Util) >= 1.07
%endif
# Tests
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Class::Inspector) >= 1.12
%if %{with perl_File_ShareDir_enables_optional_runtime}
Recommends:     %{?scl_prefix}perl(List::MoreUtils) >= 0.428
Recommends:     %{?scl_prefix}perl(Params::Util) >= 1.07
%endif

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(Class::Inspector\\)$

%description
The intent of File::ShareDir is to provide a companion to Class::Inspector
and File::HomeDir, modules that take a process that is well-known by
advanced Perl developers but gets a little tricky, and make it more
available to the larger Perl community.

%prep
%setup -q -n File-ShareDir-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*
chmod 644 share/sample.txt
chmod 644 share/subdir/sample.txt
rm -rf %{buildroot}/blib/lib/auto/share/dist/File-ShareDir/
rm -rf %{buildroot}/blib/lib/auto/share/module/File-ShareDir/test_file.txt

%check
%{?scl:scl enable %{scl} '}make test AUTOMATED_TESTING=1%{?scl:'}

%files
%doc LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.116-7
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.116-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.116-2
- Perl 5.28 rebuild

* Mon Jun 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.116-1
- 1.116 bump

* Fri Jun 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.114-1
- 1.114 bump

* Tue Jun 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.112-1
- 1.112 bump

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.110-1
- 1.110 bump

* Mon Jun 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-1
- 1.106 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.104-1
- 1.104 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.102-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.102-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.102-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.102-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.102-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.102-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.102-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.102-1
- 1.102 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.03-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Petr Šabata <contyk@redhat.com> - 1.03-7
- Modernize specfile
- Specify all dependencies
- Drop command macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.03-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-3
- Perl mass rebuild
- fix macros

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Petr Sabata <psabata@redhat.com> - 1.03-1
- 1.03 version bump

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Sep 15 2010 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.00-6
- Mass rebuild with perl-5.12.0

* Thu Jan 14 2010 Marcela Mašláňová 1.00-5
- fix build

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.00-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Marcela Mašláňová 1.00-1
- Specfile autogenerated by cpanspec 1.77.
