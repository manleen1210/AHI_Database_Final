AHI_Database_Final
# Step 1
## Launching Virtual Machine 
### The first VM was launched on Microsoft Azure. An UBUNTU server with username and password. Ports 22(SSH) and 3306(MySQL) were opened.
#### Public IP address: 52.249.196.193

# Step 2
## Creating username and password 
#### Defined in a private document

# Step 3
## Installing mysql on the UBUNTU instance
#### Using a terminal, the following command was used to connect to the new VM
#### ssh client@52.249.196.193 and the password that was created in Step 2
#### Next we entered the command sudo apt-get update followed by sudo apt install mysql-server mysql-client
#### Then log into mysql using the command sudo mysql
##### To test the command show databases; will allow review of the databases expected in the sql instance 

# Step 4 
## Creating a new user 
#### Using the following set of commands, a new user was created with the expected credentials 
### Create USER ‘dba'@'%' IDENTIFIED BY ‘ahi2020’;
#### Confirm creation of new user with the command
### select user from mysql.user; 
#### Grant all privilges for the new user 
### GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' WITH GRANT OPTION;
#### Then confirm with 
### show grants for dba;
#### Exit mysql with Ctrl+D 

# Step 5 
## Creating a new database
#### Log into mysql with the new user from step 4 using command 
### mysql -u DBA -p
#### and enter password 'ahi2021'
#### To create the new database use the following command
### Create database e2e;
#### Then confirm creation using command 
### Show databases;

# Step 6 
## Load H1N1 data into new database 
### Please refer to file 'Step6_newtable_h1n1.py' in this repository
#### In order to ensure the python code works and connection is established, we need to update a mySQL configuration file
#### In the terminal, exit mysql with Ctrl+D, then enter the command 
### sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
#### Scroll to bind-address using the arrow keys and update to 0.0.0.0.
#### Then Ctrl+O to save changes and Ctrl+X to exit the configuration file
#### The following command needs to be entered to ensure changes are in place 
### /etc/init.d/mysql restart
#### Once authentication is complete, the python file should run smoothly

#### To check that the data has been uploaded successfully, in the terminal we log back into mysql with DBA user 
### mysql -u DBA -p
#### then follow these steps
### show databases;
### use e2e;
### show tables;
#### table list should included h1n1

# Step 7
## Create a dump (.sql) backup 
#### A simple one line command to do this will be 
###  sudo mysqldump e2e > backup_e2e.sql
#### Then type the following command to ensure we have the right file
### ls
#### Also use the following command to look at details of the dump file 
### nano backup_e2e.sql
#### use Ctrl+X to exit once review is complete 

# Step 8 
## Use SCP command to move the file from the primary machine to a replica
#### A second Azure VM (UBUNTU) was launched with username and password. Ports 22(SSH) and 3306(MySQL) were opened.
#### Public IP: 52.179.23.94
#### Now on the terminal which is logged into the primary terminal requires the following command 
### scp backup_e2e.sql replica@52.179.23.94:/home/replica

# Step 9
## Create a new trigger
### Please refer to the sql file 'Step9_newtrigger_h1n1concern.sql' for the trigger code
#### It also includes an example to check if the trigger works.

# And that's it! Thank you! 