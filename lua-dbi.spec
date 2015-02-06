%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luadbi

# DBI.lua has a shebang that requires bin/lua directly
%if %{_use_internal_dependency_generator}
%define __noautoreq '.*bin/lua.*'
%else
%define _requires_exceptions bin/lua
%endif

Summary:	Database connectivity for the Lua programming language
Name:		lua-dbi
Version:	0.5
Release:	2
License:	MIT
Group:		Development/Other
Url:		http://code.google.com/p/%{oname}/
Source0:	http://%{oname}.googlecode.com/files/%{oname}.%{version}.tar.gz
# patch to compile with postgresql,
# to send upstream, once a Pgsql ( nanar ) tell me if this is right or not
Patch0:		luadbi-fix_postgresql.diff
Patch1:		luadbi-0.5-pgsql_transaction.patch
Patch2:		luadbi-0.5-postgresql-path.patch
BuildRequires:	lua >= %{luaver}
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(lua) >= %{luaver}
BuildRequires:	pkgconfig(libpq)
BuildRequires:	pkgconfig(sqlite3)
Requires:	lua >= %{luaver}

%description
LuaSQL is a simple interface from Lua to a DBMS. This package of LuaSQL
supports MySQL, SQLite and PostgreSQL databases. You can execute arbitrary SQL
statements and it allows for retrieving results in a row-by-row cursor fashion.

%files
%doc README
%{lualibdir}/DBI.lua

#----------------------------------------------------------------------------

%package sqlite
Summary:	SQLite database connectivity for the Lua programming language
Group:		Development/Other
Requires:	%{name}

%description sqlite
LuaDBI is a simple interface from Lua to a DBMS. This package provides access
to SQLite databases.

%files sqlite
%{lualibdir}/dbdsqlite3.so

#----------------------------------------------------------------------------

%package mysql
Summary:	MySQL database connectivity for the Lua programming language
Group:		Development/Other
Requires:	%{name}

%description mysql
LuaDBI is a simple interface from Lua to a DBMS. This package provides access
to MySQL databases.

%files mysql
%{lualibdir}/dbdmysql.so

#----------------------------------------------------------------------------

%package postgresql
Summary:	PostgreSQL database connectivity for the Lua programming language
Group:		Development/Other
Requires:	%{name}

%description postgresql
LuaDBI is a simple interface from Lua to a DBMS. This package provides access
to PostgreSQL databases.

%files postgresql
%{lualibdir}/dbdpostgresql.so

#----------------------------------------------------------------------------

%prep
%setup -c -q -n %{oname}-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
mkdir -p build
make

%install
mkdir -p %{buildroot}/%{lualibdir}/
cp *so *lua %{buildroot}/%{lualibdir}/

