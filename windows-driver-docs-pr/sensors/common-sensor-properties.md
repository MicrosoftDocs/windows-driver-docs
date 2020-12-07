---
title: Common sensor properties
description: This topic describes the sensor properties that are common for all sensors.
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# Common sensor properties


This topic describes the sensor properties that are common for all sensors.

The following table shows common properties. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key</th>
<th>Type</th>
<th>Access (R/O, R/W)</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_Sensor_Type</p></td>
<td><p>VT_CLSID</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The type of sensor. The GUID will consist of the same format as a Windows sensor (e.g., SENSOR_TYPE_ACCELEROMETER_3D). For more information about sensor types, see <a href="/windows-hardware/drivers/sensors/about-sensor-constants" data-raw-source="[Sensor type GUIDs](./about-sensor-constants.md)">Sensor type GUIDs</a>.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_Sensor_State</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The state of the sensor. For more information about sensor states, see <a href="/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_state" data-raw-source="[&lt;strong&gt;SENSOR_STATE&lt;/strong&gt;](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_state)"><strong>SENSOR_STATE</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_Sensor_MinimumDataInterval_Ms</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The minimum time interval (in milliseconds) that the hardware supports for sensor data report generation.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_Sensor_MaximumDataFieldSize_Bytes</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The maximum size returned in a ReadFile call. A ReadFile call allows the Native API to allocate a buffer to hold any data field.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_Sensor_Power_Milliwatts</p></td>
<td><p>VT_R4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p></td>
<td><p>The sensor power expressed in milliwatts.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorHistory_MaxSize_Bytes</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p>
<p>But required, if the sensor supports History.</p></td>
<td><p>The maximum size of sensor history data, expressed in bytes.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorHistory_Interval_Ms</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p>
<p>But required, if the sensor supports History.</p></td>
<td><p>The sensor history sampling interval, expressed in milliseconds.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorHistory_MaximumRecordSize_Bytes</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p>
<p>But required, if the sensor supports History.</p></td>
<td><p>The maximum record size expressed in bytes.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_Sensor_FifoReservedSize_Samples</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p>
<p>But required, if the sensor supports Batching.</p></td>
<td><p>The number of events reserved for this sensor in the fist-in-first-out (FIFO) buffer for the batch. This guarantees a minimum number of events. If this value is zero, then there is no guarantee that the sensor will perform batching.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_Sensor_FifoMaxSize_Samples</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p>
<p>But required, if the sensor supports Batching.</p></td>
<td><p>The maximum number of events that could be batched in the FIFO. If this value is zero, then batching is not supported by the sensor. The actual number of events may be smaller than this number since the batch FIFO can be shared by multiple sensors.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_Sensor_WakeCapable</p></td>
<td><p>VT_BOOL</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p>
<p>But required, if the sensor supports Batching.</p></td>
<td><p>Indicates whether the sensor is wake-capable.</p>
<p>When a sensor supports Sensor batching, this should be set to VARIANT_TRUE, if sensor can wake the application processor when the FIFO is full. And the value should be set to VARIANT_FALSE, if the sensor can’t wake the application processor. When this is the case, the state of this property indicates the sensor’s ability to wake from Connected Standby.</p>
<p>If the sensor supports waking a system from SX, this property should be set to VARIANT_TRUE and if it does not support wake from SX, this property should be set to VARIANT_FALSE.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Note"></span><span id="note"></span><span id="NOTE"></span>Note


A sensor driver that supports data batching must report the following common sensor properties:

-   PKEY\_Sensor\_FifoReservedSize\_Samples

-   PKEY\_Sensor\_FifoMaxSize\_Samples

-   PKEY\_Sensor\_WakeCapable

Starting with Windows 10, version 1511, support is now available for implementing data batching using the HID sensor class driver. For information about this, see [Sensor Batching Controls](sensor-batching-for-power-saving-.md).

See [EvtSensorSetBatchLatency](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) for information about the callback function related to data batching.

With the additional ability of a sensor to wake up the CPU and Operating system from SX state, PKEY\_Sensor\_WakeCapable is also used as an enumeration property that can be queried from the PnP driver store to find out whether the sensor is capable of waking up the system from SX in addition to waking the system from Connected Standby.

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


When the client driver reports the following properties, the client driver must use **CollectionsListGetMarshalledSizeWithoutSerialization** instead of **CollectionsListGetMarshalledSize**:

-   PKEY\_SensorHistory\_MaxSize\_Bytes

-   PKEY\_SensorHistory\_MaximumRecordSize\_Bytes

## <span id="related_topics"></span>Related topics


[EvtSensorSetBatchLatency](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)

[PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)

[**SENSOR\_STATE**](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_state)

[Sensor type GUIDs](./about-sensor-constants.md)
