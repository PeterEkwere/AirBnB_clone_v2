#!/usr/bin/env bash

/server_name _;/a\
	location /hbnb_static {\
	    alias /data/web_static/current/;\
	    index index.html index.htm;\
	}
