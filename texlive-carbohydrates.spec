%global tl_name carbohydrates
%global tl_revision 39000

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Carbohydrate molecules with chemfig
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/carbohydrates
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carbohydrates.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carbohydrates.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers macros that make the preparation of exercise sheets
for teaching carbohydrate chemistry a lot less tedious. It uses chemfig
for drawing the formulas. Different representation models (Fischer,
Haworth, chair...) are supported as well as alpha, beta, and chain
isomers.

