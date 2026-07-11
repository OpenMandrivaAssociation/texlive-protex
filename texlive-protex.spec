%global tl_name protex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Literate programming package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/web/protex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/protex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/protex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
ProTeX is a simple but powerful literate programming tool, which is
designed to generate useful hypertext output (either PDF, or HTML using
TeX4ht).

