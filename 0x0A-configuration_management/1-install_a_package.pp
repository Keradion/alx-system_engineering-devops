# This puppet manifest Install flask using pip3

package { 'flask':
  ensure   => 'latest',
  provider => 'pip3',
}
