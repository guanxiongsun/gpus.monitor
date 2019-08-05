# Demo

Demo result:

![](demo/demo.png)

Watch result per second:

![](demo/demo2.png)

# Install
 ~~~
    pip install -r requirements.txt
 ~~~

# Usage
1. modify $USER and $PASSWORD in `list.sh`
2. modify `server_list.yaml` file as example
3. list all gpu resources on server list
    ~~~
    ./list.sh
    ~~~
    or show per second 
    ~~~
    watch -n 1 ./list.sh
    ~~~

# Tips
- The $USER and $PASSWORD in the shell script will rewrite which in the `server_list.yaml` file.
- If you have different username and password on different server, leave the $USER and $PASSWORD in the shell script as NONE and then customize what in the `server_list.yaml` file.