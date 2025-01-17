# Generated by rust2rpm 23
%bcond_without check

%global crate kondo

Name:           rust-kondo
Version:        0.6
Release:        1%{?dist}
Summary:        Filesystem cleaning tool that recursively searches directories for known project structures and determines how much space you could save by deleting the unnecessary files

License:        MIT
URL:            https://crates.io/crates/kondo
Source0:        https://github.com/tbillington/kondo/releases/download/v%{version}/kondo-x86_64-unknown-linux-gnu.tar.gz
Source1:        https://github.com/tbillington/kondo/blob/v%{version}/LICENSE
ExclusiveArch:  x86_64

BuildRequires:  anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Filesystem cleaning tool that recursively searches directories for known
project structures and determines how much space you could save by deleting the
unnecessary files.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
/usr/bin/kondo

%prep
tar xf %{SOURCE0}

%build

%install
install -Dm755 kondo %{buildroot}/usr/bin/kondo
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/licenses/%{crate}/LICENSE

%changelog
%autochangelog
