import random
import time
import json
from awscrt import io, mqtt, auth, http
from awscrt.mqtt import QoS
from awsiot import mqtt_connection_builder
from temperature_test import get_soil_temperature
from soil_input import pipe


# Callback when connection is accidentally lost.
def on_connection_interrupted(connection, error, **kwargs):
    print("Connection interrupted. error: {}".format(error))


# Callback when an interrupted connection is re-established.
def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print("Connection resumed. return_code: {} session_present: {}".format(return_code, session_present))


def build_direct_mqtt_connection(on_connection_interrupted, on_connection_resumed):
    # proxy_options = get_proxy_options_for_mqtt_connection()

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint='a11fs45h9s9xh3-ats.iot.ap-southeast-2.amazonaws.com',
        # port=self.get_command_required("port"),
        cert_filepath="certs/iot-certificate.pem.crt",
        pri_key_filepath="certs/iot-private.pem.key",
        ca_filepath="certs/AmazonRootCA1.pem",
        on_connection_interrupted=on_connection_interrupted,
        on_connection_resumed=on_connection_resumed,
        # client_id=self.get_command_required("client_id"),
        clean_session=False,
        client_id='3e47ac1d551a3b8d062aa546fac39aff16652fe10e366696486a81265ae248e8',
        keep_alive_secs=30)
        # http_proxy_options=proxy_options)
    return mqtt_connection


if __name__ == '__main__':

    mqtt_connection = build_direct_mqtt_connection(on_connection_interrupted, on_connection_resumed)

    connect_future = mqtt_connection.connect()

    #Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")

    while True:
        
        #temperature = round(random.uniform(0.0, 100.0), 2)
        temperature = get_soil_temperature()
        if temperature:
            payload = {
             #'serial': 'iot_assigment_device_1',
                'assetId': '8a3b3d23-8005-4508-bef4-aba59cc32abb',
                'serial': 'a26721a6-a16b-4802-97ac-60f623c41920',
                'temperature': temperature,
                'timestamp': round(time.time(), 0)
            }
            print("publish message {}".format(json.dumps(payload)))
            mqtt_connection.publish(topic='iot/temperature', payload=json.dumps(payload), qos=QoS.AT_LEAST_ONCE)
            
        
        
        for moisture in pipe():
            payload = {
             #'serial': 'iot_assigment_device_1',
                'assetId': '8a3b3d23-8005-4508-bef4-aba59cc32abb',
                'serial': 'a26721a6-a16b-4802-97ac-60f623c41920',
                'moisture': moisture,
                'timestamp': round(time.time(), 0)
            }
            print("publish message {}".format(json.dumps(payload)))
            mqtt_connection.publish(topic='iot/moisture', payload=json.dumps(payload), qos=QoS.AT_LEAST_ONCE)

    # Disconnect
    # print("Disconnecting...")
    # disconnect_future = mqtt_connection.disconnect()
    # disconnect_future.result()
    # print("Disconnected!")