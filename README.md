# assignment

A backend application for user sign-up and login using Rest API.

### Requirements
1. An IDE that supports Java
2. Maven installed and path set in environment variable
3. SQL server to query and set-up the database

### How to Setup the Database
1. Make sure the MySQL server is installed. You can also use H2 Database.
2. Go to your terminal and type:
```
mysql -u root -p
```
3. enter the root user password
4. create a new database using following command:
```
create database <database_name>;
```
5. Switch to this database:
```
use <database_name>;
```
6. The database has been setup.

### How to Setup the project
1. clone the repository
2. extract the contents of the zip file and open the folder in IDE
3. In the terminal of the IDE, enter the following command or manually go the following directory:
```
cd project1/src/main/resources
```
4. Open the "application.properties" file
5. Make sure to make the following changes in yout application.properties file.
```
spring.datasource.url=jdbc:mysql://localhost:3306/<database_name>
spring.datasource.username=<username>
spring.datasource.password=<password>
```
database_name: same as the one used in mysql
username: the username for the user ('root' if you didn't create another user)
password: user password
6. Head to the following directory and find the file- "ProjectApplication.java"
```
src/main/java/com/project
```
7. build the project
8. run the file- "ProjectApplication.java"
