---
title: Magnetometer data fields
description: This topic provides information about the data fields that are specific to the magnetometer.
ms.date: 03/02/2023
ms.topic: reference
---

# Magnetometer data fields

This topic provides information about the data fields that are specific to the magnetometer.

## Data fields

The following table shows the data fields. For more information about the types shown in the type column, see [MSDN PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_MagneticFieldStrengthX_Microteslas | **VT_R4** | Required | The x-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis. |
| PKEY_SensorData_MagneticFieldStrengthY_Microteslas | **VT_R4** | Required | The y-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis. |
| PKEY_SensorData_MagneticFieldStrengthZ_Microteslas | **VT_R4** | Required | The z-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis. |
| PKEY_SensorData_MagnetometerAccuracy | **VT_UI4** | Required | The accuracy of the magnetometer sensor. For more information about valid values, see **[MAGNETOMETER_ACCURACY](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-magnetometer_accuracy)**. |

## Related topics

- **[MAGNETOMETER_ACCURACY](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-magnetometer_accuracy)**
- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
