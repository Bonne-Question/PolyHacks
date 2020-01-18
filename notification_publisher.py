from azure.servicebus import ServiceBusService
import json


def notification_publisher():

    bus_service_plate_publisher = ServiceBusService(
        service_namespace="licenseplatepublisher",
        shared_access_key_name='wantedplatelistupdate',
        shared_access_key_value='w+ifeMSBq1AQkedLCpMa8ut5c6bJzJxqHuX9Jx2XGOk='
    )

    msg = bus_service_plate_publisher.receive_subscription_message('listeneronly',
                                                                   'JWWtexQpcUeCjnd9',
                                                                   peek_lock=True)

    print(json.loads(msg.body.decode()))


notification_publisher()