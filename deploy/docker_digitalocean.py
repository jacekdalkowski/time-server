import subprocess
import re
import os
import time
import sh
import time
from docker_digitalocean_time_server import *

ssh_con_str = "root@46.101.148.70"

print "NOTICE: this script has to be run as a user with access to SSH keys."
print "Deployment to remote server (" + ssh_con_str + ") started."

ssh = sh.ssh.bake('-oStrictHostKeyChecking=no', ssh_con_str)

print "Successfully connected to remote server."

kill_and_remove_all_containers(ssh, 'time-server')

copy_time_server_src_to_remote_host(ssh_con_str)
build_time_server_image_in_remote_host(ssh)
run_time_server_container(ssh)



