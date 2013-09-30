class python {
  package { "python":
    ensure => present,
    require => Exec["apt-get update"]
  }

  # install pip
  package { "python-pip":
    ensure => present,
    require => Exec["apt-get update"]
  }

  package { "python-dev":
    ensure => present,
    require => Exec["apt-get update"]
  }

  package { "build-essential":
    ensure => present,
    require => Exec["apt-get update"]
  }
}
