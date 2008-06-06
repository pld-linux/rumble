#
Summary:	Mailing list manager
Name:		rumble
Version:	0.0.23
Release:	1
#Epoch:		-
License:	Ruby's
Group:		Applications
Source0:	http://dinhe.net/~aredridel/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	a7a23df99307910c503814c389735f46
URL:		http://dinhe.net/~aredridel/projects/ruby/rumble
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRequires:	rake
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple mailing list manager.

%prep
%setup -q

%build
install %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root)   %{_bindir}/rumble
%{ruby_rubylibdir}/rumble.rb
%{ruby_rubylibdir}/rumble
