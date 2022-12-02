---
title: Geomagnetic Orientation
description: This topic provides information about the data fields that are specific to the geomagnetic orientation sensor.
ms.date: 12/01/2022
---

# Geomagnetic orientation

This topic provides information about the data fields that are specific to the geomagnetic orientation sensor.

## Data fields

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description/Comments |
|---|---|---|---|
| PKEY_SensorData_QuaternionW | **VT_R4** | Required | Real coefficient (as opposed to the imaginary portion of the complex number). |
| PKEY_SensorData_QuaternionX | **VT_R4** | Required | X-component of rotational axis vector. |
| PKEY_SensorData_QuaternionY | **VT_R4** | Required | Y-component of rotational axis vector. |
| PKEY_SensorData_QuaternionZ | **VT_R4** | Required | Z-component of rotational axis vector. |
| PKEY_SensorData_DeclinationAngle_Degrees | **VT_R4** | Required | Declination angle. If not supported, the class extension will compute this value. |
| PKEY_SensorData_RotationAngle_Degrees | **VT_R4** | Required for Windows 10 Mobile</br></br>Optional for Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) | Rotation angle, in degrees.</br></br>Drivers that expose a Device Orientation sensor should use this property key for threshold keys. |

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
