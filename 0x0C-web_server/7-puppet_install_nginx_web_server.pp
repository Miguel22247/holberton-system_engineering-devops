# Install the nginx engine
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  name     => 'nginx',
}
file { 'index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}
# The redirection must be 301
file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
service { 'nginx':
  ensure  => 'running',
}Permanentlya
