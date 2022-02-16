# Confirm you have no swap
sudo swapon -s

# Allocate 1GB (or more if you wish) in /swapfile
sudo fallocate -l 4G /swapfile

# Make it secure
sudo chmod 600 /swapfile
ls -lh /swapfile

# Activate it
sudo mkswap /swapfile
sudo swapon /swapfile

# Confirm again there's indeed more memory now
free -m
sudo swapon -s

# Add this line to /etc/fstab
echo '/swapfile   none    swap    sw    0   0' | sudo tee -a /etc/fstab

# Change swappiness to 10, so that swap is used only when 10% RAM is unused
# The default is too high at 60
echo 10 | sudo tee /proc/sys/vm/swappiness
echo vm.swappiness = 10 | sudo tee -a /etc/sysctl.conf