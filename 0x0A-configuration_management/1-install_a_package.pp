# Installs puppet-lint

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'verify_flask_version':
  command     => 'flask --version',
  path        => ['/usr/local/bin', '/usr/bin', '/bin'],
  logoutput   => true,
  refreshonly => true,
}
