use agent;
create table products(
	u_id int identity(1, 1) primary key,
	u_name nvarchar(30),
	u_tel nvarchar(20),
	u_adress nvarchar(100)
);
