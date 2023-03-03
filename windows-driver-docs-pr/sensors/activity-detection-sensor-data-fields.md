---
title: Activity detection sensor data fields
description: This topic provides information about the data fields that are specific to the activity detection sensor.
ms.date: 03/02/2023
ms.topic: reference
---

# Activity detection sensor data fields

This topic provides information about the data fields that are specific to the activity detection sensor.

The following table shows the data fields. For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_CurrentActivityState | VT_UI4 | Required | An indication of the current activity state, expressed as a value of type **[ACTIVITY_STATE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-activity_state)**. |
| PKEY_SensorData_CurrentActivityStateConfidence_Percentage | VT_UI2 | Required | Confidence level of the sensor in indicating the current activity state. |
| PKEY_SensorData_SubscribedActivityStates | VT_UI4 | Required | An indication of the subscribed activity state, expressed as a value of type **[ACTIVITY_STATE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-activity_state)**. |
| PKEY_SensorData_ActivityStream | VT_BOOL | Required | Boolean value that is set to TRUE, if an activity stream is available. |
| PKEY_SensorData_ConfidenceThreshold_Percentage | VT_UI2 | Required | A threshold value for the sensor's confidence level. |

## Related topics

- **[ACTIVITY_STATE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-activity_state)**
- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
