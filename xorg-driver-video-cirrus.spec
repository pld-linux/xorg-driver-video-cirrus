Summary:	X.org video driver for Cirrus Logic video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Cirrus Logic
Name:		xorg-driver-video-cirrus
Version:	1.6.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-cirrus-%{version}.tar.xz
# Source0-md5:	75ef45cd4e747a7b2506e1f41d7236c3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.4
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.4
Provides:	xorg-driver-video
Obsoletes:	X11-driver-cirrus < 1:7.0.0
Obsoletes:	XFree86-Cirrus < 4
Obsoletes:	XFree86-driver-cirrus < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Cirrus Logic video chips.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Cirrus Logic.

%prep
%setup -q -n xf86-video-cirrus-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md README.multihead
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_drv.so
%{_mandir}/man4/cirrus.4*
