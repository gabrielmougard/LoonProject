# /etc/init.d/autorun.sh
### BEGIN INIT INFO
# Provides:		autorun.sh
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	Start daemon at boot time
# Description:		Enable service provided by daemon.
### END INIT INFO

#!/bin/bash

BIN=/home/pi/loon


	$BIN/enableConnection.sh &
	cd $BIN
	python enableMesure.py &
	python Asservissement.py
		
	exit 0			
