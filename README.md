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

## python virtual environment
This will help to install all python packages to be installed in different location and not to mix up project files.
Doing following on guest server
vagrant@ubuntu-bionic:~$ cd /vagrant/
vagrant@ubuntu-bionic:/vagrant$ python -m venv ~/env
->this creates following
```
vagrant@ubuntu-bionic:/vagrant$ ls -ltr ~/env
total 20
-rw-rw-r-- 1 vagrant vagrant   69 Jul 13 20:31 pyvenv.cfg
lrwxrwxrwx 1 vagrant vagrant    3 Jul 13 20:31 lib64 -> lib
drwxrwxr-x 3 vagrant vagrant 4096 Jul 13 20:31 lib
drwxrwxr-x 2 vagrant vagrant 4096 Jul 13 20:31 include
drwxrwxr-x 3 vagrant vagrant 4096 Jul 13 20:31 share
drwxrwxr-x 2 vagrant vagrant 4096 Jul 13 20:31 bin
```
->to activate virtual environment
```
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$
```
See (env) is present when virtual environment is entered.
->to de-activate virtual environment
```
(env) vagrant@ubuntu-bionic:/vagrant$ deactivate
vagrant@ubuntu-bionic:/vagrant$
```

## requirements.txt
we mentioned software to install. These package name and version can be found from https://pypi.org/
->install django and djangorestframework by activating virtual environment
```
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ pip install -r requirements.txt
```

## new django project
We activated virtual mode and then create new django project
```
(env) vagrant@ubuntu-bionic:/vagrant$ pwd
/vagrant
(env) vagrant@ubuntu-bionic:/vagrant$ ls
LICENSE  README.md  Vagrantfile  hello_world.py  requirements.txt  ubuntu-bionic-18.04-cloudimg-console.log

(env) vagrant@ubuntu-bionic:/vagrant$ django-admin startproject profiles_project .
```
last parameter "." means don't create right here. if we don't mention, django will create subdirectory.
profiles_project is name of project.
```
(env) vagrant@ubuntu-bionic:/vagrant$ ls -ltr
total 68
-rw-r--r-- 1 vagrant vagrant  1067 Jul 13 19:34 LICENSE
-rw-r--r-- 1 vagrant vagrant  1189 Jul 13 20:06 Vagrantfile
-rw------- 1 vagrant vagrant 43723 Jul 13 20:12 ubuntu-bionic-18.04-cloudimg-console.log
-rw-r--r-- 1 vagrant vagrant    21 Jul 13 20:20 hello_world.py
-rw-r--r-- 1 vagrant vagrant    39 Jul 13 20:47 requirements.txt
-rw-r--r-- 1 vagrant vagrant  3315 Jul 14 00:49 README.md
drwxr-xr-x 1 vagrant vagrant   192 Jul 14 00:49 profiles_project
-rwxrwxr-x 1 vagrant vagrant   636 Jul 14 00:49 manage.py
```

we will create profiles_api project
```
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py startapp profiles_api
(env) vagrant@ubuntu-bionic:/vagrant$ ls -ltr
total 68
-rw-r--r-- 1 vagrant vagrant  1067 Jul 13 19:34 LICENSE
-rw-r--r-- 1 vagrant vagrant  1189 Jul 13 20:06 Vagrantfile
-rw------- 1 vagrant vagrant 43723 Jul 13 20:12 ubuntu-bionic-18.04-cloudimg-console.log
-rw-r--r-- 1 vagrant vagrant    21 Jul 13 20:20 hello_world.py
-rw-r--r-- 1 vagrant vagrant    39 Jul 13 20:47 requirements.txt
-rwxrwxr-x 1 vagrant vagrant   636 Jul 14 00:49 manage.py
-rw-r--r-- 1 vagrant vagrant  3407 Jul 14 00:50 README.md
drwxr-xr-x 1 vagrant vagrant   224 Jul 14 00:51 profiles_project
drwxr-xr-x 1 vagrant vagrant   288 Jul 14 00:51 profiles_api
```

start django server to test... you can see django page at http://127.0.0.1:8000/
```
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py runserver 0.0.0.0:8000

```

Now update profile_api/models.py with user profile and user profile manager,
which tells django that we enhanced user profile object model and model manager
for managing changes.
Now run makemigrations to prepare for migration.
```
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py makemigrations profiles_api
Migrations for 'profiles_api':
  profiles_api/migrations/0001_initial.py
    - Create model UserProfile
```
Now run migrate to make all changes to database for our django project.
Will run all migrations. Creates all required tables and so on.
```
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py migrate
```
create superuser
```
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py createsuperuser
```

and enable admin by addin details to profiles_api/admin.py
```
admin.site.register(models.UserProfile)
```

->Create api view
HelloWorld api view
Updated file is profiles_api/view.py
create urls.py in profile_api and then include this file to urls.py file of project.

->Create serializer to receive we post to request to our API
Serializer is a feature from the Django rest framework that allows you to easily
convert data inputs into Python objects and vice versa. Is kind of similar to a
Django form which you define and it has the various fields that you want to
expect for the input for your API.
So if we're going to add post or update functionality to our Hello API view then we need to create a Serializer to receive the content that we post to the API.
