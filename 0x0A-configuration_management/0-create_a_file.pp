file {'/tmp/school':
  # This manifest creates a new file 
  ensure => 'present',
  content => 'I love Puppet',
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
}
