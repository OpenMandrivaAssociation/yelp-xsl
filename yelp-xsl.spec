%define name yelp-xsl
%define version 3.4.2
%define release %mkrel 1

Summary: GNOME XML documentation utilities
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
License: LGPLv2+ and GPLv2+
Group: Publishing
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: 		libxslt-devel
BuildRequires: 		libxslt-proc
BuildRequires: 		intltool
BuildRequires:		itstool

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
rm -rf %{buildroot} %name.lang
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%_datadir/%name
%_datadir/pkgconfig/%name.pc


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.31.6-2mdv2011.0
+ Revision: 671943
- mass rebuild

* Tue Nov 09 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 595423
- update to new version 2.31.6

* Mon Jul 12 2010 Götz Waschk <waschk@mandriva.org> 2.31.5-1mdv2011.0
+ Revision: 551280
+ rebuild (emptylog)

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 0.20.1-1mdv2010.1
+ Revision: 539205
- update to new version 0.20.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 528901
- update to new version 0.20.0

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 0.19.5-1mdv2010.1
+ Revision: 509415
- update to new version 0.19.5

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 0.19.4-1mdv2010.1
+ Revision: 502719
- update to new version 0.19.4

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 0.19.3-1mdv2010.1
+ Revision: 496504
- update to new version 0.19.3

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 0.19.2-1mdv2010.1
+ Revision: 489965
- update to new version 0.19.2

* Wed Jan 06 2010 Götz Waschk <waschk@mandriva.org> 0.19.1-1mdv2010.1
+ Revision: 486562
- update to new version 0.19.1

* Sat Nov 21 2009 Götz Waschk <waschk@mandriva.org> 0.18.1-1mdv2010.1
+ Revision: 467788
- update to new version 0.18.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 446698
- update to new version 0.18.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 0.17.5-1mdv2010.0
+ Revision: 437419
- update to new version 0.17.5

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.17.4-1mdv2010.0
+ Revision: 420778
- disable parallel build
- update to new version 0.17.4

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 0.17.3-1mdv2010.0
+ Revision: 401407
- update to new version 0.17.3

* Sun Jun 28 2009 Götz Waschk <waschk@mandriva.org> 0.17.2-1mdv2010.0
+ Revision: 390427
- update build deps
- new version
- update file list

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 0.17.1-1mdv2010.0
+ Revision: 385964
- update to new version 0.17.1

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 0.16.1-1mdv2009.1
+ Revision: 367218
- update to new version 0.16.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 356129
- update to new version 0.16.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 0.15.2-1mdv2009.1
+ Revision: 346878
- update to new version 0.15.2

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 0.15.1-1mdv2009.1
+ Revision: 336344
- update to new version 0.15.1

* Sat Jan 10 2009 Götz Waschk <waschk@mandriva.org> 0.14.2-1mdv2009.1
+ Revision: 327957
- update to new version 0.14.2

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 0.14.1-1mdv2009.1
+ Revision: 315788
- update to new version 0.14.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2009.0
+ Revision: 287253
- new version
- update license

* Thu Aug 28 2008 Götz Waschk <waschk@mandriva.org> 0.13.1-1mdv2009.0
+ Revision: 276871
- new version
- fix build

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.12.2-2mdv2009.0
+ Revision: 221086
- rebuild

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 0.12.2-1mdv2008.1
+ Revision: 183223
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 0.12.1-1mdv2008.1
+ Revision: 166379
- new version
- rediff the patch

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.12.0-2mdv2008.1
+ Revision: 150139
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2008.0
+ Revision: 89360
- new version

* Sun Aug 19 2007 Götz Waschk <waschk@mandriva.org> 0.11.2-1mdv2008.0
+ Revision: 67038
- new version
- fix build

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 0.11.1-2mdv2008.0
+ Revision: 57362
- depend on docbook DTDs

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2008.0
+ Revision: 56702
- fix buildrequires
- new version
- fix aclocal call

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdv2008.0
+ Revision: 14134
- new version

