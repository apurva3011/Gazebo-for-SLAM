#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


class Turtle:
    def __init__(self):
        rospy.init_node('traverse', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def stop():
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        self.velocity_publisher.publish(vel_msg)
        return

    def straight(self,time,speed):
        vel_msg = Twist()  
        vel_msg.linear.x = abs(speed)

        # Since we are moving just in x-axis
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        while not rospy.is_shutdown():

            t = rospy.Time.now().to_sec()

            # Loop to move the turtle in an specified distance
            while time-t =! 0:
                self.velocity_publisher.publish(vel_msg)
                t = rospy.Time.now().to_sec()
                
    vel_msg.linear.x = 0
    self.velocity_publisher.publish(vel_msg)
        return

    def rotate(self, time, speed, clockwise):
        vel_msg = Twist()

        angular_speed = speed
       
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0

        # Checking if our movement is CW or CCW
        if clockwise:
            vel_msg.angular.z = -abs(angular_speed)
        else:
            vel_msg.angular.z = abs(angular_speed)
        
        t = rospy.Time.now().to_sec()

            # Loop to move the turtle in an specified distance
            while time-t =! 0:
                self.velocity_publisher.publish(vel_msg)
                t = rospy.Time.now().to_sec()
        
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        return


if __name__ == "__main__":
    turtle = Turtle()
    turtle.straight(16,0.22)
    turtle.rotate(8, 0.2, True)
    turtle.straight(16,0.22)
    turtle.rotate(16, 0.2, False)
    turtle.straight(16,0.22)
    turtle.rotate(8, 0.2, True)
    turtle.straight(16,0.22)
    turtle.rotate(16, 0.2, False)
    turtle.straight(11,0.22)
    turtle.rotate(8, 0.2, True)
    turtle.straight(16,0.22)
    turtle.rotate(16, 0.2, False)
    turtle.straight(16,0.22)
    turtle.rotate(8, 0.2, False)
    turtle.straight(40,0.22)
    # initial
    turtle.rotate(16, 0.2, False)
    turtle.straight(3,0.22)
    turtle.rotate(3, 0.2, True)
    turtle.straight(3,0.22)
    turtle.rotate(16, 0.2, False)
    turtle.straight(3,0.22)
    turtle.rotate(8, 0.2, False)
    turtle.straight(3,0.22)
    turtle.stop()
