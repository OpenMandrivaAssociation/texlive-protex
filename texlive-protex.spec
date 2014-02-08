# revision 15878
# category Package
# catalog-ctan /web/protex
# catalog-date 2008-09-16 21:39:08 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-protex
Version:	1.5
Release:	3
Summary:	Literate programming package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/protex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/protex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/protex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ProTeX is a simple but powerful literate programming tool,
which is designed to generate useful hypertext output (either
PDF, or HTML using TeX4ht).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/protex/AlProTex.sty
%{_texmfdistdir}/tex/latex/protex/ProTex.sty
%doc %{_texmfdistdir}/doc/latex/protex/LitProg
%doc %{_texmfdistdir}/doc/latex/protex/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 755138
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719311
- texlive-protex
- texlive-protex
- texlive-protex
- texlive-protex

