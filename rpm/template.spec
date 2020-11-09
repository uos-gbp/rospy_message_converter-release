%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rospy-message-converter
Version:        0.5.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rospy_message_converter package

License:        BSD
URL:            http://ros.org/wiki/rospy_message_converter
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rospy
Requires:       ros-noetic-std-msgs
BuildRequires:  python3-numpy
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Converts between Python dictionaries and JSON to rospy messages.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon Nov 09 2020 Martin Günther <martin.guenther@dfki.de> - 0.5.5-1
- Autogenerated by Bloom

* Tue Oct 13 2020 Martin Günther <martin.guenther@dfki.de> - 0.5.4-1
- Autogenerated by Bloom

* Thu Aug 20 2020 Martin Günther <martin.guenther@dfki.de> - 0.5.3-1
- Autogenerated by Bloom

* Thu Jul 09 2020 Martin Günther <martin.guenther@dfki.de> - 0.5.2-1
- Autogenerated by Bloom

* Mon May 25 2020 Martin Günther <martin.guenther@dfki.de> - 0.5.1-1
- Autogenerated by Bloom

