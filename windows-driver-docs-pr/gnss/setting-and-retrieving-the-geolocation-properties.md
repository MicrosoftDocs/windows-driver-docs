---
title: Setting and retrieving the geolocation properties
author: windows-driver-content
description: When an application retrieves a particular property value, a corresponding property-retrieval method is called in the sample driver.
ms.assetid: 576C610E-180A-44A0-9637-5C18341F3777
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting and retrieving the geolocation properties


When an application retrieves a particular property value, a corresponding property-retrieval method is called in the sample driver. For the simulated sensor, this would be **CGeolocation::GetPropertyValuesForGeolocationObject**. The Sensor API will pass the property keys for the properties requested by the application and the driver bundles the property values in an **IPortableDeviceValues** object which it returns to the API.

When an application writes, or updates, a property (such as change sensitivity or the desired accuracy), a corresponding property-write method is called in the sample driver. For the simulated sensor, this would be **CGeolocation::UpdateGeolocationPropertyValues**. This method is declared and defined in the sensor object’s files (Geolocation.h and Geolocation.cpp) and is invoked in the SensorDDI.cpp module.

For information about how the sensor properties are defined, see [Supporting the geolocation properties](supporting-the-geolocation-properties.md).

## Related topics
[Defining the geolocation object](defining-the-geolocation-object.md)  
[Supporting the geolocation properties](supporting-the-geolocation-properties.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Setting%20and%20retrieving%20the%20geolocation%20properties%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


