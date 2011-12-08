%define		plugin		showlogin2
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Dokuwiki Action Plugin: Show Login-Page on "Access Denied"
Name:		dokuwiki-plugin-%{plugin}
Version:	20091017
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.tu-harburg.de/~psvkv/dokuwiki/showlogin2.tar.gz
# Source0-md5:	806c00de984b15e1aac9bee1c4f4c879
URL:		http://www.dokuwiki.org/plugin:showlogin2
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
Requires:	php-common >= 4:%{php_min_version}
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
mv %{plugin}/* .

version=$(awk -F"'" '/date/&&/=>/{print $4}' action.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
