---
title: Setting and retrieving the geolocation properties
description: When an application retrieves a particular property value, a corresponding property-retrieval method is called in the sample driver.
ms.assetid: 576C610E-180A-44A0-9637-5C18341F3777
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting and retrieving the geolocation properties

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

When an application retrieves a particular property value, a corresponding property-retrieval method is called in the sample driver. For the simulated sensor, this would be **CGeolocation::GetPropertyValuesForGeolocationObject**. The Sensor API will pass the property keys for the properties requested by the application and the driver bundles the property values in an **IPortableDeviceValues** object which it returns to the API.

When an application writes, or updates, a property (such as change sensitivity or the desired accuracy), a corresponding property-write method is called in the sample driver. For the simulated sensor, this would be **CGeolocation::UpdateGeolocationPropertyValues**. This method is declared and defined in the sensor object’s files (Geolocation.h and Geolocation.cpp) and is invoked in the SensorDDI.cpp module.

For information about how the sensor properties are defined, see [Supporting the geolocation properties](supporting-the-geolocation-properties.md).

## Related topics
[Defining the geolocation object](defining-the-geolocation-object.md)  
[Supporting the geolocation properties](supporting-the-geolocation-properties.md)  



