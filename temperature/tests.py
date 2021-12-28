from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
class TestTemperatureConversion(TestCase):
  """
  This class contains tests that convert temperature from Celcius
  to Fahrenheit.
  
  """
  def setUp(self):
    """
    It runs before any execution in each test case.
    
    """
    self.client = Client()
    self.url = reverse("temperature:temperature-conversion")

  def test_celcius_to_fahrenheit_conversion(self):
    """ 
    Tests conversion of celcius to fahrenheit.
    
    """
    celsius_1 = 25.8
    data = {
      "temperature_in_celcius": celsius_1,
    }
    response = self.client.get(self.url, data)
    self.assertContains(response, 78.44)

  def test_fahrenheit_to_celcius_conversion(self):
    """ 
    Tests conversion of farenheit to celcius.
    
    """
    celsius_1 = 25.8
    data = {
      "temperature_in_celcius": celsius_1,
    }
    response = self.client.get(self.url, data)
    self.assertContains(response, 78.44)


