%include	/usr/lib/rpm/macros.php
%define		_class		Testing
%define		_subclass	FIT
%define		_status		beta
%define		_pearname	Testing_FIT
Summary:	%{_pearname} - FIT: Framework for Integrated Test
Summary(pl.UTF-8):	%{_pearname} - FIT: Framework do zintegrowanych testów
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4778f17d031296b2ef3235745681fe4c
URL:		http://pear.php.net/package/Testing_FIT/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Great software requires collaboration and communication.

Fit is a tool for enhancing collaboration in software development.
It's an invaluable way to collaborate on complicated problems--and get
them right--early in development.

Fit allows customers, testers, and programmers to learn what their
software should do and what it does do. It automatically compares
customers' expectations to actual results.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Większe programy wymagają współpracy i komunikacji.

Fit jest narzędziem usprawniającym współpracę na etapie rozwoju
oprogramowania. Jest szczególnie przydatny przy współpracy nad
złożonymi problemami - oraz rozwiązywaniu ich - na wczesnym etapie
rozwoju.

Fit pozwala klientom, testerom i programistom stwierdzenie jaką
funkcjonalność oprogramowanie powinno udostępniać oraz jaką
udostępnia, a następnie porównanie otrzymanie wyników.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Testing_FIT
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Testing/FIT
