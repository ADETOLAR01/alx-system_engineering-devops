file { '/home/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

augeas { 'configure ssh client':
  context => '/files/home/ubuntu/.ssh/config',
  changes => [
    'set Host/* IdentityFile /home/ubuntu/.ssh/school',
    'set Host/* PasswordAuthentication no',
  ],
}
