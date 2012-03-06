Summary: GNOME XML documentation utilities
Name: yelp-xsl
Version: 3.2.1
Release: 1
License: LGPLv2+ and GPLv2+
Group: Publishing
Url: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildArch: noarch
BuildRequires: 		intltool
BuildRequires: 		itstool
BuildRequires: 		xsltproc
BuildRequires: 		pkgconfig(libxslt)

%description
yelp-xsl is a collection of documentation utilities for the Gnome
project.  Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT stylesheets that were once distributed with Yelp.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %{name}.lang
%makeinstall_std

%files
%doc AUTHORS README
%{_datadir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
