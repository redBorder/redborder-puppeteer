%global debug_package %{nil}

Name:    puppeteer-rpm
Version: %{__version}
Release: %{__release}%{?dist}
Summary: Puppeteer RPM Package

License: MIT
URL: https://github.com/redBorder/puppeteer-rpm
Source0: %{name}-%{version}.tar.gz
Source1: puppeteer-19.5.2-2.tar.gz
Source2: chromium-linux-1069273.tar.gz

BuildRequires: nodejs >= 16 npm
Requires: nodejs >= 16 npm

%description
Puppeteer RPM Package with all necessary dependencies for offline installation.

%prep
%setup -qn %{name}-%{version}

%build
tar -xzvf %{SOURCE1}
tar -xzvf %{SOURCE2}

%install
mkdir -p %{buildroot}/var/www/rb-rails/node_modules/
cp -r node_modules/* %{buildroot}/var/www/rb-rails/node_modules/
mkdir -p %{buildroot}/var/www/rb-rails/.cache/puppeteer/chrome/linux-1069273/
cp -r chrome-linux/* %{buildroot}/var/www/rb-rails/.cache/puppeteer/chrome/linux-1069273/

%clean
rm -rf %{buildroot}

%files
%defattr(-,webui,webui)
/var/www/rb-rails/node_modules/
/var/www/rb-rails/.cache/puppeteer

%changelog
* Tue Jul 26 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.3-1
- Include Chromium binary and dependencies for offline reproducibility
* Tue Jul 23 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.2-1
- Update URL, include all node_modules and update Requires
* Mon Jul 22 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.1-1
- Changed Puppeteer Core to Puppeteer, renamed RPM and got rid of Chromium RPM
* Tue Jul 09 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.0-1
- first spec version