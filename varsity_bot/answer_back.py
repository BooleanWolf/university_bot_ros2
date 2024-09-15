import rclpy 
from rclpy.node import Node 

from std_msgs.msg import String 



class Chatting(Node):
    def __init__(self):
        super().__init__("chatting")

        self.subsciption = self.create_subscription(String, 'robot_mode', self.chat_callback,10)

    def chat_callback(self, msg):
        if msg.data == "Chatting":
            self.get_logger().info("CHATTING MODE ACTIVATED")
            
        else:
            self.get_logger().info("CHATTING MODE DEACTIVATED")

       

def main(args=None):
    rclpy.init(args=args)

    chatting = Chatting() 
    rclpy.spin(chatting)



if __name__ == '__main__':
    main()