%bcond_without check
%global debug_package %{nil}

%global crate rustc-std-workspace-core

Name:           rust-%{crate}
Version:        1.0.0
Release:        2
Summary:        Explicitly empty crate for rust-lang/rust integration

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-std-workspace-core
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Explicitly empty crate for rust-lang/rust integration.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rustc-std-workspace-core) = 1.0.0
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(rustc-std-workspace-core/default) = 1.0.0
Requires:       cargo
Requires:       crate(rustc-std-workspace-core) = 1.0.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
