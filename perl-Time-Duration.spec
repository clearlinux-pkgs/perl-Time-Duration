#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Time-Duration
Version  : 1.21
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Time-Duration-1.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Time-Duration-1.21.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtime-duration-perl/libtime-duration-perl_1.20-1.debian.tar.xz
Summary  : 'rounded or exact English expression of durations'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Time-Duration-license = %{version}-%{release}
Requires: perl-Time-Duration-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Time-Duration,
version 1.21:
rounded or exact English expression of durations

%package dev
Summary: dev components for the perl-Time-Duration package.
Group: Development
Provides: perl-Time-Duration-devel = %{version}-%{release}
Requires: perl-Time-Duration = %{version}-%{release}

%description dev
dev components for the perl-Time-Duration package.


%package license
Summary: license components for the perl-Time-Duration package.
Group: Default

%description license
license components for the perl-Time-Duration package.


%package perl
Summary: perl components for the perl-Time-Duration package.
Group: Default
Requires: perl-Time-Duration = %{version}-%{release}

%description perl
perl components for the perl-Time-Duration package.


%prep
%setup -q -n Time-Duration-1.21
cd %{_builddir}
tar xf %{_sourcedir}/libtime-duration-perl_1.20-1.debian.tar.xz
cd %{_builddir}/Time-Duration-1.21
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Time-Duration-1.21/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Time-Duration
cp %{_builddir}/Time-Duration-1.21/LICENSE %{buildroot}/usr/share/package-licenses/perl-Time-Duration/00f3e582f2a5ef8a04d655ac858ff47dbec2042e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Time::Duration.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Time-Duration/00f3e582f2a5ef8a04d655ac858ff47dbec2042e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
