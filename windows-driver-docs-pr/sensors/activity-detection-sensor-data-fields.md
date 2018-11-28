---
title: Activity detection sensor data fields
description: This topic provides information about the data fields that are specific to the activity detection sensor.
ms.assetid: D123C082-9E20-44C2-A9F2-DAC0E09F61B7
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Activity detection sensor data fields


This topic provides information about the data fields that are specific to the activity detection sensor.

The following table shows the data fields. For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description|
| --- | --- | --- | --- |
|PKEY_SensorData_CurrentActivityState|VT_UI4|Required|An indication of the current activity state, expressed as a value of type [<strong>ACTIVITY_STATE</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-activity_state).|
|PKEY_SensorData_CurrentActivityStateConfidence_Percentage|VT_UI2|Required|Confidence level of the sensor in indicating the current activity state.|
|PKEY_SensorData_SubscribedActivityStates|VT_UI4|Required|An indication of the subscribed activity state, expressed as a value of type [<strong>ACTIVITY_STATE</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-activity_state).|
|PKEY_SensorData_ActivityStream|VT_BOOL|Required|Boolean value that is set to TRUE, if an activity stream is available.|
|PKEY_SensorData_ConfidenceThreshold_Percentage|VT_UI2|Required|A threshold value for the sensor's confidence level.|
 

## Related topics


[**ACTIVITY\_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ne-sensorsdef-activity_state)

[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






