FROM php:8.2-apache

WORKDIR /var/www/html
COPY . .

RUN chown -R www-data:www-data /var/www/html
RUN a2enmod rewrite

EXPOSE 80