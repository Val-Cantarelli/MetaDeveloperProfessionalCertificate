from django.test import TestCase
from datetime import datetime
from .models import Reservation

class ReservationModelTest(TestCase):
    @classmethod
    # Prepara os dados para testes
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            name = "John",
            last_name="McQueen"
            
        )
        
    def test_fields(self):
        # teste acontece
        self.assertIsInstance(self.reservation.name, str)
        self.assertIsInstance(self.reservation.last_name, str)    

    def test_timestamps(self):
        # teste acontece
        self.assertIsInstance(self.reservation.booking_time, datetime)