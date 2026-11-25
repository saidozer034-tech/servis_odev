import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class RectangleAreaServer(Node):

    def __init__(self):
        super().__init__('rectangle_area_server')
        self.srv = self.create_service(
            RectangleArea,
            'rectangle_area',
            self.calculate_area_callback
        )
        self.get_logger().info('RectangleArea servisi hazir. Istek bekleniyor...')

    def calculate_area_callback(self, request, response):
        if request.width < 0.0 or request.height < 0.0:
            response.area = 0.0
            response.success = False
            self.get_logger().warn(
                f'Negatif deger reddedildi: width={request.width}, height={request.height}'
            )
            return response

        response.area = request.width * request.height
        response.success = True
        self.get_logger().info(
            f'Hesaplandi: {request.width} x {request.height} = {response.area}'
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = RectangleAreaServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
