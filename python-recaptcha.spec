%define		pname	recaptcha
%define		fname	recaptcha-client
%define		wtfname recaptcha_client
Summary:	A client for reCAPTCHA and reCAPTCHA Mailhide
Summary(pl.UTF-8):	Klient usług reCAPTCHA i reCAPTCHA Mailhide
Name:		python-%{pname}
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/r/%{fname}/%{fname}-%{version}.tar.gz
# Source0-md5:	6a479f2142efc25954a6f37012b4c2dd
URL:		http://recaptcha.net
BuildRequires:	python-setuptools
BuildRequires:	python >= 2.5
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide. This functionality requires pycrypto. This library requires
two types of API keys. If you'd like to use the CAPTCHA, you'll need
a key from http://recaptcha.net/api/getkey. For Mailhide, you'll need
a key from http://mailhide.recaptcha.net/apikey

%description -l pl.UTF-8
Obsługuje CAPTCHA (kod do wpisania z obrazka) oparte o usługę reCAPTCHA.
Nie wymaga żadnaj biblioteki graficznej, gdyż CAPTCHA serwowana jest
bezpośrednio z reCAPTCHA. Pozwala również bezpiecznie ukryć adresy email
za pomocą Mailhide. Ta funkcjonalność wymaga pycrypto.
Do działania klienta niezbędne są dwa klucze. Jeśli chcesz używać CAPTCHA,
pobierz klucz ze strony http://recaptcha.net/api/getkey. Dla Mailhide,
pobierz klucz ze strony http://mailhide.recaptcha.net/apikey.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# structure of this module is an incredible fuckup. anyone knows how to fix this?
cp %{pname}/__init__.pyc $RPM_BUILD_ROOT%{py_sitescriptdir}/%{pname}/

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{pname}
%{py_sitescriptdir}/%{wtfname}-%{version}-py*.egg-info
