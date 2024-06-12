import rclpy
from rclpy.node import Node

class MyNode(node) :
    def __init__(self) :
        super().__init__("name_of_node")              # super with init is a way to call the parent class constuctor, and "name_of_node" is arguement for the parent class's constuctor
        self.get_logger().info("ROS2")
    
def main(args=None) :
    rclpy.init(args=args)   # ROS 2 client library is being initialized with the provided arguments
    node= "MyNode"
    rclpy.spin(node)
    rclpy.shutdown()

if  __name__ == '__main__':              # This idiom is used to ensure that the main() function is only executed when the script is run directly, and not when it's imported as a module. 
    main()

