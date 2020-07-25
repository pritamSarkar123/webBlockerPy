1. prevent some specific websites
2. pass site links and working hours to prevent them at that time
3. here we are working with date and time 
4. runs python program in background
5. we can attach gui with it later
6. in 
 windows:- "C:\Windows\System32\drivers\etc\hosts"->
 linux/mac:-"/etc/hosts"
"exaples":-list of blocked filed
7. our python script will add there the site names 
8. and also remove them after stated interval
9. we need Task schedular(Windoes)/Cron(Linux) to run the script
or we can do it in python also using while loop
10. the host file can only be accessed by admin

how to run the script when windows is turned on
0. if cursor is not at next line of "hostes" file then do it
1. change extension from .py to .pyw
2. right click on it and run as admin...
3. steps :- 
    1. task schedular>create task>Name:,Configure for:,Runs with highest privilages:,
    2. Triggers>New>Begin the task: At startup>ok
    3. Actions>new>Action:Start a program>Browse:....pyw>Ok
    4. conditions>start the task only if ...: make it unchecked>ok
    5. ok

in Ubuntu
1. host_path="/etc/hosts"
2. websiteBlocker.py will also work
3. manualy:- sudo python3 websiteBlocker.py
4. sudo crontab -e
    1. add the path to the websiteBlocker.py script
    2. @reboot python3 /home/....../websiteBlocker.py
    3. ctrl+x -> Y-> enter
5. reboot 

