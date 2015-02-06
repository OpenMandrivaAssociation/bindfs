Name:           bindfs
Version:        1.12.2
Release:        2
Summary:        Fuse filesystem to mirror a directory

Group:          System/Base
License:        GPLv2+
URL:            http://code.google.com/p/bindfs/
Source0:        http://bindfs.googlecode.com/files/bindfs-%{version}.tar.gz

BuildRequires:  fuse-devel
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
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
