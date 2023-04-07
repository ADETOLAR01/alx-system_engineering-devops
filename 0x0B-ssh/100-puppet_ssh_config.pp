file { '/home/user/.ssh/config':
  ensure => file,
  owner  => 'user',
  group  => 'user',
  mode   => '0600',
  content => "Host example.com\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
