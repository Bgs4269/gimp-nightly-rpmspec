%global major 2
%global minor 99
%global micro 16
%global binver %{major}.%{minor}
%global lib_api_version %{major}.%{minor}
%global gettext_version 30

Name:       gimp-2.99
Version:    2.99.%{micro}
Release:    7%{?dist}
Summary:    GNU Image Manipulation Program

License:    GPLv3+ and GPLv3
URL:        https://www.gimp.org/
	
Source0:    https://download.gimp.org/gimp/v2.99/gimp-2.99.%{micro}.tar.xz

# https://gitlab.gnome.org/GNOME/gimp/-/issues/9633
Patch1:    gimp-2.99-defcheck.patch
# bz#1706653
Patch2:    gimp-2.99-default-font.patch

BuildRequires:  aalib-devel
BuildRequires:  curl
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  enchant
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.19
BuildRequires:  gjs
BuildRequires:  glib-networking
BuildRequires:  gtk-doc >= 1.0
BuildRequires:  icu
BuildRequires:  intltool >= 0.40.1
BuildRequires:  libappstream-glib >= 0.7.7
BuildRequires:  libgs-devel
BuildRequires:  luajit
BuildRequires:  appstream >= 0.15.3
BuildRequires:  meson >= 0.50.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.100
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.46
BuildRequires:  pkgconfig(libjxl) >= 0.6.1
BuildRequires:  pkgconfig(alsa) >= 1.0.0
BuildRequires:  pkgconfig(appstream-glib) >= 0.7.7
BuildRequires:  pkgconfig(atk) >= 2.4.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cairo-pdf) >= 1.12.2
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(fontconfig) >= 2.12.4
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gexiv2) >= 0.14.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.10
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gutenprint)
BuildRequires:  pkgconfig(harfbuzz) >= 1.0.5
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.6
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libart-2.0) >= 2.3.19
BuildRequires:  pkgconfig(libexif) >= 0.6.15
BuildRequires:  pkgconfig(libheif) >= 1.3.2
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint) >= 1.3.0
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libpng) >= 1.6.25
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libunwind) >= 1.1.0
BuildRequires:  pkgconfig(libwebp) >= 0.6.0
BuildRequires:  pkgconfig(libwmf) >= 0.2.8
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= 1.3.0
BuildRequires:  pkgconfig(OpenEXR) >= 1.6.1
BuildRequires:  pkgconfig(pangocairo) >= 1.44.0
BuildRequires:  pkgconfig(pangoft2) >= 1.29.4
BuildRequires:  pkgconfig(poppler-data) >= 0.4.9
BuildRequires:  pkgconfig(poppler-glib) >= 0.69.0
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3) >= 3.6.0
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.20.3
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vala
BuildRequires:  perl-lib
BuildRequires:  gi-docgen
BuildRequires:  xdg-utils
BuildRequires:  xorg-x11-server-Xvfb
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Requires:       cfitsio
Recommends:     ghostscript
Recommends:     gjs
Recommends:     luajit
Recommends:     lua-lgi-compat
Recommends:     pygobject2
Recommends:     mypaint-brushes1
#Recommends:     rawtherapee
#Recommends:     darktable
Conflicts:      gimp-nightly

%description
GIMP (GNU Image Manipulation Program) is a powerful image composition and
editing program, which can be extremely useful for creating logos and other
graphics for web pages. GIMP has many of the tools and filters you would expect
to find in similar commercial offerings, and some interesting extras as well.
GIMP provides a large image manipulation toolbox, including channel operations
and layers, effects, sub-pixel imaging and anti-aliasing, and conversions, all
with multi-level undo.

%package data
Summary:        GIMP data files
License:        LGPLv3+
Requires:       %{name}-data = %{version}-%{release}
BuildArch:      noarch
Conflicts:      gimp-nightly-data

%description data
The %{name}-data package contains data files needed for the GNU Image
Manipulation Program (GIMP).

%package libs
Summary:        GIMP libraries
License:        LGPLv3+
Conflicts:      gimp-nightly-libs

%description libs
The %{name}-libs package contains shared libraries needed for the GNU Image
Manipulation Program (GIMP).

%package devel
Summary:        GIMP plugin and extension development kit
License:        LGPLv3+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel-tools = %{version}-%{release}
Conflicts:      gimp-nightly-devel

%description devel
The %{name}-devel package contains the static libraries and header files
for writing GNU Image Manipulation Program (GIMP) plug-ins and
extensions.

%package devel-doc
Summary:        GIMP plugin and extension development documentation
License:        LGPLv3+
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch
Conflicts:      gimp-nightly-devel-doc

%description devel-doc
The %{name}-devel-doc package contains documentation to
build GNU Image Manipulation Program (GIMP) plug-ins and extensions.

%package devel-tools
Summary:        GIMP plugin and extension development tools
License:        LGPLv3+
Requires:       %{name}-devel = %{version}-%{release}
Conflicts:      gimp-nightly-devel-tools

%description devel-tools
The %{name}-devel-tools package contains gimptool, a helper program to
build GNU Image Manipulation Program (GIMP) plug-ins and extensions.

%prep
%autosetup -p1 -n gimp-2.99.%{micro}

%build
%meson -Dpython=enabled -Dbug-report-url=https://github.com/uriesk/gimp-nightly-rpmspec/issues --buildtype=release
%meson_build

%install
%meson_install

# Plugins and modules change often (grab the executeable ones)
find %{buildroot}%{_libdir}/gimp/%{lib_api_version} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{lib_api_version}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files

# Auto detect the lang files
%find_lang gimp%{gettext_version}
%find_lang gimp%{gettext_version}-std-plug-ins
%find_lang gimp%{gettext_version}-script-fu
%find_lang gimp%{gettext_version}-libgimp
# No lang files found for tips with 2.99.16
# %find_lang gimp%{gettext_version}-tips
%find_lang gimp%{gettext_version}-python

# cat gimp%{gettext_version}.lang gimp%{gettext_version}-std-plug-ins.lang gimp%{gettext_version}-script-fu.lang gimp%{gettext_version}-libgimp.lang gimp%{gettext_version}-tips.lang gimp%{gettext_version}-python.lang > gimp-all.lang
cat gimp%{gettext_version}.lang gimp%{gettext_version}-std-plug-ins.lang gimp%{gettext_version}-script-fu.lang gimp%{gettext_version}-libgimp.lang gimp%{gettext_version}-python.lang > gimp-all.lang
# Build the master filelists generated from the above mess.
cat gimp-plugin-files gimp-all.lang > gimp.files

# remove unversioned files for compatibility with stable gimp
rm -f %{buildroot}%{_mandir}/man1/gimp.1*
rm -f %{buildroot}%{_mandir}/man1/gimp-console.1*
rm -f %{buildroot}%{_mandir}/man5/gimprc.5*
rm -f %{buildroot}%{_mandir}/man1/gimptool.1*
rm -f %{buildroot}%{_bindir}/gimp
rm -f %{buildroot}%{_bindir}/gimp-console
rm -f %{buildroot}%{_bindir}/gimp-test-clipboard
rm -f %{buildroot}%{_bindir}/gimptool
rm -f %{buildroot}%{_libexecdir}/gimp-debug-tool

# desktop file -- mention version and name it accordingly
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    --set-name="GIMP Beta %{major}.%{minor}" \
    --set-icon="gimp%{major}%{minor}" \
    %{buildroot}%{_datadir}/applications/gimp.desktop
sed -i 's/org\.gimp\.GIMP/org.gimp.GIMP299/g' %{buildroot}%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
mv -f %{buildroot}%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml \
    %{buildroot}%{_datadir}/metainfo/org.gimp.GIMP%{major}%{minor}.appdata.xml
mv -f %{buildroot}%{_datadir}/applications/gimp.desktop \
    %{buildroot}%{_datadir}/applications/org.gimp.GIMP%{major}%{minor}.desktop

# rename icons to include version
mv -f %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/gimp.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/gimp%{major}%{minor}.svg
pushd %{buildroot}%{_datadir}/icons/hicolor
for srcicon in */apps/gimp.png; do
    geo=${srcicon%%%%/*}
    destdir="%{buildroot}%{_datadir}/icons/hicolor/$geo/apps"
    desticon="$destdir/gimp%{major}%{minor}.png"
    mkdir -p "$destdir"
    # here we could modify the icons
    mv -f "$srcicon" "$desticon"
done
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstreamcli validate --no-color %{buildroot}%{_datadir}/metainfo/*.xml
find %{buildroot}%{_datadir}

%files -f gimp.files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/gimp-%{binver}
%{_bindir}/gimp-console-%{binver}
%{_bindir}/gimp-script-fu-interpreter-3.0
%{_bindir}/gimp-test-clipboard-%{lib_api_version}
%{_libdir}/libgimp-scriptfu-3.0.so.0*
%{_libexecdir}/gimp-debug-tool-%{lib_api_version}

%{_mandir}/man1/gimp-%{binver}.1*
%{_mandir}/man1/gimp-console-%{binver}.1*
%{_mandir}/man5/gimprc-%{binver}.5*

%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/%{lib_api_version}
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/controllerrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/gimprc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/gimp.css
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/unitrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/sessionrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/templaterc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/toolrc

%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{lib_api_version}
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gimp-3.0.typelib
%{_libdir}/girepository-1.0/GimpUi-3.0.typelib

%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/icons/hicolor/*/apps/gimp%{major}%{minor}.png
%{_datadir}/icons/hicolor/scalable/apps/gimp%{major}%{minor}.svg

%files data
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{lib_api_version}
%{_datadir}/gimp/%{lib_api_version}/dynamics/
%{_datadir}/gimp/%{lib_api_version}/file-raw/
%{_datadir}/gimp/%{lib_api_version}/menus/
%{_datadir}/gimp/%{lib_api_version}/tags/
%{_datadir}/gimp/%{lib_api_version}/tips/
%{_datadir}/gimp/%{lib_api_version}/tool-presets/
%{_datadir}/gimp/%{lib_api_version}/fonts/
%{_datadir}/gimp/%{lib_api_version}/brushes/
%{_datadir}/gimp/%{lib_api_version}/fractalexplorer/
%{_datadir}/gimp/%{lib_api_version}/gfig/
%{_datadir}/gimp/%{lib_api_version}/gflare/
%{_datadir}/gimp/%{lib_api_version}/gimpressionist/
%{_datadir}/gimp/%{lib_api_version}/gradients/
%{_datadir}/gimp/%{lib_api_version}/icons/
%{_datadir}/gimp/%{lib_api_version}/images/
%{_datadir}/gimp/%{lib_api_version}/palettes/
%{_datadir}/gimp/%{lib_api_version}/patterns/
%{_datadir}/gimp/%{lib_api_version}/scripts/
%{_datadir}/gimp/%{lib_api_version}/themes/
%{_datadir}/gimp/%{lib_api_version}/gimp-release

%files libs
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libgimp-3.0.so.0*
%{_libdir}/libgimpbase-3.0.so.0*
%{_libdir}/libgimpcolor-3.0.so.0*
%{_libdir}/libgimpconfig-3.0.so.0*
%{_libdir}/libgimpmath-3.0.so.0*
%{_libdir}/libgimpmodule-3.0.so.0*
%{_libdir}/libgimpthumb-3.0.so.0*
%{_libdir}/libgimpui-3.0.so.0*
%{_libdir}/libgimpwidgets-3.0.so.0*

%files devel
%doc README.i18n
%{_libdir}/*.so
%{_includedir}/gimp-3.0
%{_libdir}/pkgconfig/*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gimp-3.0.gir
%{_datadir}/gir-1.0/GimpUi-3.0.gir
%{_datadir}/vala/vapi/gimp-3.0.*
%{_datadir}/vala/vapi/gimp-ui-3.0.*

%files devel-doc
%doc %{_datadir}/doc/gimp-%{binver}

%files devel-tools
%{_bindir}/gimptool-%{lib_api_version}
%{_mandir}/man1/gimptool-%{lib_api_version}.1*

%changelog
* Sat Jul 22 19:29:00 CEST 2023 uriesk <uriesk@posteo.de> - 2.99.16
- Update to 2.99.16

* Fri Dec 11 02:51:57 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.2-1
- Update to 2.99.2

* Sun Aug 23 15:51:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.2-0.2.20200823git56982e
- Bump to commit 56982e6ce96d34b0802f90b5dd0606565f6b3914

* Mon Jul 20 22:05:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.99.1-0.1.20200720git1a7a53d
- Initial package for GIMP 2.99

