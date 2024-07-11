Name:    redborder-puppeteer
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: x86_64
Summary: Puppeteer Core and Chromium RPM

License: MIT and BSD
URL: https://github.com/puppeteer/puppeteer
Source0: %{name}-%{version}.tar.gz
Source1: chromium-126.0.6478.126-1.fc41.x86_64.rpm

BuildRequires: nodejs
BuildRequires: npm
Requires: nodejs

%global debug_package %{nil}

%description
This package includes both Puppeteer Core, a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol, and Chromium, an open-source web browser project.

%prep
%setup -qn %{name}-%{version}

%build
npm install puppeteer-core@19.6.3 --no-save

%install
echo %{buildroot}
echo %{SOURCE1}
mkdir -p %{buildroot}/usr/lib/node_modules/redborder-puppeteer
cp -r node_modules/puppeteer-core %{buildroot}/usr/lib/node_modules/redborder-puppeteer/
mkdir -p %{buildroot}/usr/src
cp %{SOURCE1} %{buildroot}/usr/src/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/node_modules/redborder-puppeteer
/usr/src/chromium-126.0.6478.126-1.fc41.x86_64.rpm

%changelog
* Tue Jul 09 2024 Daniel C. Cruz <dcastro@redborder.com> - 1.0-1
- first spec version