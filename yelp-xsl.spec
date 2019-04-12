%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME XML documentation utilities
Name:		yelp-xsl
Version:	3.32.1
Release:	1
License:	LGPLv2+ and GPLv2+
Group:		Publishing
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-xsl/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires:	python2-libxml2
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires: 	xsltproc
BuildRequires: 	pkgconfig(libxslt)

%description
yelp-xsl is a collection of documentation utilities for the Gnome
project.  Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT stylesheets that were once distributed with Yelp.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS README
%{_datadir}/%{name}

%files devel
%{_datadir}/pkgconfig/%{name}.pc

