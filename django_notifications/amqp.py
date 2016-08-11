import kombu

from django_notifications import settings, models

exchange = kombu.Exchange(
    name=settings.DJANGO_NOTIFICATIONS_AMQP_EXCHANGE,
    type='topic',
)

connection = kombu.Connection(settings.DJANGO_NOTIFICATIONS_AMQP_CONNECTION)

apns_queue = kombu.Queue(
    settings.DJANGO_NOTIFICATIONS_AMQP_QUEUE_PREFIX + models.DeviceOS.iOS.name,
    exchange=exchange,
    routing_key=models.DeviceOS.iOS.name,
)

fcm_queue = kombu.Queue(
    settings.DJANGO_NOTIFICATIONS_AMQP_QUEUE_PREFIX + models.DeviceOS.Android.name,
    exchange=exchange,
    routing_key=models.DeviceOS.Android.name,
)
