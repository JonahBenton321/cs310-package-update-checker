How did you get the list of packages?
    The list of packages which can be updated can be found by running the command apt list --upgradable after updating the repository using apt update
What is the crontab sequence to run the script?
    0 0 * * 0 /home/codespace/.python/current/bin/python /workspaces/cs310-package-update-checker/pkg-check.py >> /var/tmp/update-list.txt 2>&1
Since this script would require root, how do you install a crontab for root?
    You can install a cron tab at root by running 'sudo crontab -e' this will take you to the root crontab