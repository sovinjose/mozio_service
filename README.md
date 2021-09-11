Requirements (Prerequisites)
-------------------------------------------------------------------------
Tools and packages required to successfully install this project

Python 3.3 and Django==3.2.7

Installation
-------------------------------------------------------------------------
A step by step list of commands / guide that informs how to install an instance of this project.

pip install -r requirment.txt


Features
-------------------------------------------------------------------------
This project have API endpoints to create, update, delete, and retreive information about providers. A provider contains the following info
    - Name

    - Email
    - Phone Number
    - Language
    - Currency

Once a provider is created we able to start defining service areas. 
the service area will have following information

    - profile id
    - location_name
    - longitude
    - latitude
    - price
     

Using the other API endpoint, we can query the above details. the API take a longitude/latitude pair as arguments and return a list of all polygons that include the given lat/lng.


API reference
-------------------------------------------------------------------------

1.List all service provider details
 
    - GET : http://<IP>/provider/v1/profiles
    
    Response:
    
    '{
          "items": [
                {"id": 1, 
                "name": "sovin", 
                "email": "test@gmail.com", 
                "phone_number": "987897978979", 
                "language": "english", 
                "currency": "USD"
                }], 
          "count": 1
    }'
    
    
2.Get one service provider details


    - GET : http://<IP>/provider/v1/profiles/<ID>
    
    Response:
    
    '{ 
        "id": 1, 
        "name": "sovin", 
        "email": "test@gmail.com", 
        "phone_number": "987897978979", 
        "language": "english", 
        "currency": "USD"
    }'
    
    
3.Create new service provider details.

    - POST : http://<IP>/provider/v1/profiles
    
    Body:
    
    '{ 
        "name": "sovin", 
        "email": "test@gmail.com", 
        "phone_number": "987897978979", 
        "language": "english", 
        "currency": "USD"
    }'
    
    Response: 201
    
4.Update service provider details.

    - PUT : http://<IP>/provider/v1/profiles/<ID>
    
    Body:
    '{ 
        "name": "sovin", 
        "email": "test@gmail.com", 
        "phone_number": "987897978979", 
        "language": "english", 
        "currency": "USD"
    }'
    
    Response: 200
    
4.Update service provider few details.

    - PATCH : http://<IP>/provider/v1/profiles/<ID>
    
    Body:
    '{ 
        "name": "sovin", 
        "email": "test@gmail.com"
    }'
    
    Response: 200
    
5.Delete service provider details.

    - DELETE : http://<IP>/provider/v1/profiles/<ID>
  
    Response: 200


Service Location API
-----------------------------------------------------------------------


1.List all service provider details
 
    - GET : http://<IP>/provider/v1/locations
    
    Response:
    
    '{
          "items": [
               {
                   "profile_pk": 1, 
                   "location_name": 
                   "test123", 
                   "longitude": 1.0, 
                   "latitude": 0.0, 
                   "price": 128
               }
          ], 
          "count": 1
    }'
    
    
2.Get one service provider details


    - GET : http://<IP>/provider/v1/locations/<ID>
    
    Response:
    
    '{ 
       "profile_pk": 1, 
       "location_name": "test123", 
       "longitude": 1.0, 
       "latitude": 0.0, 
       "price": 128
    }'
    
    
3.Create new service provider details.

    - POST : http://<IP>/provider/v1/locations
    
    Body:
    
    '{ 
       "profile_pk": 1, 
       "location_name":  "test123", 
       "longitude": 1.0, 
       "latitude": 0.0, 
       "price": 128
    }'
    
    Response: 201
    
4.Update service provider details.

    - PUT : http://<IP>/provider/v1/locations/<ID>
    
    Body:
    '{ 
       "profile_pk": 1, 
       "location_name": "tes", 
       "longitude": 1.0, 
       "latitude": 0.0, 
       "price": 128
    }'
    
    Response: 200
    
4.Update service provider few details.

    - PATCH : http://<IP>/provider/v1/locations/<ID>
    
    Body:
    '{ 
       "price": 345
    }'
    
    Response: 200
    
5.Delete service provider details.

    - DELETE : http://<IP>/provider/v1/locations/<ID>
  
    Response: 200
    

Retreive info using latitude and longitude


    - GET : http://<IP>/provider/v1/service/list?longitude=1&latitude=0
  
    Response:
    '{
          "items": [
               {
                   {"profile_name": "sovin", "location_name": "test123", "longitude": 1.0, "latitude": 0.0, "price": 123}
               }
          ], 
          "count": 1
    }'
    
    