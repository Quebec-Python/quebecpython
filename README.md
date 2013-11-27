# Québec-Python

Québec-Python's website.

Built with [Pelican](http://getpelican.com)

## Dependencies

* See *requirements.txt* file for Pelican's dependencies.
* Sass / Compass

## Dev environment setup

### Running Vagrant

Install the [latest VirtualBox](https://www.virtualbox.org/) and [Vagrant](http://www.vagrantup.com/)

### Then hop into the vagrant folder:

    $ vagrant up

### Get into the VM by typing:

    $ vagrant ssh

### Go into the folder where the project is

    $ cd quebecpython

### Install Pelican's dependencies

    $ sudo pip install -r requirements.txt

### Run the following command in the project's folder:

    $ make devserver

Type http://localhost:8080 in your browser to see the website

## FAQ

### How can I stop Pelican's webserver ?

You need to run the shell script:

    $ ./develop_server.sh stop
