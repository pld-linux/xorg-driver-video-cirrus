Summary:	X.org video driver for Cirrus Logic video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych Cirrus Logic
Name:		xorg-driver-video-cirrus
Version:	1.0.0.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/driver/xf86-video-cirrus-%{version}.tar.bz2
# Source0-md5:	5f12d5bbe1d8cf3774dd9833af325d25
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Cirrus Logic video chips.

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych Cirrus Logic.

%prep
%setup -q -n xf86-video-cirrus-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

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
%doc ChangeLog README.multihead
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_alpine.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/cirrus_laguna.so
%{_mandir}/man4/cirrus.4*
