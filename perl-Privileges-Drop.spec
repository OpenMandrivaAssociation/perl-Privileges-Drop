%define upstream_name    Privileges-Drop
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    A module to make it simple to drop all privileges, even 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Privileges/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch

%description
This module tries to simplify the process of dropping privileges. This can
be useful when your Perl program needs to bind to privileged ports, etc.
This module is much like Proc::UID, except that it's implemented in pure
Perl. Special care has been taken to also drop saved uid on platforms that
support this, currently only test on on Linux.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog META.json META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

