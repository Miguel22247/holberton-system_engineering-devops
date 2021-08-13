file { 'holberton'
    path => '/tmp/holberton',
    mode => '0744',
    content => 'I love Puppet',
    owner => 'www-data',
    group => 'www-data',
}
