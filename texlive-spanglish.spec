# revision 20889
# category Package
# catalog-ctan /language/spanish/babel/contrib/spanglish
# catalog-date 2010-12-28 21:48:53 +0100
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-spanglish
Version:	0.1
Release:	1
Summary:	Simplified Spanish support for Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/spanish/babel/contrib/spanglish
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanglish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanglish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package provides very simplified (or ultra sloppy) support
for Spanish in Babel, mostly as a fallback in case spanish.ldf
fails for some reason. The package provides basic support for
Spanish hyphenation, captions, date, frenchspacing,
indentfirst, symbolic footnotes, enumerations, small caps roman
numerals, and a handful of shorthands and Spanish mathematical
operators. No options or attributes for customization are
provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spanglish/spanglish.ldf
%{_texmfdistdir}/tex/latex/spanglish/spanglish.sty
%doc %{_texmfdistdir}/doc/latex/spanglish/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
