
# Secure IoT Gateway with MQTT, TLS and Authentication

This project is a secure IoT gateway prototype designed to simulate how connected devices can send telemetry data to a central gateway in a protected and controlled way.

The system is based on a simulated IoT device that publishes temperature and humidity data through MQTT to a Mosquitto broker. The gateway subscribes to the MQTT topics, processes incoming messages, validates their integrity, and exposes the latest telemetry data through a REST API.

The final goal of the project is to progressively add security layers such as TLS encryption, mutual TLS authentication, MQTT access control rules, HMAC-based message validation, anti-replay protection, and API authentication.

This project demonstrates practical skills in IoT architecture, MQTT communication, Python backend development, Docker, secure communication protocols, and basic cybersecurity principles applied to connected systems.
