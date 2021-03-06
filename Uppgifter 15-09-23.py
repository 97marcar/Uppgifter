# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:40:56 2015

@author: 97marcar
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:07:30 2015

@author: 97marcar
"""
from random import *

class Crop:
  """A generic food crop"""
  
  #constructor
  def __init__(self, growth_rate, light_need, water_need):
    """konstruktor"""
    self._growth = 0
    self._days_growing = 0
    self._growth_rate = growth_rate
    self._light_need = light_need
    self._water_need = water_need
    self._status = "seed"
    self._type = "Generic"
    
  def needs(self):
    """status about how much light and water is needed."""
    return({'light need': self._light_need, 'water need': self._water_need})
    
  def report(self):
    return({'type': self._type, 'status': self._status, 'growth': self._growth, 'days growing': self._days_growing})

  def get_growth(self):
    """gives the user the value of growth"""
    return(self._growth)
  
  def set_growth(self,growth):
    """sets the value of """
    self._growth = growth
    
  def get_days_growing(self):
    """gives the user the value of days growing"""
    return(self.get_days_growing)
  
  def set_days_growing(self, days_growing):
    """sets the value of days growing"""
    self._days_growing = days_growing
    

  def get_growth_rate(self):
    """gives the user the value of the growth rate"""
    return(self._growth_rate)
  
  def set_growth_rate(self,growth_rate):
    """sets the value of the growth rate"""
    self._growth_rate = growth_rate
    
  def get_light_need(self):
    """gives the user the value of light needed"""
    return(self._light_need)
  
  def set_light_need(self,light_need):
    """sets the value of light needed"""
    self._light_need = light_need
    
  def get_water_need(self):
    """gives the user the value of water needed"""
    return(self._water_need)
  
  def set_water_need(self,water_need):
    """sets the value of water needed"""
    self._water_need = water_need
    
  def get_status(self):
    """gives the user the status of the crop"""
    return(self._status)
  
  def set_status(self,status):
    """sets the status of the crop"""
    self._status = status

  def get_type(self):
    """gives the user the type of the seed"""
    return(self._type)
  
  def set_type(self,new_type):
    """sets the type of the seed """
    self._type = new_type
    
  def _update_status(self):
    if self._growth > 15:
      self._status = "Old"
    elif self._growth > 10:
      self._status = "Mature"
    elif self._growth > 5:
      self._status = "Young"
    elif self._growth > 0:
      self._status = "Seedling"
    elif self._status == 0:
      self._status = "Seed"
      
    
  def grow(self, light, water):
    if light >= self._light_need and water >= self._water_need:
      self._growth += self._growth_rate
    #increment days growing
    self._days_growing += 1
    #update status
    self._update_status()
    


def auto_grow(crop, days):
  for day in range(days):
    light = randint(1,10)
    water = randint(1,10)
    crop.grow(light, water)
    
def manual_grow(crop):
  valid = False
  while not valid:
    try:
      light = int(input("Please enter a light value (1-10): "))
      if 1 <= light <= 10:
        valid = True
      else:
        print("not a valid number please choose a number between 1 and 10")
    except ValueError:
       print("not a valid number please choose a number between 1 and 10")
       
  valid = False
  while not valid:
    try:
      water = int(input("Please enter a water value (1-10): "))
      if 1 <= water <= 10:
        valid = True
      else:
        print("not a valid number please choose a number between 1 and 10")
    except ValueError:
       print("not a valid number please choose a number between 1 and 10")
  crop.grow(light, water)
     
def display_menu():
  print("1. Grow manually over 1 day")
  print("2. Grow automatically over 30 days")
  print("3. Report status")
  print("0. Exit test program")
  
def menu_choice():
  option_valid = False
  while not option_valid:
    try:
      choice = int(input("Option Selected: "))
      if 0 <= choice <= 4:
        option_valid = True
      else:
        print("Please enter a valid option")
        
    except ValueError:
      print("Please enter a valid option")
    return choice
    
    
def manage_crop(crop):
  print("This is the crop management program")
  print()
  noexit = True
  while noexit:
    display_menu()
    option = menu_choice()
    print()
    if option == 1:
      manual_grow(crop)
      print()
    elif option == 2:
      auto_grow(crop, 30)
    elif option == 3:
      print(crop.report())
    elif option == 0:
      noexit = False
      print()
  print("Thank you for using the management program")
     
def main():
   #instaniate the class
   new_crop = Crop(1,4,3)
   
   print(new_crop.get_status())
   print(new_crop.get_growth())
   
   print(new_crop.get_light_need())
   print(new_crop.get_water_need())
   print(new_crop.report())
   print(new_crop.needs())
  
   manage_crop(new_crop)
   print(new_crop.report())
   print(new_crop.needs())
   new_crop2 = Crop(2,5,7)
   print(new_crop2.get_status())
   print(new_crop2.get_light_need())
   print(new_crop2.get_water_need())
   
   
  
   
if __name__ == "__main__":
  main()