---
title: Magnetometer data fields
description: This topic provides information about the data fields that are specific to the magnetometer.
ms.assetid: 5DA5566A-FECA-47ED-8338-686A548687CC
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Magnetometer data fields


This topic provides information about the data fields that are specific to the magnetometer.

The following table shows the data fields. For more information about the types shown in the type column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description|
|--|--|--|--|
|PKEY_SensorData_MagneticFieldStrengthX_Microteslas|VT_R4|Required|The x-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis.|
|PKEY_SensorData_MagneticFieldStrengthY_Microteslas|VT_R4|Required|The y-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis.|
|PKEY_SensorData_MagneticFieldStrengthZ_Microteslas|VT_R4|Required|The z-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis.|
|PKEY_SensorData_MagnetometerAccuracy|VT_UI4|Required|The accuracy of the magnetometer sensor. For more information about valid values, see [<strong>MAGNETOMETER_ACCURACY</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-magnetometer_accuracy).|

 

## Related topics


[**MAGNETOMETER\_ACCURACY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-magnetometer_accuracy)

[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






