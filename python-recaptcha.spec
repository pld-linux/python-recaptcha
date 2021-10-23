Summary:	A client for reCAPTCHA and reCAPTCHA Mailhide
Summary(pl.UTF-8):	Klient usług reCAPTCHA i reCAPTCHA Mailhide
Name:		python-recaptcha
Version:	2.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/redhat-infosec/python-recaptcha/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2fe1e40784a5177f9b2b69de0f3d86fe
URL:		http://www.google.com/recaptcha
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not
require any imaging libraries because the CAPTCHA is served directly
from reCAPTCHA. Also allows you to securely obfuscate emails with
Mailhide. This functionality requires pycrypto. This library requires
two types of API keys. If you'd like to use the CAPTCHA, you'll need a
key from <http://recaptcha.net/api/getkey>. For Mailhide, you'll need
a key from <http://mailhide.recaptcha.net/apikey>.

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
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/recaptcha
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/recaptcha
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/recaptcha
%{py_sitescriptdir}/recaptcha/__init__.py[co]
%dir %{py_sitescriptdir}/recaptcha/client
%{py_sitescriptdir}/recaptcha/client/*.py[co]
%{py_sitescriptdir}/recaptcha_client-%{version}-py*.egg-info
