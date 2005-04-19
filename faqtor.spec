Summary:	FAQtor - a FAQ generator
Summary(pl):	FAQtor - generaor FAQ
Name:		faqtor
Version:	0.7
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/faqtor/%{name}-%{version}.tgz
# Source0-md5:	32c3aa742fc5fca90ea4cc2739ed9069
URL:		http://faqtor.sourceforge.net/
Requires:	python >= 1:2.3
Requires:	python-PyXML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAQtor is a FAQ generator. It is a simple but powerfull Python script
that can convert custom XML files into professional looking FAQs.

%description -l pl
FAQtor jest generatorem plików FAQ. Jest to prosty, lecz wyposa¿ony
w du¿e mo¿liwo¶ci skrypt Pythona konwertuj±cy pliki XML opisuj±ce
sekcje, pytania i odpowiedzi FAQ w profesjonalnie wygl±daj±cy
dokument.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

sed -e 's!/bin/env python!/usr/bin/python!' faqtor.py > $RPM_BUILD_ROOT%{_bindir}/faqtor.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* sample*
%attr(755,root,root) %{_bindir}/faqtor.py
