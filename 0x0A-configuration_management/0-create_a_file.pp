# create a file
file { 'holberton':
  path    => '/tmp/holberton',
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
}
