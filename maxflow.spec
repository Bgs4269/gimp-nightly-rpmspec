%define major 0

Name:           libmaxflow
Version:        3.0.5
Release:        1
Summary:        Software for computing mincut/maxflow in a graph
License:        GPLv3+
URL:            https://github.com/gerddie/maxflow
Source0:        https://github.com/gerddie/maxflow/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
This library implements an efficient minimum cut/maximum flow algorithms
on graphs that can be used for exact or approximate energy minimization
in low-level vision. The algorithm provides a high performance that makes
near real-time performance possible.

%package devel
Summary:        Header files for %{name}
License:        GPLv3+
Requires:       %{name} = %{version}-%{release}

%description devel
This library implements an efficient minimum cut/maximum flow algorithms
on graphs that can be used for exact or approximate energy minimization
in low-level vision. The algorithm provides a high performance that makes
near real-time performance possible.

%prep
%autosetup -p1 -n maxflow-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGES.TXT README.md
%license GPL.TXT
%{_libdir}/libmaxflow.so.%{major}{,.*}

%files devel
%{_libdir}/libmaxflow.so
%{_libdir}/pkgconfig/maxflow.pc
%dir %{_includedir}/maxflow-3.0
%{_includedir}/maxflow-3.0/maxflow.h
%dir %{_includedir}/maxflow-3.0/maxflow
%{_includedir}/maxflow-3.0/maxflow/block.h
%{_includedir}/maxflow-3.0/maxflow/graph.h
%{_includedir}/maxflow-3.0/maxflow/graph.cpp

%changelog
* Sat Jul 22 19:29:00 CEST 2023 uriesk <uriesk@posteo.de> - 3.0.5
- initial build
