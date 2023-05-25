%define libname %mklibname KF6Declarative
%define devname %mklibname KF6Declarative -d
%define git 20230526

Name: kf6-kdeclarative
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kdeclarative/-/archive/master/kdeclarative-master.tar.bz2#/kdeclarative-%{git}.tar.bz2
Summary: Integration of QML and KDE work spaces
URL: https://invent.kde.org/frameworks/kdeclarative
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6WidgetsAddons)
Requires: %{libname} = %{EVRD}

%description
Integration of QML and KDE work spaces

%package -n %{libname}
Summary: Integration of QML and KDE work spaces
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Integration of QML and KDE work spaces

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Integration of QML and KDE work spaces

%prep
%autosetup -p1 -n kdeclarative-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang

%files -n %{devname}
%{_includedir}/KF6/KDeclarative
%{_libdir}/cmake/KF6Declarative
%{_qtdir}/doc/KF6Declarative.*

%files -n %{libname}
%{_libdir}/libKF6CalendarEvents.so*
%{_qtdir}/qml/org/kde/draganddrop
%{_qtdir}/qml/org/kde/graphicaleffects
%{_qtdir}/qml/org/kde/kcm
%{_qtdir}/qml/org/kde/kquickcontrols
%{_qtdir}/qml/org/kde/kquickcontrolsaddons
%{_qtdir}/qml/org/kde/private/kquickcontrols
