%global debug_package %{nil}

Name:		bindfs
Version:	1.18.1
Release:	1
Source0:	https://github.com/mpartel/bindfs/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	FUSE filesystem for mirroring a directory to another directory
URL:		https://github.com/mpartel/bindfs
License:	GPLv2+
Group:		System/Base

BuildRequires:	make
BuildRequires:  lib64fuse3-devel
BuildRequires:  recode

%description
Bindfs allows you to mirror a directory and also change the the permissions in
the mirror directory.

%prep
%setup -q
recode latin1..utf8 ChangeLog


%build
autoreconf -fi
%configure2_5x
%make LIBS="-lpthread"

%install
%makeinstall_std

%files
%doc COPYING ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
