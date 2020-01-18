from azure.servicebus import ServiceBusService
import json


def notification_publisher():

    print("Starting")

    bus_service_plate_publisher = ServiceBusService(
        service_namespace="licenseplatepublisher",
        shared_access_key_name='listeneronly',
        shared_access_key_value='w+ifeMSBq1AQkedLCpMa8ut5c6bJzJxqHuX9Jx2XGOk='
    )

    msg = bus_service_plate_publisher.receive_subscription_message('wantedplatelistupdate',
                                                                   'JWWtexQpcUeCjnd9',
                                                                   peek_lock=False)
    message = {}

    if msg.body is not None:

        message = json.load(msg.body.decode())

    return message



