Name:		texlive-protex
Version:	20170414
Release:	1
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
%{_texmfdistdir}/tex/latex/protex
%doc %{_texmfdistdir}/doc/latex/protex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
