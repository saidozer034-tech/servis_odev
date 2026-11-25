# RectangleArea ROS 2 Servisi

## Derleme Komutları
```bash
cd ~/ros2_ws
colcon build --packages-select alan_interfaces alan_py
source install/setup.bash
```

## Çalıştırma Komutları
**Sunucu:**
```bash
ros2 run alan_py alan_server
```

**İstemci:**
```bash
ros2 run alan_py alan_client 5.0 4.0
```

**Negatif Değer Kontrolü (Bonus):**
```bash
ros2 run alan_py alan_client -3.0 4.0
```

**Manuel Servis Çağrısı (ros2 service call):**
```bash
ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.0, height: 3.5}"
```

## Doğrulama Çıktısı
```text
$ ros2 run alan_py alan_client 5.0 4.0
[INFO] [1795162614.020564070] [rectangle_area_client]: Alan: 20.0 (success=True)

$ ros2 run alan_py alan_client -3.0 4.0
[ERROR] [1795162614.565351057] [rectangle_area_client]: Istek reddedildi: Negatif deger girilemez! (success=False)

$ ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.0, height: 3.5}"
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.0, height=3.5)

response:
alan_interfaces.srv.RectangleArea_Response(area=21.0, success=True)
```
