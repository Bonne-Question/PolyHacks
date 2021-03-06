from azure.servicebus import ServiceBusService
import json


def license_plate_publisher():

    bus_service_plate_publisher = ServiceBusService(
        service_namespace="licenseplatepublisher",
        shared_access_key_name='ConsumeReads',
        shared_access_key_value='VNcJZVQAVMazTAfrssP6Irzlg/pKwbwfnOqMXqROtCQ='
    )

    msg = bus_service_plate_publisher.receive_subscription_message('licenseplateread',
                                                                   'r6GKjeC7ZaLkC46B',
                                                                   peek_lock=True)
    if msg.body is not None:

        return json.loads(msg.body.decode())

    return {}



