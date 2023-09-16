from django.dispatch import receiver
from . import signals

@receiver(signals.change_of_state_signal)
def send_notification(state_option, **kwargs):
    print("hi")
