---
title: Light sensor data fields
description: This topic provides information about the data fields that are specific to the light sensor.
ms.date: 12/02/2022
---

# Light sensor data fields

This topic provides information about the data fields that are specific to the light sensor.

## Data fields

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_LightLevel_Lux | **VT_R4** | Required | The illuminance level in lux. |
| PKEY_SensorData_LightTemperature_Kelvins | **VT_R4** | Optional | The light temperature in Kelvins. |
| PKEY_SensorData_LightChromaticityX | **VT_R4** | Optional | The x color coordinate on the CIE 1931 chromaticity diagram. |
| PKEY_SensorData_LightChromaticityY | **VT_R4** | Optional | The y color coordinate on the CIE 1931 chromaticity diagram. |
| PKEY_SensorData_IsValid | **VT_BOOL** | Optional | This value must be set to FALSE when the ambient light sensor cannot currently return any valid sample. For example, this value may be set to FALSE when the sensor field of view is obstructed (such as when an object, or the user hand is in front of the sensor). This value should be set to TRUE when the ambient light sensor is able to accurately measure the ambient light. Proper hardware design should try to minimize the time and scenarios requiring this value to be set to FALSE as such scenario prevents the system from properly controlling brightness. On an ideal system, this value is always set to TRUE. |

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
