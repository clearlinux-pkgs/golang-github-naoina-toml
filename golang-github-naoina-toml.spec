Name     : golang-github-naoina-toml
Version  : 0.1.0
Release  : 1
URL      : https://github.com/naoina/toml/archive/v0.1.0.tar.gz
Source0  : https://github.com/naoina/toml/archive/v0.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-github-naoina-go-stringutil

%description
# TOML parser and encoder library for Golang [![Build Status](https://travis-ci.org/naoina/toml.png?branch=master)](https://travis-ci.org/naoina/toml)

%prep
%setup -q -n toml-0.1.0

%build
export LANG=C

%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/naoina/toml 

# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template toml; do
    for file in $(find . -iname "*.$ext") ; do
        install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
        cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done


%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/... || :

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/naoina/toml/_example/main.go
/usr/lib/golang/src/github.com/naoina/toml/ast/ast.go
/usr/lib/golang/src/github.com/naoina/toml/decode.go
/usr/lib/golang/src/github.com/naoina/toml/decode_bench_test.go
/usr/lib/golang/src/github.com/naoina/toml/decode_test.go
/usr/lib/golang/src/github.com/naoina/toml/encode.go
/usr/lib/golang/src/github.com/naoina/toml/encode_test.go
/usr/lib/golang/src/github.com/naoina/toml/error.go
/usr/lib/golang/src/github.com/naoina/toml/parse.go
/usr/lib/golang/src/github.com/naoina/toml/parse.peg.go
/usr/lib/golang/src/github.com/naoina/toml/util.go
/usr/lib/golang/src/github.com/naoina/toml/_example/example.toml
/usr/lib/golang/src/github.com/naoina/toml/testdata/test.toml
