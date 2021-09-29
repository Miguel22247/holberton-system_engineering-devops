# Puppet program that fix the code
exec { 'fixit':
  command  => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  provider => 'shell'
}