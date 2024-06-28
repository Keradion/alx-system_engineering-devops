# This puppet manifest kill running process using pkill

exec {'Killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/pkill',
}
  
