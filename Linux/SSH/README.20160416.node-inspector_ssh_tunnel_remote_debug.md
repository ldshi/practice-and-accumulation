- SSH local port forwarding, the following command is tested with ‘meteor debug’

  ```
  ssh -L LOCAL_PORT:YOUR_APP_SERVER:APP_RUNNING_ON_PORT USERNAME@YOUR_APP_SERVER -i YOUR_PEM_KEY.pem -N

  Then access ‘http://localhost:8080/debug?port=5858’ with your browser, you should be able to do whatever you need just like debugging in your localhost.
  ```

  - [SSH Port Forwarding(SSH Tunneling)](http://www.linuxhorizon.ro/ssh-tunnel.html)

  - [What is a Pem file and how does it differ from other OpenSSL Generated Key File Formats?](http://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file)


