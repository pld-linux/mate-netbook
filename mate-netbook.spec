Summary:	Simple window management tool
Summary(pl.UTF-8):	Proste narzędzie do zarządzania oknami
Name:		mate-netbook
Version:	1.26.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	9eb98f9009b7b3791da3965130e3e100
URL:		https://wiki.mate-desktop.org/mate-desktop/components/mate-netbook/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libfakekey-devel
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libwnck-devel >= 3.0
BuildRequires:	mate-panel-devel >= 1.17.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.50.0
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.22
Requires:	mate-panel >= 1.17.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# use the same libexecdir as mate-panel
# (better solution: store mate-panel libexecdir in libmatepanelapplet-*.pc and read it here)
%define		matepanel_libexecdir	%{_libexecdir}/mate-panel

%description
A simple window management tool which:
- allows you to set basic rules for a window type, such as maximise
  or undecorate
- allows exceptions to the rules, based on string matching for window
  name and window class
- allows 'reversing' of rules when the user manually changes
  something:
  - re-decorates windows on un-maximise

%description -l pl.UTF-8
Proste narzędzie do zarządzania oknami, które:
- pozwala na ustawianie podstawowych reguł dla typu okna, takich jak
  maksymalizacja lub usunięcie dekoracji
- pozwala na wyjątki od reguł, w oparciu o dopasowywanie nazwy lub
  klasy okna
- pozwala na odwrócenie reguł, kiedy użytkownik coś zmieni:
  - ponownie włącza dekoracje okien przy wyłączeniu maksymalizacji

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libexecdir=%{matepanel_libexecdir} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_ES,frp,ie,jv,ku_IQ,nqo,pms}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mate-maximus
%attr(755,root,root) %{matepanel_libexecdir}/mate-window-picker-applet
/etc/xdg/autostart/mate-maximus-autostart.desktop
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWindowPickerFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.maximus.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.mate-window-picker-applet.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MateWindowPicker.mate-panel-applet
%{_datadir}/mate-panel/ui/mate-window-picker-applet-menu.xml
%{_mandir}/man1/mate-maximus.1*
