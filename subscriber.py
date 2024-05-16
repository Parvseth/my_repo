# SUBSCRIBER
import rclpy
from rclpy.node import Node
#from std_msgs.msg import String  # Replace with the correct message type
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from eufs_msgs.msg import WheelSpeedsStamped
from eufs_msgs.msg import ConeArrayWithCovariance
from eufs_msgs.msg import CarState

class SensorDataSubscriber(Node):
    def __init__(self):                              
        super().__init__('sensor_data_subscriber')    
        self.subscription = self.create_subscription(
            WheelSpeedsStamped,                                            # Replaced the correct message type
            'ros_can/wheel_speeds',                                         # Replaced the topic name
            self.listener_callback,                                         # got the above 2 information from the metadata.yaml file , ead it for any info about the msg
            10)
                   

        self.subscription1 = self.create_subscription(
            CarState,
            'ground_truth/state',
            self.listener_callback1 , 
            10
        )
        
        self.subscription2 = self.create_subscription(
            Imu,
            'imu/data',
            self.listener_callback2,
            10
        )
        
        

    def listener_callback(self, msg):
        header = msg.header
        speeds = msg.speeds
        steering = speeds.steering
        lf_speed = speeds.lf_speed
        rf_speed = speeds.rf_speed
        lb_speed = speeds.lb_speed
        rb_speed = speeds.rb_speed
        # log the extracted data     ; it means the lines that gets printed on the terminal 
        self.get_logger().info(f'Received header: {header}')             
        self.get_logger().info(f'Steering angle: {steering} radians')
        self.get_logger().info(f'Left front wheel speed: {lf_speed} RPM')
        self.get_logger().info(f'Right front wheel speed: {rf_speed} RPM')
        self.get_logger().info(f'Left back wheel speed: {lb_speed} RPM')
        self.get_logger().info(f'Right back wheel speed: {rb_speed} RPM')
        print()
        print()
        print()
        
    def listener_callback1(self,msg):
        header = msg.header
        id = msg.child_frame_id
        pose = msg.pose
        twist = msg.twist 
        lin_acce = msg.linear_acceleration
        lin_acc_cov = msg.linear_acceleration_covariance
        slip_angle = msg.slip_angle
        state_of_charge = msg.state_of_charge

        
        # log the extracted data
        self.get_logger().info(f'header={header}')
        self.get_logger().info(f'ID={id}')
        self.get_logger().info(f'Pose={pose}')
        self.get_logger().info(f'Twist={twist}')
        self.get_logger().info(f'Linear Acceleration={lin_acce} m/s^2')
        self.get_logger().info(f'Linear Acceleration Covariance={lin_acc_cov}')
        self.get_logger().info(f'Slip Angle={slip_angle}')
        self.get_logger().info(f'State of charge={state_of_charge}')
        print()
        print()
        print()
    
    def listener_callback2(self,msg):
        header = msg.header
        orientation = msg.orientation
        x1 = orientation.x
        y1 = orientation.y
        z1 = orientation.z
        orientation_cov = msg.orientation_covariance
        x2 = orientation_cov.x
        y2 = orientation_cov.y
        z2 = orientation_cov.z
        ang_vel = msg.angular_velocity 
        x3 = ang_vel.x
        y3 = ang_vel.y  
        z3 = ang_vel.z
        ang_vel_cov = msg.angular_velocity_covariance
        x4 = ang_vel_cov.x
        y4 = ang_vel_cov.y
        z4 = ang_vel_cov.z
        # log the extracted data
        self.get_logger().info(f'header={header}')
        self.get_logger().info(f'Orientation={x1,y1,z1}')
        self.get_logger().info(f'Orientation Covariance={x2,y2,z2}')
        self.get_logger().info(f'Angular Velocity={x3,y3,z3}')
        self.get_logger().info(f'Angular Velocity Covariance={x4,y4,z4}')
        print()
        print()
        print()
        
        



def main(args=None):
    rclpy.init(args=args)
    sensor_data_subscriber = SensorDataSubscriber()
    rclpy.spin(sensor_data_subscriber)
    sensor_data_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
