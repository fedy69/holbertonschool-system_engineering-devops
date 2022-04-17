# using Puppet to changes the configuration file
exec { 'echo -e "\tPasswordAuthentication no" >> /etc/ssh/ssh_config':
    path => '/bin'
}
exec { 'echo -e "\tIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
    path => '/bin'
}