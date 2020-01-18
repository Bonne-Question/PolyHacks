from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME

bus_service = ServiceBusService(
    service_namespace='licenseplateread',
    shared_access_key_name='ConsumeReads',
    shared_access_key_value='VNcJZVQAVMazTAfrssP6Irzlg/pKwbwfnOqMXqROtCQ=')

bus_service.create_topic('licenseplateread')

topic_options = Topic()
topic_options.max_size_in_megabytes = '5120'
topic_options.default_message_time_to_live = 'PT1M'

bus_service.create_topic('licenseplateread', topic_options)

bus_service.create_subscription('licenseplateread', 'AllMessages')
