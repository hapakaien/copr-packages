Name: 		pnpm
Version: 	7.18.2
Release: 	1%{?dist}
License:	MIT
Summary: 	Fast, disk space efficient package manager
Url: 		https://github.com/pnpm/pnpm
Source0: 	%{url}/releases/download/v%{version}/pnpm-linux-x64

BuildArch: x86_64

%description
When using npm, if you have 100 projects using a dependency, you will have 100 
copies of that dependency saved on disk. With pnpm, the dependency will be 
stored in a content-addressable store.

#-- INSTALL -------------------------------------------------------------------#
%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{_sourcedir}/pnpm-linux-x64 %{buildroot}%{_bindir}/pnpm

#-- FILES ---------------------------------------------------------------------#
%files
%{_bindir}/pnpm

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Dec 18 2022 Ahmad Husen <hi@husen.id> 7.18.2-1
- new package built with tito

* Sun Dec 18 2022 A. Husen <hi@husen.id> - 7.18.2
- Release v7.18.2

