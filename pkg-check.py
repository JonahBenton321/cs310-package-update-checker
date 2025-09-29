import subprocess
# This script is called once a week by cron at the sudo level to update the package repository and output all packages which can be updated to /var/tmp/update-list.txt

# Updates the package repositorie
subprocess.run(["sudo", "apt-get", "update"], stdout=subprocess.PIPE)
# gets the list of all packeges that can be upgraded and out puts to a file 
subprocess.run(["sh", "-c", "apt list --upgradable >> /var/tmp/update-list.txt"], capture_output=True, text=True)