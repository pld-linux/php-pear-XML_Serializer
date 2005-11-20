%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Serializer
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - class to build XML documents from data structures
Summary(pl):	%{_pearname} - klasa do tworzenia dokumentów XML ze struktur danych
Name:		php-pear-%{_pearname}
Version:	0.18.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f9d7dd792a7b3258dfa4544017734cf8
URL:		http://pear.php.net/package/XML_Serializer/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Util >= 1.1.1
Requires:	php-pear-XML_Parser >= 1.2.6
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} serializes complex data structures like arrays or objects
as XML documents. This class helps you generating any XML document you
require without the need for DOM.

In PEAR status of this package is: %{_status}.

%description -l pl
%{_pearname} serializuje z³o¿one struktury danych takie jak tablice
czy obiekty jako dokumenty XML. Ta klasa pomaga w generowaniu
dowolnego dokumentu XML bez potrzeby u¿ycia DOM.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/data/%{_pearname}/doc/* docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
