
from pydantic import BaseModel, Field
from enum import Enum


class Model(str, Enum):
    b_max = "B-MAX"
    c_max = "C-MAX"
    ecosport = "EcoSport"
    edge = "Edge"
    escort = "Escort"
    fiesta = "Fiesta"
    focus = "Focus"
    fusion = "Fusion"
    galaxy = "Galaxy"
    grand_c_max = "Grand C-MAX"
    grand_tourneo = "Grand Tourneo Connect"
    ka = "KA"
    ka_plus = "Ka+"
    kuga = "Kuga"
    mondeo = "Mondeo"
    mustang = "Mustang"
    puma = "Puma"
    ranger = "Ranger"
    s_max = "S-MAX"
    streetka = "Streetka"
    tourneo_connect = "Tourneo Connect"
    tourneo_custom = "Tourneo Custom"
    # transit_tourneo = "Transit Tourneo"
    


class Transmission(str,Enum):
    Manual = "Manual"
    Automatic = "Automatic"
    Semi_Auto = "Semi_auto"   
    

class FuelType(str, Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"
    Hybrid = "Hybrid"
    Electric = "Electric"
    # Other = "Other"
    
    
class car_features(BaseModel):
    mileage :float = Field(... , ge=0, description= " Total Mileage" )
    # tax :float = Field(... , ge=0, description= "Tax Amount " ) 
    mpg : float = Field(..., ge=0, description= "Miles per gallon")
    engineSize: float = Field(..., gt=0, le=6.0, description="Engine size in litres")
    car_age : float = Field(..., gt=0, le=30 , description= " Age of Car in years")
    model : Model = Field(..., description="Car Model")
    transmission : Transmission = Field(..., description="Transmission Type")
    fuelType : FuelType = Field(..., description="Fuel Type")
    

class prediction_price(BaseModel):
    prediction :float




