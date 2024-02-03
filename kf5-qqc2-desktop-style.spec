#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.249.0
%define		qtver		5.15.2
%define		kfname		qqc2-desktop-style

Summary:	QQC2StyleBridge
Name:		kf5-%{kfname}
Version:	5.249.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	b3d3bb8fcc315707295acaf13cb21677
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf6-kirigami-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
This is a style for QtQuickControls 2 that uses QWidget's QStyle for
painting, making possible to achieve an higher deree of consistency
between QWidget-based and QML-based apps. NOTE: the application must
be a QApplication rather than a QGuiApplication instance in order for
this style to be used

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kirigami/platform/org.kde.desktop.so
%dir %{_libdir}/qt6/qml/org/kde/desktop
%{_libdir}/qt6/qml/org/kde/desktop/BusyIndicator.qml
%{_libdir}/qt6/qml/org/kde/desktop/Button.qml
%{_libdir}/qt6/qml/org/kde/desktop/CheckBox.qml
%{_libdir}/qt6/qml/org/kde/desktop/CheckDelegate.qml
%{_libdir}/qt6/qml/org/kde/desktop/ComboBox.qml
%{_libdir}/qt6/qml/org/kde/desktop/Container.qml
%{_libdir}/qt6/qml/org/kde/desktop/Control.qml
%{_libdir}/qt6/qml/org/kde/desktop/DelayButton.qml
%{_libdir}/qt6/qml/org/kde/desktop/Dial.qml
%{_libdir}/qt6/qml/org/kde/desktop/Dialog.qml
%{_libdir}/qt6/qml/org/kde/desktop/DialogButtonBox.qml
%{_libdir}/qt6/qml/org/kde/desktop/Drawer.qml
%{_libdir}/qt6/qml/org/kde/desktop/Frame.qml
%{_libdir}/qt6/qml/org/kde/desktop/GroupBox.qml
%{_libdir}/qt6/qml/org/kde/desktop/HorizontalHeaderView.qml
%{_libdir}/qt6/qml/org/kde/desktop/ItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/desktop/Label.qml
%{_libdir}/qt6/qml/org/kde/desktop/Menu.qml
%{_libdir}/qt6/qml/org/kde/desktop/MenuBar.qml
%{_libdir}/qt6/qml/org/kde/desktop/MenuBarItem.qml
%{_libdir}/qt6/qml/org/kde/desktop/MenuItem.qml
%{_libdir}/qt6/qml/org/kde/desktop/MenuSeparator.qml
%{_libdir}/qt6/qml/org/kde/desktop/Page.qml
%{_libdir}/qt6/qml/org/kde/desktop/PageIndicator.qml
%{_libdir}/qt6/qml/org/kde/desktop/Pane.qml
%{_libdir}/qt6/qml/org/kde/desktop/Popup.qml
%{_libdir}/qt6/qml/org/kde/desktop/ProgressBar.qml
%{_libdir}/qt6/qml/org/kde/desktop/RadioButton.qml
%{_libdir}/qt6/qml/org/kde/desktop/RadioDelegate.qml
%{_libdir}/qt6/qml/org/kde/desktop/RangeSlider.qml
%{_libdir}/qt6/qml/org/kde/desktop/RoundButton.qml
%{_libdir}/qt6/qml/org/kde/desktop/ScrollBar.qml
%{_libdir}/qt6/qml/org/kde/desktop/ScrollView.qml
%{_libdir}/qt6/qml/org/kde/desktop/Slider.qml
%{_libdir}/qt6/qml/org/kde/desktop/SpinBox.qml
%{_libdir}/qt6/qml/org/kde/desktop/StackView.qml
%{_libdir}/qt6/qml/org/kde/desktop/Switch.qml
%{_libdir}/qt6/qml/org/kde/desktop/SwitchDelegate.qml
%{_libdir}/qt6/qml/org/kde/desktop/TabBar.qml
%{_libdir}/qt6/qml/org/kde/desktop/TabButton.qml
%{_libdir}/qt6/qml/org/kde/desktop/TextArea.qml
%{_libdir}/qt6/qml/org/kde/desktop/TextField.qml
%{_libdir}/qt6/qml/org/kde/desktop/ToolBar.qml
%{_libdir}/qt6/qml/org/kde/desktop/ToolButton.qml
%{_libdir}/qt6/qml/org/kde/desktop/ToolSeparator.qml
%{_libdir}/qt6/qml/org/kde/desktop/ToolTip.qml
%{_libdir}/qt6/qml/org/kde/desktop/TreeViewDelegate.qml
%{_libdir}/qt6/qml/org/kde/desktop/VerticalHeaderView.qml
%{_libdir}/qt6/qml/org/kde/desktop/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/desktop/liborg_kde_desktop.so
%{_libdir}/qt6/qml/org/kde/desktop/org_kde_desktop.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/desktop/private
%{_libdir}/qt6/qml/org/kde/desktop/private/CheckIndicator.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/DefaultListItemBackground.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/DefaultSliderHandle.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/DefaultToolBarBackground.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/FocusRect.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/GlobalSonnetSettings.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/MobileCursor.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/MobileTextActionsToolBar.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/MobileTextActionsToolBarImpl.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/SwitchIndicator.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/TextFieldContextMenu.qml
%{_libdir}/qt6/qml/org/kde/desktop/private/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/desktop/private/liborg_kde_desktop_private.so
%{_libdir}/qt6/qml/org/kde/desktop/private/org_kde_desktop_private.qmltypes
%{_libdir}/qt6/qml/org/kde/desktop/private/qmldir
%{_libdir}/qt6/qml/org/kde/desktop/qmldir
%dir %{_libdir}/qt6/qml/org/kde/qqc2desktopstyle
%dir %{_libdir}/qt6/qml/org/kde/qqc2desktopstyle/private
%{_libdir}/qt6/qml/org/kde/qqc2desktopstyle/private/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/qqc2desktopstyle/private/libqqc2desktopstyleplugin.so
%{_libdir}/qt6/qml/org/kde/qqc2desktopstyle/private/qmldir
%{_libdir}/qt6/qml/org/kde/qqc2desktopstyle/private/qqc2desktopstyleplugin.qmltypes

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF6QQC2DesktopStyle
