# revision 29272
# category Package
# catalog-ctan /language/spanish/babel/contrib/spanglish
# catalog-date 2013-03-02 07:48:35 +0100
# catalog-license lppl1.3
# catalog-version 0.1a
Name:		texlive-spanglish
Version:	0.1a
Release:	11
Summary:	Simplified Spanish support for Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/spanish/babel/contrib/spanglish
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanglish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanglish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides very simplified (or ultra sloppy) support
for Spanish in Babel, mostly as a fallback in case spanish.ldf
fails for some reason. The package provides basic support for
Spanish hyphenation, captions, date, frenchspacing,
indentfirst, symbolic footnotes, enumerations, small caps roman
numerals, and a handful of shorthands and Spanish mathematical
operators. No options or attributes for customization are
provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
