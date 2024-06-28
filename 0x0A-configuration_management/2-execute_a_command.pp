# This puppet manifest kill running process using pkill

exec {'Killmenow':
  command => 'pkill -9 killmenow',
  path    => ['/usr/bin', '/usr/bin/pkill'],
}
