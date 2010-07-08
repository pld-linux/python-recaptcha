%define		fname	recaptcha-client
Summary:	A client for reCAPTCHA and reCAPTCHA Mailhide
Summary(pl.UTF-8):	Klient usług reCAPTCHA i reCAPTCHA Mailhide
Name:		python-recaptcha
Version:	1.0.3
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/r/recaptcha-client/%{fname}-%{version}.tar.gz
# Source0-md5:	5aaa88d703f1003ecc63a0ced00baad6
URL:		http://recaptcha.net
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
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
a key from <http://recaptcha.net/api/getkey>. For Mailhide, you'll
need a key from <http://mailhide.recaptcha.net/apikey>.

%description -l pl.UTF-8
Ten moduł obsługuje CAPTCHA (kod do wpisania z obrazka) w Pythonie w
oparciu o usługę reCAPTCHA. Nie wymaga żadnaj biblioteki graficznej,
gdyż CAPTCHA serwowana jest bezpośrednio z reCAPTCHA. Pozwala również
bezpiecznie ukryć adresy email za pomocą Mailhide. Ta funkcjonalność
wymaga pycrypto. Do działania klienta niezbędne są dwa klucze. Aby
używać CAPTCHA, należy pobrać klucz ze strony
<http://recaptcha.net/api/getkey>. Dla Mailhide należy pobrać klucz ze
strony <http://mailhide.recaptcha.net/apikey>.

%prep
%setup -qn %{fname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# structure of this module is an incredible fuckup. anyone knows how to fix this?
cp recaptcha/__init__.pyc $RPM_BUILD_ROOT%{py_sitescriptdir}/recaptcha

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/recaptcha
%{py_sitescriptdir}/recaptcha_client-%{version}-py*.egg-info
