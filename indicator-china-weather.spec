%define debug_package %{nil}
Name:           indicator-china-weather
Version:        3.1.0
Release:        16
Summary:        The weather data are from the heweather API s6 version.
License:        GPL-3.0+
URL:            https://github.com/UbuntuKylin/indicator-china-weather
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qtchooser
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconf
BuildRequires:  libX11-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  GeoIP-devel

# Requires: NetworkManager

patch0: fix-gsetting-issue.patch
patch1: fix-auto-get-location.patch
patch2: 0002-Modified-kylin-weather-display-is-incomplete.patch
patch3: 0003-add-X-UKUI-AutoRestart-filed-in-desktop.patch
patch4: 0004-update-translation-file.patch
patch5: 0005-Increase-the-drag-bar-of-forecast-part.patch
patch6: 0006-Hide-tray-icon-in-case-of-network-exception.patch
patch7: 0007-Repair-menu-button-hover-style-exception.patch
patch8: 0008-Solve-the-problem-of-button-backlighting.patch
patch9: 0009-Update-ts-file-and-add-today-translation.patch

%description
 Indicator that displays China weather information
 Kylin Weather displays detail weather information for one place,
 including weather forecast and observe weather, and you can
 change it.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  indicator-china-weather.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/bin/
mkdir -p %{buildroot}/usr/share/doc/indicator-china-weather/
mkdir -p %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/indicator-china-weather/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/indicator-china-weather/changelog.gz
gzip -c man/indicator-china-weather.1	> %{buildroot}/usr/share/man/man1/indicator-china-weather.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/xdg/autostart/indicator-china-weather.desktop
%{_bindir}/indicator-china-weather
%{_datadir}/applications/indicator-china-weather.desktop
%{_datadir}/doc/indicator-china-weather/changelog.gz
%{_datadir}/doc/indicator-china-weather/copyright
%{_datadir}/glib-2.0/schemas/org.china-weather-data.gschema.xml
%{_datadir}/indicator-china-weather/translations/indicator-china-weather_bo.qm
%{_datadir}/indicator-china-weather/translations/indicator-china-weather_zh_CN.qm
%{_datadir}/man/man1/indicator-china-weather.1.gz

%changelog
* Wed Jul 13 2022 tanyulong <tanyulong@kylinos.cn> - 3.1.0-16
- Update ts file and add today translation

* Mon Jul 11 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-15
- 解决按钮反白的问题

* Wed Jun 29 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-14
- 修复菜单按钮hover样式异常

* Wed Jun 29 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-13
- 网络异常情况下隐藏托盘icon

* Tue Jun 28 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-12
- Increase the drag bar of forecast part

* Mon Jun 27 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-11
- update translation file

* Fri Jun 24 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-10
- add-X-UKUI-AutoRestart filed in desktop

* Fri Jun 24 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.0-9
- Modified kylin-weather display is incomplete

* Mon Jan 10 2022 douyan <douyan@kylinos.cn> - 3.1.0-8
- add fix-auto-get-location.patch

* Wed Dec 8 2021 douyan <douyan@kylinos.cn> - 3.1.0-7
- update to upstream version 3.1.0-36
- fix open failed caused by gsetting

* Tue Dec 7 2021 douyan <douyan@kylinos.cn> - 3.1.0-6
- update to upstream version 3.1.0-34

* Thu Oct 28 2021 douyan <douyan@kylinos.cn> - 3.1.0-5
- fetch upstream release to 3.1.0-33

* Wed Oct 27 2021 douyan <douyan@kylinos.cn> - 3.1.0-4
- fix city name display issue when offline

* Tue Oct 26 2021 douyan <douyan@kylinos.cn> - 3.1.0-3
- fix vnc show issue

* Tue Jan 19 2021 lvhan <lvhan@kylinos.cn> - 3.1.0-2
- remove about

* Wed Dec 30 2020 lvhan <lvhan@kylinos.cn> - 3.1.0-1
- update to upstream version 3.1.0-32
