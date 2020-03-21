Name:           dbox
Version:        1.0
Release:        1%{?dist}
Summary:        Tool for developing software in containers
License:        GPLv2.0+
URL:            https://github.com/dmach/dbox
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       git-core
Requires:       podman
Requires:       python3dist(argcomplete)


%description
Tool for developing, building, testing and debugging software in unprivileged Podman containers


%files
%{_bindir}/*
%{python3_sitelib}/*
%license gpl-2.0.txt


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%changelog
