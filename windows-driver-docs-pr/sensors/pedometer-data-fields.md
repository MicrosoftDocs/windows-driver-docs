---
title: Pedometer data fields
author: windows-driver-content
description: This topic provides information about the data fields that are specific to the pedometer.
ms.assetid: 35E52085-9727-465D-B6EF-D95974423CD5
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pedometer data fields


This topic provides information about the data fields that are specific to the pedometer.

The following table shows the data fields. For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description|
|--|--|--|--|
|PKEY_SensorData_PedometerStepType|VT_UI4|Required|The step type, expressed as a [PEDOMETER_STEP_TYPE](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-pedometer_step_type) value.|
|PKEY_SensorData_PedometerStepCount|VT_UI4|Required|The number of steps detected.|
|PKEY_SensorData_PedometerStepDuration_Ms|VT_I8|Required|The duration over which the pedometer counted steps. This value is expressed in milliseconds.|
|PKEY_SensorData_PedometerReset|VT_BOOL|Required|Indicates that the pedometer has been reset.|

 

## Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

[**PEDOMETER\_STEP\_TYPE**](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-pedometer_step_type)

 

 






