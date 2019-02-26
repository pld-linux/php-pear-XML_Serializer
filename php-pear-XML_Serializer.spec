%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	XML_Serializer
Summary:	%{_pearname} - class to build XML documents from data structures
Summary(pl.UTF-8):	%{_pearname} - klasa do tworzenia dokumentów XML ze struktur danych
Name:		php-pear-%{_pearname}
Version:	0.21.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0a21c3327035c46284348874099185ff
URL:		http://pear.php.net/package/XML_Serializer/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php(xml)
Requires:	php-pear
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Parser >= 1.2.6
Requires:	php-pear-XML_Util >= 1.1.1
Obsoletes:	php-pear-XML_Serializer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} serializes complex data structures like arrays or objects
as XML documents. This class helps you generating any XML document you
require without the need for DOM.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
%{_pearname} serializuje złożone struktury danych takie jak tablice
czy obiekty jako dokumenty XML. Ta klasa pomaga w generowaniu
dowolnego dokumentu XML bez potrzeby użycia DOM.

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
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/Serializer.php
%{php_pear_dir}/XML/Unserializer.php
