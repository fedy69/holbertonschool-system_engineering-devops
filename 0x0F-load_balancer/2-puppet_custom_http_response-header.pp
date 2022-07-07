# Puppet script to install a package

exec { 'nginx.conf':
  provider => shell,
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "/http {/a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
}
