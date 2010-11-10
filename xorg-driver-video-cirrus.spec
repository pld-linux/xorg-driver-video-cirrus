Summary:	X.org video driver for Cirrus Logic video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Cirrus Logic
Name:		xorg-driver-video-cirrus
Version:	1.3.2
Release:	5
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-cirrus-%{version}.tar.bz2
# Source0-md5:	8195d03ed0be0975c03441e66a9f53b3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRequires:	xorg-xserver-server-devel >= 1.4
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.4
Obsoletes:	X11-driver-cirrus < 1:7.0.0
Obsoletes:	XFree86-Cirrus
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

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README README.multihead
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_alpine.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_laguna.so
%{_mandir}/man4/cirrus.4*
