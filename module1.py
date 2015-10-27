Traceback (most recent call last):
  File "C:\Python27\lib\site-packages\roslaunch\__init__.py", line 298, in main
    p.start()
  File "C:\Python27\lib\site-packages\roslaunch\parent.py", line 260, in start
    self._start_infrastructure()
  File "C:\Python27\lib\site-packages\roslaunch\parent.py", line 209, in _start_infrastructure
    self._load_config()
  File "C:\Python27\lib\site-packages\roslaunch\parent.py", line 124, in _load_config
    roslaunch_strs=self.roslaunch_strs, verbose=self.verbose)
  File "C:\Python27\lib\site-packages\roslaunch\config.py", line 445, in load_config_default
    load_roscore(loader, config, verbose=verbose)
  File "C:\Python27\lib\site-packages\roslaunch\config.py", line 92, in load_roscore
    f_roscore = get_roscore_filename()
  File "C:\Python27\lib\site-packages\roslaunch\config.py", line 84, in get_roscore_filename
    return os.path.join(r.get_path('roslaunch'), 'resources', 'roscore.xml')
  File "C:\Python27\lib\site-packages\rospkg\rospack.py", line 200, in get_path
    raise ResourceNotFound(name, ros_paths=self._ros_paths)
ResourceNotFound: roslaunch
ROS path [0]=c:\ros\root
The Python REPL process has exited



//cygwin

from rospkg import environment
environment.get_ros_paths()
['/opt/ros/install_isolated/share/ros', '/opt/ros/install_isolated/share', '/opt/ros/install_isolated/stacks']
from rospkg import config
from roslaunch import config
config.get_roscore_filename()
'/opt/ros/install_isolated/etc/ros/roscore.xml'
import rospkg
r=rospkg.RosPack()
r.get_path('roslaunch')
'/opt/ros/install_isolated/share/roslaunch'


local:
    sourceNotFound: roslaunch
ROS path [0]=c:\ros\root
>>> import rospkg
>>> r=rospkg.RosPack()
>>> r
<rospkg.rospack.RosPack object at 0x033961B0>
>>> r.
  File "<stdin>", line 1
    r.
     ^
SyntaxError: invalid syntax
>>> r.get_path()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: get_path() takes exactly 2 arguments (1 given)
>>> r.get_path('roslaunch')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\rospkg\rospack.py", line 200, in get_path
    raise ResourceNotFound(name, ros_paths=self._ros_paths)
ResourceNotFound: roslaunch
ROS path [0]=c:\ros\root
>>> 


//and now

  File "C:\Python27\lib\site-packages\roslaunch\__init__.py", line 298, in main
    p.start()
  File "C:\Python27\lib\site-packages\roslaunch\parent.py", line 271, in start
    self.runner.launch()
  File "C:\Python27\lib\site-packages\roslaunch\launch.py", line 646, in launch
    self._setup()
  File "C:\Python27\lib\site-packages\roslaunch\launch.py", line 622, in _setup
    self._launch_master()
  File "C:\Python27\lib\site-packages\roslaunch\launch.py", line 391, in _launch_master
    success = p.start()
  File "C:\Python27\lib\site-packages\roslaunch\nodeprocess.py", line 290, in start
    self.popen = subprocess.Popen(self.args, cwd=cwd, stdout=logfileout, stderr=logfileerr, env=full_env, close_fds=True) #greg1, preexec_fn=os.setsid)
AttributeError: 'module' object has no attribute 'setsid'
The Python REPL process has exited

No handlers could be found for logger "roslaunch"
Roslaunch got a 'The system cannot find the file specified' error while attempting to run:

rosmaster --core -p 11311 __log:=c:\ROS\log\e5670e0f-7cd6-11e5-8c31-003ee1c5c62d\master.log

Please make sure that all the executables in this command exist and have
executable permission. This is often caused by a bad launch-prefix.
The traceback for the exception was written to the log file
The Python REPL process has exited

#go time:
import roslaunch
roslaunch.main(['roslaunch','--core'])


#testing failure
import rospkg
import os
import roslib
rospack = rospkg.RosPack(rospkg.get_ros_paths(env=os.environ))
matches = roslib.packages.find_node('rosout','rosout', rospack)



#('process[%s]: start w/ args [%s]', 'master', ['rosmaster', '--core', '-p', '11311', '__log:=c:\\ros\\home\\log\\9c890ec0-7cde-11e5-93d1-003ee1c5c62d\\master.log'])
#('process[%s]: cwd will be [%s]', 'master', 'c:\\ros\\home')
#def rosmaster_main(argv=sys.argv, stdout=sys.stdout, env=os.environ):
#rosmaster --core -p 11311 __log:=c:\ROS\log\e5670e0f-7cd6-11e5-8c31-003ee1c5c62d\master.log

#i see whats going on, rosmaster_main() is called without arguments from rosmaster file (which is a py file without extension).  It then uses the argv of the command line to launch as a separate process.  It doesnt like bening
#run within python. Might need to change the code there. 

import rosmaster
rosmaster.rosmaster_main(['--core', '-p', '11311'])

#this works
import subprocess
subprocess.Popen(['python','_rosmaster.py', '--core','-p','11311'], cwd="c:\\ros\\root")
#292 in nodeprocess.py needs to do the above since rosmaster can't run as a standalone script on windows like it does on unix
#where rosmaster.py is:

"""
import rosmaster

print 'rosmaster proxy starting up...'
rosmaster.rosmaster_main()

"""
#and if located in ROS_HOME since that is what cwd defaults to.




def go():

    roslaunch.main(['roslaunch','--core'])

#NOTES
Make sure that rosout is in the package path, or you get an earlier error
matches shoudl be  ['/opt/ros/install_isolated/lib/rosout/rosout.exe'], but our matches return 0.  

SOLUTION: packages.py at line 503, if we hardcode matches to locate the exe, then the item SHOULD start.  Yikes. 

launch_node() (launch) -> create_node_process (nodeprocess) ->create_local_process_args (node_args)
