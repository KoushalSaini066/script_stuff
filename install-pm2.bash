# Install PM2
sudo npm install pm2 -g

# Spawn PM2.
sudo pm2 --version
pm2 --version

# PM2 logrotate installation
sudo pm2 install pm2-logrotate
pm2 set pm2-logrotate:retain 30
pm2 set pm2-logrotate:max_size 2G
pm2 set pm2-logrotate:compress true
pm2 restart all

