FROM debian:latest

EXPOSE 80

RUN apt-get update
RUN apt-get -y install python3 python3-pip

RUN apt-get -y install apache2
RUN a2enmod cgi

RUN service apache2 restart

RUN pip3 install art

#enable cgi in the website root
#second block to allow .htaccess
RUN echo "                       \n \
<Directory /var/www/html>        \n \
   Options +ExecCGI              \n \
   AddHandler cgi-script .py     \n \
   DirectoryIndex index.py       \n \
</Directory>                     \n \
" >> /etc/apache2/apache2.conf

RUN chmod -R u+rwx,g+x,o+x /var/www/html

RUN ln -sf /usr/bin/python /usr/local/bin/python

CMD /usr/sbin/apache2ctl -D FOREGROUND