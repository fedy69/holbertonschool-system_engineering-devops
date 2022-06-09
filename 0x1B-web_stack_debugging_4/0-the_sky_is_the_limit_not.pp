#the amount of traffic an Nginx server can handle
exec {'replace':
  provider => shell,
  command  => ' sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\',
  before   => Exec['restart'],
}
#Restart Nginx

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}