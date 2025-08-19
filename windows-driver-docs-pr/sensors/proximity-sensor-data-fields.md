---
title: Proximity Sensor Data Fields
description: This article provides information about the data fields that are specific to the proximity sensor.
ms.date: 03/06/2024
ms.topic: reference
---

# Proximity sensor data fields

This article provides information about the data fields that are specific to the proximity sensor.

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_ProximityDetection | VT_BOOL | Required | An indication that an object is within proximity of the sensor. |
| PKEY_SensorData_ProximityDistanceMillimeters | VT_UI4 | Optional | Distance to the detected object, in millimeters. |
| PKEY_SensorData_HumanPresence_DetectionDistance_Threshold | VT_R4 | Optional | The distance detection threshold value in millimeters. Only objects located within this distance are reported by the sensor. |
| PKEY_SensorData_HumanPresence_AttentionDetection | VT_BOOL | Optional | Indicates the user's attention status. |
| PKEY_Sensor_Proximity_SensorCapabilities | VT_UI4 | Optional | Contains a bitmap of capability flags defined by the [PROXIMITY_SENSOR_CAPABILITIES](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-proximity_sensor_capabilities) enum. |
| DEVPKEY_Sensor_HumanPresence_MaxDetectablePersonsCount | VT_UI4 | Optional | The maximum number of persons the sensor is able to detect simultaneously. This property is mandatory for sensors that support multi-person detection. |
| PKEY_SensorData_HumanPresence_DetectedPersonsCount | VT_UI4 | Optional | The total number of detected persons reported by the current sensor reading. Detailed per-person data is provided in vector properties below, each element describing one person. Items in vector properties are sorted by distance, starting with the person closest to the device. This property must be present in sensor readings when multi-person detection capability is supported. |
| PKEY_SensorData_HumanPresence_DistanceMillimetersVector | VT_VECTOR\|VT_UI4 | Optional | Each person's distance from the device in millimeters, starting with the person closest to the device. This property must be present in sensor readings when distance detection and multi-person detection capabilities are supported. Max(UI4) value is considered unknown. |
| [PKEY_SensorData_HumanPresence_AttentionVector](#head-position-parameters) | VT_VECTOR\|VT_BOOL | Optional | Each person's engagement state as Boolean values, starting with the person closest to the device. This property must be present in sensor readings when engagement detection and multi-person detection capabilities are supported. Values other than VARIANT_TRUE and VARIANT_FALSE are considered unknown. |
| [PKEY_SensorData_HumanPresence_HeadAzimuthVector](#head-position-parameters) | VT_VECTOR\|VT_R4 | Optional | Each person's head azimuth to the device, in degrees, starting with the person closest to the device. This property must be present in sensor readings when head azimuth detection and multi-person detection capabilities are supported. Values outside of the valid range [-90, 90] are considered unknown. |
| [PKEY_SensorData_HumanPresence_HeadAltitudeVector](#head-position-parameters) | VT_VECTOR\|VT_R4 | Optional | Each person's head altitude to the device, in degrees, starting with the person closest to the device. This property must be present in sensor readings when head altitude detection and multi-person detection capabilities are supported. Values outside of the valid range [-90, 90] are considered unknown. |
| PKEY_SensorData_HumanPresence_HeadRollVector | VT_VECTOR\|VT_R4 | Optional | Each person's head roll in degrees, starting with the person closest to the device. This property must be present in sensor readings when head roll detection and multi-person detection capabilities are supported. Values outside of the valid range [0, 360] are considered unknown. |
| PKEY_SensorData_HumanPresence_HeadPitchVector | VT_VECTOR\|VT_R4 | Optional | Each person's head pitch in degrees, starting with the person closest to the device. This property must be present in sensor readings when head pitch detection and multi-person detection capabilities are supported. Values outside of the valid range [-180, 180] are considered unknown. |
| PKEY_SensorData_HumanPresence_HeadYawVector | VT_VECTOR\|VT_R4 | Optional | Each person's head yaw in degrees, starting with the person closest to the device. This property must be present in sensor readings when head yaw detection and multi-person detection capabilities are supported. Values outside of the valid range [-90, 90] are considered unknown. |
| PKEY_SensorData_HumanPresence_PersonIdVector | VT_VECTOR\|VT_UI4 | Optional | Each person's face correlation IDs, starting with the person closest to the device. Face correlation ID is a unique identifier of a person within the current session. The session is implementation specific. For example, it may be the sensor's current active power state cycle. The purpose of this identifier is to distinguish people from one another as they move within the sensor's field of view. This property must be present in sensor readings when face identification and multi-person detection capabilities are supported. Max(UI4) value is considered unknown. |
| PKEY_SensorData_HumanPresence_HeadAzimuth | VT_R4 | Optional | Head azimuth to the device, in degrees. This property is only used for sensitivity thresholds. Report the sensor data via the corresponding vector property. |
| PKEY_SensorData_HumanPresence_HeadAltitude | VT_R4 | Optional | Head altitude to the device, in degrees. This property is only used for sensitivity thresholds. Report the sensor data via the corresponding vector property. |
| PKEY_SensorData_HumanPresence_HeadRoll | VT_R4 | Optional | Head roll in degrees. This property is only used for sensitivity thresholds. Report the sensor data via the corresponding vector property. |
| PKEY_SensorData_HumanPresence_HeadPitch | VT_R4 | Optional | Head pitch in degrees. This property is only used for sensitivity thresholds. Report the sensor data via the corresponding vector property. |
| PKEY_SensorData_HumanPresence_HeadYaw | VT_R4 | Optional | Head yaw in degrees. This property is only used for sensitivity thresholds. Report the sensor data via the corresponding vector property. |

## Remarks

If a sensor supports the **PKEY_SensorData_ProximityDistanceMillimeters** data field, then in response to a call from **[EvtSensorGetDataFieldProperties](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)** for the **PKEY_SensorData_ProximityDistanceMillimeters** data field, the sensor must report the following data field properties:

| Data field property | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorDataField_RangeMinimum | VT_R4 (float) | Required | Indicates the lower boundary (inclusive) of the sensor's effective detection range in millimeters. |
| PKEY_SensorDataField_RangeMaximum | VT_R4 (float) | Required | Indicates the upper boundary (inclusive) of the sensor's effective detection range in millimeters. |

> [!NOTE]
> The effective detection range is a straight-line distance from the sensor to the object. This distance is measured along the axis in which the sensor is pointing, and it's inclusive of the actual boundaries.

If the driver fails to report these data-field properties, apps will still be able to detect the proximity sensor via the WinRT API. However, these apps won't know the supported-range of the sensor, and might decide not to use the sensor.

### Head position parameters

:::image type="content" source="images/head-position-parameters.png" alt-text="Diagram showing the head position parameters relative to the computer screen.":::

- The convention for X, Y, Z axes is the same as in the device coordinate system used for motion and orientation sensors.
- Axes start at the center of the device's screen.
- The X axis is in the plane of the device's screen, positive towards the right hand side of the screen from the perspective of a user facing the device.
- The Y axis is in the plane of the screen, positive towards the top of the screen.
- The Z is perpendicular to the screen, positive toward a user facing the device.
- Axes are fixed relative to the device and don't change with the device's rotation.
- For non screen-based devices, the axes are defined relative to the devices' front panel.
- If the sensor doesn't support face detection, the reference point for azimuth and altitude might be different from the center of the person's face, as long as it's consistent between different sensor readings.
- Azimuth is the angle between Z axis and XZ-projection of the vector pointing from the sensor device to the center of the person's face. Range [-90, +90]. The angle value is positive in the counterclockwise rotation around Y axis.
- Altitude is the angle between the vector pointing from the sensor device to the center of the person's face and its XZ-projection. Range [-90, +90]. The angle value is positive in the direction of Y axis.

### Head orientation parameters

:::image type="content" source="images/head-orientation-parameters.png" alt-text="Diagram showing the head orientation parameters relative to the computer screen.":::

- Head orientation is described in intrinsic Tait-Bryan angles, applied in roll, pitch, yaw order.
- Roll is the counterclockwise rotation of the person's head around the Z axis, in degrees. Range [0, 360]. In the zero position the Z axis is parallel to the device's Z axis and points from the center of the person's face towards the device.
- Pitch is the counterclockwise rotation of the person's head around the X axis, in degrees. Range [-180, 180]. In the zero position the X axis is parallel to the device's X axis and points from the center of the person's face rightwards from the device's perspective.
- Yaw is the counterclockwise rotation of the person's head around the Y axis, in degrees. Range [-90, 90]. In the zero position the Y axis is parallel to the device's Y axis and points from the center of the person's face upwards.

## Related topics

- [EvtSensorGetDataFieldProperties](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)
- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
