---
title: Proximity sensor data fields
description: This topic provides information about the data fields that are specific to the proximity sensor.
ms.date: 03/02/2023
ms.topic: reference
---

# Proximity sensor data fields

This topic provides information about the data fields that are specific to the proximity sensor.

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_ProximityDetection | VT_BOOL | Required | An indication that an object is within proximity of the sensor. |
| PKEY_SensorData_ProximityDistanceMillimeters | VT_UI4 | Optional | Distance to the detected object, in millimeters. |
| PKEY_SensorData_HumanPresence_DetectionDistance_Threshold | VT_R4 | Required | The default distance detection threshold value in millimeters. Changes greater than this are reported by the sensor. |
| PKEY_SensorData_HumanPresence_AttentionDetection | VT_BOOL | Optional | Indicates if Attention Detection is supported by the sensor.  |

## Remarks

If a sensor supports the **PKEY_SensorData_ProximityDistanceMillimeters** data field, then in response to a call from [EvtSensorGetDataFieldProperties](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) for the **PKEY_SensorData_ProximityDistanceMillimeters** data field, the sensor must report the following data field *properties*:

| Data field property | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorDataField_RangeMinimum | VT_R4 (float) | Required | Indicates the lower boundary (inclusive) of the sensor's effective detection range in millimeters. |
| PKEY_SensorDataField_RangeMaximum | VT_R4 (float) | Required | Indicates the upper boundary (inclusive) of the sensor's effective detection range in millimeters. |

>[!NOTE]
> The effective detection range is a straight-line distance from the sensor to the object. This distance is measured along the axis in which the sensor is pointing, and it's inclusive of the actual boundaries.

If the driver fails to report these data-field properties, Apps will still be able to detect the proximity sensor via the WinRT API. However, these Apps will not know the supported-range of the sensor, and might decide not to use the sensor.

## Related topics

- [EvtSensorGetDataFieldProperties](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)
- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
