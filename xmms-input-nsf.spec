Summary:	NSF Input plugin for xmms
Summary(pl):	Wtyczka wej¶cia NSF dla xmms
Name:		xmms-input-nsf
Version:	0.0.3
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.geocities.co.jp/SiliconValley-SanJose/2956/RPMS/xmms-nsf-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	x11amp-nsf xmms-nsf

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xmms-nsf iutput plugin for xmms.

%description -l pl
Wtyczka wej¶cia NSF dla xmms.

%prep
%setup -q -n xmms-nsf-%{version}

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.jp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%lang(jp) %doc README.jp.gz
%{_libdir}/xmms/Input/libnsf.so
