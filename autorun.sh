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

BIN=/home/pi/Desktop/TIPE
SERVICE_NAME = autorun
EXECUTABLE=main.py
SERVICE_SHUTDOWN_SCRIPT = stop.py
usage()
{
        echo "-----------------------"
        echo "Usage: $0 (stop|start|restart)"
        echo "-----------------------"
}
 
if [ -z $1 ]; then
        usage
fi
 
service_start()
{
        echo "Starting service '${SERVICE_NAME}'..."
        OWD=`pwd`
        cd ${BIN} &amp;&amp; python ${EXECUTABLE}
        cd $OWD
        echo "Service '${SERVICE_NAME}' started successfully"
}
 
service_stop()
{
        echo "Stopping service '${SERVICE_NAME}'..."
        OWD=`pwd`
        cd ${BIN} &amp;&amp; python ${SERVICE_SHUTDOWN_SCRIPT}
        cd $OWD
        echo "Service '${SERVICE_NAME}' stopped"
}
 
case $1 in
        stop)
                service_stop
        ;;
        start)
                service_start
        ;;
        restart)
                service_stop
                service_start
        ;;
        *)
                usage
esac
exit 0			
