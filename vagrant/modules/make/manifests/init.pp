class make {
  package { "make":
    ensure => present,
    require => Exec["apt-get update"]
  }
}
