from .signals import change_of_state_signal 

def send_ride_started_notif(SwiftUser):
    change_of_state_signal.send(sender=SwiftUser,state_option="En Route")