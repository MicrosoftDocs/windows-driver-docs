---
title: Pedometer data fields
description: This topic provides information about the data fields that are specific to the pedometer.
ms.date: 03/02/2023
ms.topic: reference
---

# Pedometer data fields

This topic provides information about the data fields that are specific to the pedometer.

The following table shows the data fields. For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_PedometerStepType | VT_UI4 | Required | The step type, expressed as a [PEDOMETER_STEP_TYPE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-pedometer_step_type) value. |
| PKEY_SensorData_PedometerStepCount | VT_UI4 | Required | The number of steps detected. |
| PKEY_SensorData_PedometerStepDuration_Ms | VT_I8 | Required | The duration over which the pedometer counted steps. This value is expressed in milliseconds. |
| PKEY_SensorData_PedometerReset | VT_BOOL | Required | Indicates that the pedometer has been reset. |

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
- **[PEDOMETER_STEP_TYPE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-pedometer_step_type)**
