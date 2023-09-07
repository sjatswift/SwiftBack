from django.db import models
from rootApp.models import SwiftUser
import json

# Load the JSON data
with open('apis/JSONdata/vehicle.json', 'r') as json_file:
    vehicleJSON = json.load(json_file)

# Create a list of all possible vehicle models from the JSON data
all_vehicle_models = [(model, model) for company in vehicleJSON["car_makers"] for model in company["models"]]


COLOR_CHOICES = [
    ("Red", "Red"),
    ("Blue", "Blue"),
    ("Green", "Green"),
    ("Yellow", "Yellow"),
    ("Orange", "Orange"),
    ("Purple", "Purple"),
    ("Pink", "Pink"),
    ("Brown", "Brown"),
    ("Black", "Black"),
    ("White", "White"),
    ("Gray", "Gray"),
    ("Cyan", "Cyan"),
    ("Magenta", "Magenta"),
]


class Vehicles(models.Model):
    driver = models.OneToOneField(SwiftUser, on_delete=models.CASCADE, null=True, blank=True)
    
    # Define choices for vehicle company
    vehicle_company_data_CHOICES = [(company["name"], company["name"]) for company in vehicleJSON["car_makers"]]
    vehicle_company = models.CharField(max_length=100, choices=vehicle_company_data_CHOICES)
    
    # Define choices for vehicle model based on the selected company
    def vehicle_model_choices(self):
        selected_company = self.vehicle_company
        for company in vehicleJSON["car_makers"]:
            if company["name"] == selected_company:
                return [(model, model) for model in company["models"]]
        return []

    vehicle_model = models.CharField(max_length=100, choices=all_vehicle_models, blank=True)
    registration_number = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES,default="Unknown")
    vehicle_pic = models.ImageField(upload_to='media/vehicle_pics/')
