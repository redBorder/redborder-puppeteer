Name:    puppeteer-rpm
Version: %{__version}
Release: %{__release}%{?dist}
Summary: Puppeteer Core

License: MIT and BSD
URL: https://github.com/puppeteer/puppeteer
Source0: %{name}-%{version}.tar.gz

BuildRequires: nodejs npm
Requires: nodejs npm

%global debug_package %{nil}

%description
This package includes Puppeteer, a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol.

%prep
%setup -qn %{name}-%{version}

%build
npm install puppeteer@19.5.2 --no-save

%install
echo %{buildroot}
mkdir -p %{buildroot}/var/www/rb-rails/node_modules/puppeteer-rpm
cp -r node_modules/puppeteer %{buildroot}/var/www/rb-rails/node_modules/puppeteer-rpm/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/var/www/rb-rails/node_modules/puppeteer-rpm

%changelog
* Tue Jul 22 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.1-1
- Changed Puppeteer Core to Puppeteer, renamed RPM and got rid of Chromium RPM
* Tue Jul 09 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.0-1
- first spec version