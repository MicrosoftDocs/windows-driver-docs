---
title: Orientation sensor data fields
description: This topic provides information about the data fields that are specific to the orientation sensor.
ms.assetid: 4B1FA56E-6956-4BC9-B929-3D78EF933057
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Orientation sensor data fields


This topic provides information about the data fields that are specific to the orientation sensor.

The following table shows the data fields. For more information about the types shown in the type column, see the [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description/Comments|
|---|---|---|---|
|PKEY_SensorData_QuaternionW|VT_R4|Required|Real coefficient (as opposed to the imaginary portion of the complex number) of rotational axis vector.|
|PKEY_SensorData_QuaternionX|VT_R4|Required|X-component of rotational axis vector.|
|PKEY_SensorData_QuaternionY|VT_R4|Required|Y-component of rotational axis vector.|
|PKEY_SensorData_QuaternionZ|VT_R4|Required|Z-component of rotational axis vector.|
|PKEY_SensorData_MagnetometerAccuracy|VT_UI4|Required|The accuracy of the magnetometer sensor. For more information about valid values, see [MAGNETOMETER_ACCURACY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-magnetometer_accuracy).|
|PKEY_SensorData_DeclinationAngle_Degrees|VT_R4|Optional|Magnetic declination angle used to infer the true north from the earth's magnetic north. If not supported, the class extension will compute this value.|
|PKEY_SensorData_LinearAccelerationX_Gs|VT_R4|Optional|X-axis linear acceleration in g’s|
|PKEY_SensorData_LinearAccelerationY_Gs|VT_R4|Optional|Y-axis linear acceleration in g’s|
|PKEY_SensorData_LinearAccelerationZ_Gs|VT_R4|Optional|Z-axis linear acceleration in g’s|
|PKEY_SensorData_CorrectedAngularVelocityX_DegreesPerSecond|VT_R4|Optional|Gyrometric X-axis velocity, in degrees per second.|
|PKEY_SensorData_CorrectedAngularVelocityY_DegreesPerSecond|VT_R4|Optional|Gyrometric Y-axis velocity, in degrees per second.|
|PKEY_SensorData_CorrectedAngularVelocityZ_DegreesPerSecond|VT_R4|Optional|Gyrometric Z-axis velocity, in degrees per second.|


## Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20Device%20orientation%20sensor%20data%20fields%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





