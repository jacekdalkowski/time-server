import os
from docker_digitalocean_common import *

def copy_time_server_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/../*"
	print "Copying web-scheduler src (" + local_dir + ") to remote host."
	rsync_cmd = "rsync -azP --delete --exclude '*/node_modules' " + local_dir + " " + ssh_con_str + ":/root/apps/time-server"
	print "rsync command: " + rsync_cmd
	os.system(rsync_cmd)
	print "Copying web-scheduler src to remote host finished."

def build_time_server_image_in_remote_host(ssh):
	print "Building time-server image in remote host."
	result = ssh("docker build -t time-server /root/apps/time-server")
	print "Building time-server image in remote host result: "
	print result

def run_time_server_container(ssh):
	print "Starting time-server container in remote host."
	result = ssh("docker run --name time-server -d time-server")
	print "Starting time-server container in remote host result: "
	print result

