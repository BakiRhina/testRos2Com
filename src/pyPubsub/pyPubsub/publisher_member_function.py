import rclpy # ROS Client library for python

from rclpy.node import Node # basic class entity in ROS to subscribe and publish to nodes
from std_msgs.msg import String # message type from the 'std_msgs' package representing a simple string

# By passing Node class as an argument of MinimalPublisher class, we are saying that
#this is also a Node, and all properties and methods are inherited by this.

class MinimalPublisher(Node):

    # This is the constructor of the class that will be automatically called when
    #this object (class) is instantiated. In py the constructor is called __init__

    def __init__(self):

        # - This is calling the constructor (__init__) of the parent class (Node) and it's
        #basically creating a 'Node' with the name 'minimal_publisher'
        super().__init__('minimal_publisher')

        # - create_publisher is a method from 'Node' class (from 'rclpy.node') that creates
        #a publisher object that can send (publish) messages to a topic. In this case
        #is publishing a message of type 'String' on a topic named 'topic'.
        # - The integer '10' is a required QoS (Quality of Service) setting that limits the
        #amount of queued messages if a subscriber is not receiving them fast enough.
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds

        # - create_timer is a method from the Node class that sets up a timer to call
        #a specific function periodically (in this case the function timer_callback)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
