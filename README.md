# LoonProject
How to control the altitude of a balloon using raspberryPi
Using Python programming, these algorithms aim at keeping a natural-shape ballon at a given altitude... For more informations and 
a better understanding of the purpose of such a project, see https://x.company/intl/fr_fr/loon/

## SETUP :
You just have to write some modifications to `autorun.sh`:
  - replace the content of `$BIN` with the directory of your project.
    ### If you're on Linux 
    copy/paste `autorun.sh` in the folder `/etc/init.d` and `sudo chmod a+x /etc/init.d/autorun.sh` and
    `update-rc.d autorun.sh start 20 2 . stop 17 6 .` . It's done, `autorun.sh` will be executed at boot time !
  
    ### If you're on Windows
    follow : https://www.commentcamarche.com/faq/18658-script-au-demarrage-et-a-l-arret-de-windows for setting `autorun.sh`     
    executable at boot time...
    
Then you just have to modify the path (which in my case is `/home/pi/Desktop/TIPE/...`) in `main.py` 
and in `AsyncMesure.py`to make it work in yours.
