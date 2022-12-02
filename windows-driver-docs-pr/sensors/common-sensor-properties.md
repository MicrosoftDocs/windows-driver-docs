---
title: Common sensor properties
description: This topic describes the sensor properties that are common for all sensors.
ms.date: 12/02/2022
---

# Common sensor properties

This topic describes the sensor properties that are common for all sensors.

The following table shows common properties. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Access (R/O, R/W) | Required/Optional | Description |
|---|---|---|---|---|
| PKEY_Sensor_Type | **VT_CLSID** | R/O | Required | The type of sensor. The GUID will consist of the same format as a Windows sensor (for example, SENSOR_TYPE_ACCELEROMETER_3D). For more information about sensor types, see [Sensor type GUIDs](./about-sensor-constants.md). |
| PKEY_Sensor_State | **VT_UI4** | R/O | Required | The state of the sensor. For more information about sensor states, see **[SENSOR_STATE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_state)**. |
| PKEY_Sensor_MinimumDataInterval_Ms | **VT_UI4** | R/O | Required | The minimum time interval (in milliseconds) that the hardware supports for sensor data report generation. |
| PKEY_Sensor_MaximumDataFieldSize_Bytes | **VT_UI4** | R/O | Required | The maximum size returned in a ReadFile call. A ReadFile call allows the native API to allocate a buffer to hold any data field. |
| PKEY_Sensor_Power_Milliwatts | **VT_R4** | R/O | Optional | The sensor power expressed in milliwatts. |
| PKEY_SensorHistory_MaxSize_Bytes | **VT_UI4** | R/O | Optional</br></br>But required, if the sensor supports history. | The maximum size of sensor history data, expressed in bytes. |
| PKEY_SensorHistory_Interval_Ms | **VT_UI4** | R/O | Optional</br></br>But required, if the sensor supports history. | The sensor history sampling interval, expressed in milliseconds. |
| PKEY_SensorHistory_MaximumRecordSize_Bytes | **VT_UI4** | R/O | Optional</br></br>But required, if the sensor supports history. | The maximum record size expressed in bytes. |
| PKEY_Sensor_FifoReservedSize_Samples | **VT_UI4** | R/O | Optional</br></br>But required, if the sensor supports batching. | The number of events reserved for this sensor in the fist-in-first-out (FIFO) buffer for the batch. This guarantees a minimum number of events. If this value is zero, then there is no guarantee that the sensor will perform batching. |
| PKEY_Sensor_FifoMaxSize_Samples | **VT_UI4** | R/O | Optional</br></br>But required, if the sensor supports batching. | The maximum number of events that could be batched in the FIFO. If this value is zero, then batching is not supported by the sensor. The actual number of events may be smaller than this number since the batch FIFO can be shared by multiple sensors. |
| PKEY_Sensor_WakeCapable | **VT_BOOL** | R/O | Optional</br></br>But required, if the sensor supports batching. | Indicates whether the sensor is wake-capable.</br></br>When a sensor supports Sensor batching, this should be set to VARIANT_TRUE, if sensor can wake the application processor when the FIFO is full. And the value should be set to VARIANT_FALSE, if the sensor can't wake the application processor. When this is the case, the state of this property indicates the sensor's ability to wake from Connected Standby.</br></br>If the sensor supports waking a system from SX, this property should be set to VARIANT_TRUE and if it does not support wake from SX, this property should be set to VARIANT_FALSE. |

## Data batching

A sensor driver that supports data batching must report the following common sensor properties:

- PKEY_Sensor_FifoReservedSize_Samples
- PKEY_Sensor_FifoMaxSize_Samples
- PKEY_Sensor_WakeCapable

Starting with Windows 10, version 1511, support is now available for implementing data batching using the HID sensor class driver. For information about this, see [Sensor batching controls](sensor-batching-for-power-saving-.md).

See [EvtSensorSetBatchLatency](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) for information about the callback function related to data batching.

With the additional ability of a sensor to wake up the CPU and Operating system from SX state, PKEY_Sensor_WakeCapable is also used as an enumeration property that can be queried from the PnP driver store to find out whether the sensor is capable of waking up the system from SX in addition to waking the system from connected standby.

## Remarks

When the client driver reports the following properties, the client driver must use **CollectionsListGetMarshalledSizeWithoutSerialization** instead of **CollectionsListGetMarshalledSize**:

- PKEY_SensorHistory_MaxSize_Bytes
- PKEY_SensorHistory_MaximumRecordSize_Bytes

## Related topics

- [EvtSensorSetBatchLatency](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)
- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
- **[SENSOR_STATE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_state)**
- [Sensor type GUIDs](./about-sensor-constants.md)
