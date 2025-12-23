create database exemplo;

use exemplo;

create table sample_users(
user_id int auto_increment primary key,
account_name varchar(255) not null,
user_name varchar(255) not null,
age int not null,
gender enum('Male', 'Female', 'Non-binary') not null,
date_joined date not null,
posts int not null,
likes int not null,
followers int not null,
following_users int not null
);

insert into sample_users(account_name, user_name, age, gender, date_joined, posts, likes, followers, following_users)
values
('john_doe123', 'John Doe', 30, 'Male', '2023-01-01', 100, 250, 150, 200),
('jane_smith456', 'Jane Smith', 28, 'Female', '2023-02-15', 85, 300, 200, 180),
('carol_star', 'Carol Star', 22, 'Female', '2023-03-10', 50, 120, 90, 60),
('mike_dev', 'Mike Dev', 35, 'Male', '2023-01-20', 200, 500, 300, 280);

select * from sample_users;

select * from sample_users where age > 25;

select * from sample_users where likes > 200 and posts > 80;

select user_name from sample_users where likes > 250 and following_users > 100;

update sample_users set likes = likes + 50;

select user_name, likes from sample_users;

drop table sample_users;