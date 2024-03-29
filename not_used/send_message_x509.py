import os
import time
import uuid
from azure.iot.device import IoTHubDeviceClient, Message, X509

# The connection string for a device should never be stored in code.
# For the sake of simplicity we are creating the X509 connection string
# containing Hostname and Device Id in the following format:
# "HostName=<iothub_host_name>;DeviceId=<device_id>;x509=true"

hostname = "mqtt-test-iothub.azure-devices.net"

# hostname = os.getenv("HOSTNAME")

# The device that has been created on the portal using X509 CA signing or Self signing capabilities
device_id = "iotdemodevice1"

x509 = X509(
    cert_file="./app/device_sdk/device.crt",
    key_file="./app/device_sdk/device.key",
    pass_phrase="1234",
    # cert_file=os.getenv("X509_CERT_FILE"),
    # key_file=os.getenv("X509_KEY_FILE"),
    # pass_phrase=os.getenv("X509_PASS_PHRASE"),
)


class device_send_message:
    @staticmethod
    def send_message(message: str):
        # The client object is used to interact with your Azure IoT hub.
        device_client = IoTHubDeviceClient.create_from_x509_certificate(
            hostname=hostname, device_id=device_id, x509=x509
        )
        # Connect the client.
        device_client.connect()
        # send 5 messages with a 1 second pause between each message
        msg = Message(message)
        msg.message_id = uuid.uuid4()
        msg.correlation_id = "correlation-1234"
        msg.custom_properties["tornado-warning"] = "yes"
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"
        device_client.send_message(msg)

        # finally, shut down the client
        device_client.shutdown()
        return "msg send successfully. msg: " + message

    @staticmethod
    def on_device_send_message(message: str):
        # The client object is used to interact with your Azure IoT hub.
        device_client = IoTHubDeviceClient.create_from_x509_certificate(
            hostname=hostname, device_id=device_id, x509=x509
        )
        # Connect the client.
        device_client.connect()
        # send 5 messages with a 1 second pause between each message
        msg = Message(message)
        msg.message_id = uuid.uuid4()
        msg.correlation_id = "correlation-1234"
        msg.custom_properties["tornado-warning"] = "yes"
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"

        for _ in range(100):
            device_client.send_message(msg)
            time.sleep(3)

        # finally, shut down the client
        device_client.shutdown()
        return "msg send successfully. msg: " + message
