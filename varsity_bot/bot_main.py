import rclpy 
from rclpy.node import Node 

from std_msgs.msg import String 
import tkinter as tk 


class BotMain(Node):
    def __init__(self):
        super().__init__("bot_main")

        self.publisher_mode =  self.create_publisher(String, 'robot_mode', 10) 

        timer_period = 0.2 

        self.timer = self.create_timer(timer_period, self.callback_mode)

        self.default_mode = "chatting"
    
    def callback_mode(self):
        msg = String() 
        msg.data = self.default_mode 
        self.publisher_mode.publish(msg) 
    
    def set_default_mode(self, mode):
        self.default_mode = mode 
    
    def publish_msg(self, usr_input):
        msg = String() 
        msg.data = usr_input
        self.publisher_mode.publish(msg) 

class GuiApp:
    def __init__(self, ros_node):
        self.node = ros_node 

        self.window = tk.Tk() 
        self.window.title('Input') 

        self.label = tk.Label(self.window, text="Input sthing") 
        self.label.pack(padx=20, pady=5) 

        self.entry = tk.Entry(self.window, width=40) 
        self.entry.pack(padx=20, pady=7) 

        self.btn = tk.Button(self.window, text="Send", command=self.btn_press)
        self.btn.pack(padx=20, pady=20) 

    def btn_press(self):
        usr_input = self.entry.get() 

        if usr_input == "":
            usr_input = "Chatting" 
        
        if usr_input in ['Chatting', 'Manual', 'Arm', 'Autonomous']:
            self.node.publish_msg(usr_input)
        else:
            print("Error Mode.")
    
    def run(self):
        self.window.mainloop()


def main(args=None):
    rclpy.init(args=args)

    bot_main = BotMain()
    app = GuiApp(bot_main)

    app.run()



if __name__ == '__main__':
    main()