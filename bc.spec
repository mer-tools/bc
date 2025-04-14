Name:           bc
BuildRequires:  bison
BuildRequires:  ed
BuildRequires:  flex
BuildRequires:  readline-devel
BuildRequires:  texinfo
Url:            ftp://ftp.gnu.org/pub/gnu/bc
Version:        1.08.1
Release:        1
Summary:        GNU Command Line Calculator
License:        GPLv3+
Source:         bc-%{version}.tar.xz
Patch1:         bc-1.06-dc_ibase.patch
Patch2:         bc-1.07.1-readline-echo-empty.diff

%description
bc is an interpreter that supports numbers of arbitrary precision and
the interactive execution of statements. The syntax has some
similarities to the C programming language. A standard math library is
available through command line options. When used, the math library is
read in before any other input files. bc then reads in all other files
from the command line, evaluating their contents. Then bc reads from
standard input (usually the keyboard).

The dc program is also included. dc is a calculator that supports
reverse-polish notation and allows unlimited precision arithmetic.
Macros can also be defined. Normally, dc reads from standard input but
can also read in files specified on the command line. A calculator with
reverse-polish notation saves numbers to a stack. Arguments to
mathematical operations (operands) are "pushed" onto the stack until
the next operator is read in, which "pops" its arguments off the stack
and "pushes" its results back onto the stack.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure --with-readline
%make_build

%install
%make_install

rm -Rf %{buildroot}%{_datadir}/info
rm -Rf %{buildroot}%{_datadir}/man

%files
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README FAQ
%{_bindir}/bc
%{_bindir}/dc
