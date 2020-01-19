%global fontname sil-nuosu
%global fontconf 66-%{fontname}.conf

%global archivename ttf-sil-nuosusil-2.1.1.tar.gz

Name:           %{fontname}-fonts
Version:        2.1.1
Release:        4%{?dist}
Summary:        The Nuosu SIL Font

Group:          User Interface/X
License:        OFL
URL:            http://scripts.sil.org/SILYi_home
Source0:        %{archivename}
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
The Nuosu SIL Font is a single Unicode font for the standardized Yi script
used by a large ethnic group in southwestern China.
Until this version, the font was called SIL Yi.

%prep
%setup -q -c %{name}
sed -i 's/\r//' OFL.txt doc/FONTLOG.txt

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc OFL.txt doc/FONTLOG.txt


%changelog
* Mon Jun 20 2011  Peng Wu <pwu@redhat.com> - 2.1.1-4
- Resolves: rhbz#679684
- Request to add sil-nuosu-fonts to RHEL6

* Sat Feb 12 2011  Peng Wu <pwu@redhat.com> - 2.1.1-3
- Add document.

* Sun Jan 30 2011  Peng Wu <pwu@redhat.com> - 2.1.1-2
- Clean the spec file and add fontconfig file

* Wed Jan 26 2011  Peng Wu <pwu@redhat.com> - 2.1.1-1
- Initial package
