# Profiles REST API
Profiles RESP API course code.

## vagrant
This requires vagrant installed.

-> and then run go to project directory and run following command for vagrant to download detailsas mentioned in Vagrantfile (which got generated when we ran $vagrant init ubuntu/bionic64 and added so many details to Vagrantfile)
$vagrant up

-> ran following for connecting to server in ssh mode
```
$vagrant ssh
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-54-generic x86_64)

* Documentation:  https://help.ubuntu.com
* Management:     https://landscape.canonical.com
* Support:        https://ubuntu.com/advantage

 System information as of Sat Jul 13 20:15:05 UTC 2019

 System load:  0.12              Processes:             102
 Usage of /:   11.5% of 9.63GB   Users logged in:       0
 Memory usage: 13%               IP address for enp0s3: 10.0.2.15
 Swap usage:   0%


5 packages can be updated.
5 updates are security updates.
```
-> now we are guest server
```
vagrant@ubuntu-bionic:~$
vagrant@ubuntu-bionic:~$ pwd
/home/vagrant
vagrant@ubuntu-bionic:~$ whoami
vagrant
vagrant@ubuntu-bionic:~$ ls
vagrant@ubuntu-bionic:~$ ls /
bin   dev  home        initrd.img.old  lib64       media  opt   root  sbin  srv  tmp  vagrant  vmlinuz
boot  etc  initrd.img  lib             lost+found  mnt    proc  run   snap  sys  usr  var      vmlinuz.old
```

-> /vagrant folder is synchronized directory between guest server and host
```
vagrant@ubuntu-bionic:/vagrant$ ls
LICENSE  README.md  Vagrantfile  ubuntu-bionic-18.04-cloudimg-console.log
```

->
