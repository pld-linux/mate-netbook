#
# Conditional build:
%bcond_with	gtk3		# use GTK+ 3.x instead of 2.x

Summary:	Simple window management tool
Summary(pl.UTF-8):	Proste narzędzie do zarządzania oknami
Name:		mate-netbook
Version:	1.16.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.16/%{name}-%{version}.tar.xz
# Source0-md5:	e1365a9039e361e86d744192a71e1028
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.36.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libfakekey-devel
BuildRequires:	libtool >= 1:1.4.3
%{?with_gtk3:BuildRequires:	libwnck-devel >= 3.0}
%{!?with_gtk3:BuildRequires:	libwnck2-devel >= 1.0}
BuildRequires:	mate-panel-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	glib2 >= 1:2.36.0
Requires:	mate-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_gtk3:--with-gtk=3.0}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,jv}

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
%attr(755,root,root) %{_libexecdir}/mate-window-picker-applet
/etc/xdg/autostart/mate-maximus-autostart.desktop
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWindowPickerFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.maximus.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.mate-window-picker-applet.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MateWindowPicker.mate-panel-applet
%{_datadir}/mate-panel/ui/mate-window-picker-applet-menu.xml
%{_mandir}/man1/mate-maximus.1*
