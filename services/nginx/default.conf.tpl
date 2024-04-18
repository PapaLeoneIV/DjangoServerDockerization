    server {
        listen       80;
        server_name  localhost;
        
        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            alias /vol/static/;
        }

       
        location /media {
            alias /vol/media;
        }
        location / {
            include proxy_params;
            proxy_pass http://web:8000;  # Ensure you have the correct URL and port
        }
    }