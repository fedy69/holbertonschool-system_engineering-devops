# fixes Apache error by fixing typo in wordpress
exec { 'fixed-phpp':
   command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
   path    => '/bin';
   
   }