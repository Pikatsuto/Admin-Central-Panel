#!/bin/sh

rm -Rf /usr/local/apache2/htdocs/index.html
cp /usr/local/apache2/htdocs/template.html /usr/local/apache2/htdocs/index.html

/bin/sed -i "s/PortainerHttpOrHttps/${PortainerHttpOrHttps}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/WebSshHttpOrHttps/${WebSshHttpOrHttps}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/DozzleHttpOrHttps/${DozzleHttpOrHttps}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/ProxyHttpOrHttps/${ProxyHttpOrHttps}/g" "/usr/local/apache2/htdocs/index.html"

/bin/sed -i "s/PortainerPort/${PortainerPort}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/WebSshPort/${WebSshPort}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/DozzlePort/${DozzlePort}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/ProxyPort/${ProxyPort}/g" "/usr/local/apache2/htdocs/index.html"

/bin/sed -i "s/PortainerIp/${PortainerIp}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/WebSshIp/${WebSshIp}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/DozzleIp/${DozzleIp}/g" "/usr/local/apache2/htdocs/index.html"
/bin/sed -i "s/ProxyIp/${ProxyIp}/g" "/usr/local/apache2/htdocs/index.html"

/usr/local/bin/httpd-foreground