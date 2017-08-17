%define		subver	2016-01-24
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		showlogin2
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Dokuwiki Action Plugin: Show Login-Page on "Access Denied"
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/kvormweg/showlogin2/archive/v0.3.4/%{plugin}-%{subver}.tar.gz
# Source0-md5:	fff925a7012fcdc9841e8573fb5d3db3
URL:		https://www.dokuwiki.org/plugin:showlogin2
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki < 20140505
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin shows the login dialog if you try to access a page you do
not have rights for in case you are not logged in already.

%prep
%setup -qc
mv %{plugin}-*/* .

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{README.md,LICENSE}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
