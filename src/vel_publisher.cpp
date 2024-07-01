#include <chrono>
#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

using namespace std::chrono_literals;
using std::placeholders::_1;

class ControlPublisher : public rclcpp::Node {
public:
  ControlPublisher() : Node("control_publisher") {
    publisher_ = create_publisher<geometry_msgs::msg::Twist>(
        "/diff_cont/cmd_vel_unstamped", 10);

    timer_ = create_wall_timer(100ms, std::bind(&ControlPublisher::publishCommands, this));
  }

private:
  void publishCommands() {
    auto message = std::make_shared<geometry_msgs::msg::Twist>();

    // Set the linear and angular velocities for the robot
    message->linear.x = 2.0;
    message->linear.y = 0.0;
    message->linear.z = 0.0;
    message->angular.x = 0.0;
    message->angular.y = 0.0;
    message->angular.z = 1.8;

    publisher_->publish(*message);
  }

  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<ControlPublisher>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}