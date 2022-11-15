Name:		texlive-carbohydrates
Version:	39000
Release:	1
Summary:	Carbohydrate molecules with chemfig
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/carbohydrates
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carbohydrates.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carbohydrates.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers macros that make the preparation of
exercise sheets for teaching carbohydrate chemistry a lot less
tedious. It uses chemfig for drawing the formulas. Different
representation models (Fischer, Haworth, chair...) are
supported as well as alpha, beta, and chain isomers.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/carbohydrates
%doc %{_texmfdistdir}/doc/latex/carbohydrates

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
