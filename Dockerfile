FROM httpd:latest

RUN rm -Rf "/usr/local/apache2/htdocs/*"
ADD ./site/* /usr/local/apache2/htdocs/

ENV PortainerHttpOrHttps=http
ENV WebSshHttpOrHttps=http
ENV DozzleHttpOrHttps=http
ENV ProxyHttpOrHttps=http

ENV PortainerPort=9443
ENV WebSshPort=8002
ENV DozzlePort=8001
ENV ProxyPort=81

ENV PortainerIp=0.0.0.0
ENV WebSshIp=0.0.0.0
ENV DozzleIp=0.0.0.0
ENV ProxyIp=0.0.0.0

ADD ./init.sh /bin/
RUN chmod +x /bin/init.sh

CMD [ "/bin/init.sh" ]