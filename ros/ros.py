'''ROS :’
message passing between differeent modules in a distributed system  
package management 
harware abstraction

ways of communicaton between different modules :
message , service , action
messages : implimented using topic : interest to both , package that wants to listen about it(subscriber) and the package that wants to talk about it (publisher)
publisher might not have a set frequency
service means to get info abt a type from any number of modules(service client initiates the transfer and asks for it from a service server at any time ) .
action : the subscriber sends  command to the publisher and it sends intermediate feedback : we can cancel the action in between of the process 
	


A package can be considered a container for your ROS 2 code .
Simplest possible package may have file structure that looks like : 
my_package/
      setup.py
      package.xml
      resource/my_package
one ws can have many packages; cannot have nested package ;
best practice : 
workspace folder /
     src/
         package1 /
             …
         package2 /
             …
         package3 /
             …
to create new package :
        ros2 pkg create --build-type ament_python <package_name>

can run many packages at once : by running colcon build in root (ws root)

to source the workspace =  . install/local_setup.bash

for a new package : we first edit the package.xml file and edit all the TODO points under the description , license  and maintainer sections 	.
license : <license>Apache License 2.0</license>

 and similarly edit the setup.py file also 

package creation command : to be run in the package <src directory : ros2 pkg create –-build-type ament_python <package-name>

Queue size is a required QoS (quality of service) setting that limits the amount of queued messages if a subscriber is not receiving them fast enough.
Queue size is the third attribute in the create_publisher  function
timer_callback function is created :
timer_callback creates a message with the counter value appended, and publishes it to the console with get_logger().info
First the rclpy library is initialized, then the node is created, and then it “spins” the node so its callbacks are called.
After maintainer , description, license in the package.xml, add the following dependencies corresponding to your node’s import statements:
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
This declares the package needs rclpy and std_msgs when its code is executed

then in setup.py after the changes as done in package.xml> under the  entry_points >console_scripts: add the following: 

entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
        ],
}
in setup.cfg < check :: 
[develop]
script-dir=$base/lib/py_pubsub
[install]
install-scripts=$base/lib/py_pubsub

after writing the subcriber’s node, we have to add entry point for the subscriber’s node after the publisher’s entry point in setup.py
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},
run rosdep in the root workspace to check for any missing dependencies =
rosdep install -i --from-path src --rosdistro galactic -y
to get to know the type of service or node : ros2 service type  /<name of the service>
to get info abt the service : ros2 interface show <type_that is found by previous command>
to call service  : ros2 service call <service_name> <service_type> “{values required : got from the previous command}”

'''