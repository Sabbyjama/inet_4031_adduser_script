# inet_4031_adduser_script
**Python Script for Adding Users/Groups to a System**
  
## Description
  
This Python Script reads user/group data from an input file, processes the file line-by-line and adds each user to the system.
The imports are necessary Because they offer essential capabilities for dealing with the operating system, using regular expressions, and reading input. The # in the input file acts as a marker for comments. This guarantees that commented lines (beginning with #) are disregarded by the regex.

## Operation
  
### Input File Specification
  
The input file should have the following format:

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

jdoe11:mypass:Doe:John:admins, reviewers

The name of the input file is up to the user.  Convention is create-users.input

### Running the Script
In order to run the code you need to install python onto your ubuntu and make sure that you put down the version of python that you use and ensure that it has script permissions by using chmod +x + your script name for example chmod +x inet_4031.py. Then you would create an input file named create-users.input with user data that was provided to you. Then you would execute the script in terminal for example >> $ sudo ./inet_4031.py < create-users.input which would allow the script to operate on the user data stored in create-users.input. The confirm your data went through and Then you would make sure your GitHub is connected to your ubuntu system and do the necessary personal token information and boom your code has been pushed from ubuntu to GitHub.





