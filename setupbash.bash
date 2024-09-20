echo "source myenv/bin/activate" >> ~/.bashrc &&
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc &&
source ~/.bashrc

ros2 topic pub --once /Ctrl_val geometry_msgs/msg/Pose2D "{x: 00, y: 0, theta: 0}"
ros2 topic echo /Odom_pub
rviz2