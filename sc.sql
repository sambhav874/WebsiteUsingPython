create table log_date(
    id integer primary key autoincrement,
    entry_date date not null
);

create table signin(
    id integer primary key autoincrement ,
    f_name text not null,
    l_name text not null,
    email text not null,
    password text not null,
    address text not null

);

create table login(
    email text not null,
    password integer not null,
    primary key(email)
);