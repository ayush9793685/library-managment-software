create database lib;
use lib;
create table book(sno int,book_id int,book_name text,author text,publication text,edition int,price int);
create table students(sno int,student_id int,students_name text,class int,sec text,fine int,contact varchar(13));
create table issue(book_id int,student_id int,date_of_issue date,date_of_return date);
insert into book values(1,101,'comp_sci','sumita arora','dhanpat rai',2021,750);
insert into students values(1,1,'ayush yadav',12,'A',0,'9793685966');
insert into issue values(101,1,'2022-1-1','2022-1-1');