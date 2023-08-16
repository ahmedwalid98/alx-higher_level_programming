-- create database and table on it
-- create Database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- create table state
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO GENERATED NOT NULL PRIMARY KEY, name VARCHAR(256));