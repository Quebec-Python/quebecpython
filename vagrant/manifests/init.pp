class core {

    exec { "apt-update":
      command => "/usr/bin/sudo apt-get -y update"
    }

    package {
      [ "build-essential" ]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }
}

class python {

    package {
      [ "python", "python-setuptools", "python-dev", "python-pip"]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }

    exec {
      "virtualenv":
      command => "/usr/bin/sudo pip install virtualenv",
      require => Package["python-dev", "python-pip"]
    }

}

class pythondev {
    package {
        [ "python2.7-dev", "checkinstall", "libmysqlclient-dev" ]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }
}

include core
include python
include pythondev