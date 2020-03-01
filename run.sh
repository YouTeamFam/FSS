#!/bin/bash
cd /usr/src
gunicorn -w 1 -b 0.0.0.0:8000 house.wsgi:application
echo '服务已启动'