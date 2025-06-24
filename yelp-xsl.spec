%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME XML documentation utilities
Name:		yelp-xsl
Version:	42.4
Release:	1
License:	LGPLv2+ and GPLv2+
Group:		Publishing
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/yelp-xsl/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires:  meson
BuildRequires:	python-libxml2
BuildRequires:  libxml2-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires: 	xsltproc
BuildRequires: 	pkgconfig(libxslt)

%patchlist
# https://www.phoronix.com/news/GNOME-Yelp-Security-Issue-2025
# https://gitlab.gnome.org/GNOME/yelp/-/issues/221
#https://gitlab.gnome.org/-/project/1541/uploads/c96d62a9df3b77056e254f861c52bf5c/yelp-xsl.patch

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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS README*
%{_datadir}/%{name}

%files devel
%{_datadir}/pkgconfig/%{name}.pc

