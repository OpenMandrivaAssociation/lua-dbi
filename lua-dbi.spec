%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luadbi

# DBI.lua has a shebang that requires bin/lua directly
%define _requires_exceptions bin/lua

Name:           lua-dbi
Version:        0.4
Release:        %mkrel 2
Summary:        Database connectivity for the Lua programming language

Group:          Development/Other
License:        MIT
URL:            http://code.google.com/p/%{oname}/
Source0:        http://%{oname}.googlecode.com/files/%{oname}.%{version}.tar.gz
# patch to compile with postgresql, 
# to send upstream, once a Pgsql ( nanar ) tell me if this is right or not
Patch0:         luadbi-fix_postgresql.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
#BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel >= 3.0
BuildRequires:  mysql-devel
BuildRequires:  postgresql-devel

%description
LuaSQL is a simple interface from Lua to a DBMS. This package of LuaSQL
supports MySQL, SQLite and PostgreSQL databases. You can execute arbitrary SQL
statements and it allows for retrieving results in a row-by-row cursor fashion.

%package sqlite
Summary:        SQLite database connectivity for the Lua programming language
Group:          Development/Other
Requires:       lua >= %{luaver}
Requires:       %{name}
%description sqlite
LuaDBI is a simple interface from Lua to a DBMS. This package provides access
to SQLite databases.


%package mysql
Summary:        MySQL database connectivity for the Lua programming language
Group:          Development/Other
Requires:       lua >= %{luaver}
Requires:       %{name}
%description mysql
LuaDBI is a simple interface from Lua to a DBMS. This package provides access
to MySQL databases.


%package postgresql
Summary:        PostgreSQL database connectivity for the Lua programming language
Group:          Development/Other
Requires:       lua >= %{luaver}
Requires:       %{name}
%description postgresql
LuaDBI is a simple interface from Lua to a DBMS. This package provides access
to PostgreSQL databases.


%prep
%setup -c -q -n %{oname}-%{version}
%patch0 -p0

%build
mkdir -p build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%lualibdir/
cp *so *lua $RPM_BUILD_ROOT/%lualibdir/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{lualibdir}/DBI.lua

%files sqlite
%defattr(-,root,root,-)
%{lualibdir}/dbdsqlite3.so

%files mysql
%defattr(-,root,root,-)
%{lualibdir}/dbdmysql.so

%files postgresql
%defattr(-,root,root,-)
%{lualibdir}/dbdpostgresql.so
