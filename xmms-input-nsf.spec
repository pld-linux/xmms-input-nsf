%define name    @PACKAGE@
%define version @VERSION@
%define release 1
%define serial  1
%define input_plugin_dir @XMMS_INPUT_PLUGIN_DIR@

Summary:        NSF Input plugin for xmms
Name:           %{name}
Version:        %{version}
Release:        %{release}
Serial:         %{serial}
Copyright:      GPL
Group:          Applications/Multimedia
Source:         xmms-nsf-%{version}.tar.gz
Requires:       xmms >= 1.0
BuildRoot:      /var/tmp/%{name}-%{version}
Obsoletes:      x11amp-nsf xmms-nsf
NoSource:       0

%description
xmms-nsf iutput plugin for xmms.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%post
/sbin/ldconfig  

%postun -p /sbin/ldconfig 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README README.jp
%{input_plugin_dir}/libnsf.la
%{input_plugin_dir}/libnsf.so

%changelog
* Mon Jul 3 2000 Shinya Uchimaki <abekiti@mbg.sphere.ne.jp>
- 1st release.
