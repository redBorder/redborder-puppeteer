%global debug_package %{nil}

Name:    puppeteer-rpm
Version: %{__version}
Release: %{__release}%{?dist}
Summary: Puppeteer RPM Package

License: MIT
URL: https://github.com/redBorder/puppeteer-rpm
Source0: %{name}-%{version}.tar.gz
Source1: puppeteer-19.5.2.tar.gz

BuildRequires: nodejs >= 16 npm
Requires: nodejs >= 16 npm

%description
Puppeteer RPM Package with all necessary dependencies for offline installation.

%prep
%setup -qn %{name}-%{version}

%build
tar -xzvf %{SOURCE1}

%install
mkdir -p %{buildroot}/var/www/rb-rails/node_modules/
cp -r node_modules/* %{buildroot}/var/www/rb-rails/node_modules/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/var/www/rb-rails/node_modules/

%changelog
* Tue Jul 26 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.3-1
- 
* Tue Jul 23 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.2-1
- Update URL, include all node_modules and update Requires
* Mon Jul 22 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.1-1
- Changed Puppeteer Core to Puppeteer, renamed RPM and got rid of Chromium RPM
* Tue Jul 09 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.0-1
- first spec version