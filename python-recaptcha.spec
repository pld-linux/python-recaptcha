%define		fname	recaptcha-client
Summary:	A client for reCAPTCHA and reCAPTCHA Mailhide
Summary(pl.UTF-8):	Klient usług reCAPTCHA i reCAPTCHA Mailhide
Name:		python-recaptcha
Version:	1.0.6
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/r/recaptcha-client/%{fname}-%{version}.tar.gz
# Source0-md5:	74228180f7e1fb76c4d7089160b0d919
URL:		http://www.google.com/recaptcha
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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
%setup -qn %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

# structure of this module is an incredible fuckup. anyone knows how to fix this?
cp -p recaptcha/__init__.py[co] $RPM_BUILD_ROOT%{py_sitescriptdir}/recaptcha

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
%{py_sitescriptdir}/recaptcha_client-%{version}-py*-nspkg.pth
