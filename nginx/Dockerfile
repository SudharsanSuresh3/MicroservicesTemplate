# nginx/Dockerfile

# Use the official NGINX image
FROM nginx:alpine

# Remove the default configuration file and copy our own config file
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
