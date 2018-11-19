---
title: Sensor Properties
description: The Sensor and Location platform defines constants that identify properties for sensors. Sensor manufacturers can also define their own properties.
ms.assetid: a9f88dad-a81d-45dc-b607-e7b4c5036774
topic_type:
- apiref
api_name:
- SENSOR_PROPERTY_ACCURACY
- SENSOR_PROPERTY_CHANGE_SENSITIVITY
- SENSOR_PROPERTY_CONNECTION_TYPE
- SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL
- SENSOR_PROPERTY_DESCRIPTION
- SENSOR_PROPERTY_DEVICE_PATH
- SENSOR_PROPERTY_FRIENDLY_NAME
- SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE
- SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY
- SENSOR_PROPERTY_MANUFACTURER
- SENSOR_PROPERTY_MIN_REPORT_INTERVAL
- SENSOR_PROPERTY_MODEL
- SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID
- SENSOR_PROPERTY_RANGE_MAXIMUM
- SENSOR_PROPERTY_RANGE_MINIMUM
- SENSOR_PROPERTY_RESOLUTION
- SENSOR_PROPERTY_SERIAL_NUMBER
- SENSOR_PROPERTY_STATE
- SENSOR_PROPERTY_TURN_ON_OFF_NMEA
- SENSOR_PROPERTY_TYPE
- WPD_FUNCTIONAL_OBJECT_CATEGORY
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# Sensor Properties


The Sensor and Location platform defines constants that identify properties for sensors. Sensor manufacturers can also define their own properties.

The platform defines the following **PROPERTYKEY** values for sensor properties. These properties are read-only unless otherwise noted.

Each platform-defined sensor property **PROPERTYKEY** is based on a common **GUID** named SENSOR\_PROPERTY\_COMMON\_GUID:

{7F8383EC-D3EC-495C-A8CF-B8BBE85C2920}.

**Important**   Do not use this base value to define your own property keys.

 

Values for properties designated as read/write can be specified by the client application. Values for properties designated as static must not change over time. Properties designated as required must be supported by the sensor.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key name and PID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_ACCURACY_"></span><span id="sensor_property_accuracy_"></span>
<strong>SENSOR_PROPERTY_ACCURACY</strong>
(PID = 17)</td>
<td><p><strong>VT_UNKNOWN</strong></p>
<p>Read only. <a href="http://go.microsoft.com/fwlink/p/?linkid=134660" data-raw-source="[IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=134660)">IPortableDeviceValues</a> object that contains sensor data type names and their associated accuracies. Accuracy values represent possible variation from true values. Accuracy values are expressed by using the same units as the data field, except when otherwise documented.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_CHANGE_SENSITIVITY"></span><span id="sensor_property_change_sensitivity"></span>
<strong>SENSOR_PROPERTY_CHANGE_SENSITIVITY</strong>
(PID = 14)</td>
<td><p><strong>VT_UNKNOWN</strong></p>
<p>Read/write. <strong>IPortableDeviceValues</strong> object that contains sensor data type names and their associated change sensitivity values. Change sensitivity values provide requests about the amount by which the data field should change before the SENSOR_EVENT_DATA_UPDATED event is raised.</p>
<p>Sensitivity values are expressed by using the same units as the data field, except where otherwise documented.</p>
<p>For some sensors, the change sensitivity is interpreted as an actual value. For example, a change sensitivity value of 2 for SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS represents a sensitivity of plus or minus 2 degrees Celsius.</p>
<p>For other sensors, like the ambient light sensor (ALS), the change sensitivity is interpreted as a percent. So, a change sensitivity of 2 for SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX represents plus or minus 2% of LUX.</p>
<p>You can set this value to request a particular change sensitivity, but multiple applications could be using the same sensor. Therefore, sensors determine the true change sensitivity, based on their internal logic. For example, the sensor might always use the smallest change sensitivity that is requested by any of the applications.</p>
<p>If an application sets this property to VT_NULL, the device driver should reset SENSOR_PROPERTY_CHANGE_SENSITIVITY to its default value.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_CONNECTION_TYPE"></span><span id="sensor_property_connection_type"></span>
<strong>SENSOR_PROPERTY_CONNECTION_TYPE</strong>
(PID = 11)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Read only. <a href="https://msdn.microsoft.com/library/windows/desktop/dd318902" data-raw-source="[&lt;strong&gt;SensorConnectionType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/dd318902)"><strong>SensorConnectionType</strong></a> value that contains the current connection type.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL"></span><span id="sensor_property_current_report_interval"></span>
<strong>SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL</strong>
(PID = 13)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Read/write. The current elapsed time for sensor data report generation, in milliseconds.</p>
<p>Setting a value of zero signals the driver to return either: the default report interval, or, the smallest report interval. If there is only one client connected, the driver should return the default report interval. If multiple clients are connected, the driver should return the smallest interval requested by any of those clients.</p>
<p>Applications can set this value to request a particular report interval, but multiple applications could be using the same driver. Therefore, drivers determine the true report interval, based on internal logic. For example, the driver might always use the shortest report interval that is requested by any caller.</p>
<p>For an example of how to use this property, see <a href="https://msdn.microsoft.com/library/windows/desktop/dd319014" data-raw-source="[Using Sensor API Events](https://msdn.microsoft.com/library/windows/desktop/dd319014)">Using Sensor API Events</a>.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_DESCRIPTION"></span><span id="sensor_property_description"></span>
<strong>SENSOR_PROPERTY_DESCRIPTION</strong>
(PID = 10)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Read only. The sensor description string.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_DEVICE_PATH"></span><span id="sensor_property_device_path"></span>
<strong>SENSOR_PROPERTY_DEVICE_PATH</strong>
(PID = 15)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Read only. Uniquely identifies the device instance with which the sensor is associated. You can use this property to determine whether a device contains multiple sensors.</p>
<p>Device drivers do not have to support this property because the platform provides this value to applications without querying drivers.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_FRIENDLY_NAME"></span><span id="sensor_property_friendly_name"></span>
<strong>SENSOR_PROPERTY_FRIENDLY_NAME</strong>
(PID = 9)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Read only. Required, static. The friendly name for the device.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE"></span><span id="sensor_property_light_response_curve"></span>
<strong>SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE</strong>
(PID = 16)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Read only. A counted array that contains pairs of values that provide a mapping between ambient light levels and offsets. These values are expressed as percentages. The adaptive brightness feature in Windows applies these values to the user&#39;s current display brightness preference.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This property actually contains each value as a 4-byte unsigned integer (<strong>VT_UI4)</strong>. For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY"></span><span id="sensor_property_location_desired_accuracy"></span>
<strong>SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY</strong>
(PID = 19)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Read/write. A value from the <a href="https://msdn.microsoft.com/library/windows/desktop/dd756639" data-raw-source="[&lt;strong&gt;LOCATION_DESIRED_ACCURACY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/dd756639)"><strong>LOCATION_DESIRED_ACCURACY</strong></a> enumeration that indicates the type of accuracy handling requested by a client application.</p>
<p><strong>LOCATION_DESIRED_ACCURACY_DEFAULT</strong> (0) indicates that the sensor should use the accuracy for which it can optimize power use and other cost considerations.</p>
<p><strong>LOCATION_DESIRED_ACCURACY_HIGH</strong> (1) indicates that the sensor should deliver the most accurate report possible. This includes using services that might charge money, or consuming higher levels of battery power or connection bandwidth.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_MANUFACTURER"></span><span id="sensor_property_manufacturer"></span>
<strong>SENSOR_PROPERTY_MANUFACTURER</strong>
(PID = 6)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Read only. Required, static. The manufacturer&#39;s name.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_MIN_REPORT_INTERVAL"></span><span id="sensor_property_min_report_interval"></span>
<strong>SENSOR_PROPERTY_MIN_REPORT_INTERVAL</strong>
(PID = 12)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Read only. Required, static. The minimum interval that the hardware supports for sensor data report generation, in milliseconds.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_MODEL"></span><span id="sensor_property_model"></span>
<strong>SENSOR_PROPERTY_MODEL</strong>
(PID = 7)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Read only. Required, static. The sensor model name.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID"></span><span id="sensor_property_persistent_unique_id"></span>
<strong>SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID</strong>
(PID = 5)</td>
<td><p><strong>VT_CLSID</strong></p>
<p>Read only. Required, static. A <strong>GUID</strong> that identifies the sensor. This value must be unique for each sensor on a device, or across devices of the same model as enumerated on the computer. This property contains the same value obtained by calling <a href="https://msdn.microsoft.com/library/windows/desktop/dd318873" data-raw-source="[&lt;strong&gt;ISensor::GetID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/dd318873)"><strong>ISensor::GetID</strong></a> .</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_RANGE_MAXIMUM"></span><span id="sensor_property_range_maximum"></span>
<strong>SENSOR_PROPERTY_RANGE_MAXIMUM</strong>
(PID = 21)</td>
<td><p><strong>VT_UKNOWN</strong></p>
<p>Read only. <strong>IPortableDeviceValues</strong> object that contains sensor data field names and their associated maximum values.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_RANGE_MINIMUM"></span><span id="sensor_property_range_minimum"></span>
<strong>SENSOR_PROPERTY_RANGE_MINIMUM</strong>
(PID = 20)</td>
<td><p><strong>VT_UKNOWN</strong></p>
<p>Read only. <strong>IPortableDeviceValues</strong> object that contains sensor data field names and their associated minimum values.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_RESOLUTION"></span><span id="sensor_property_resolution"></span>
<strong>SENSOR_PROPERTY_RESOLUTION</strong>
(PID = 18)</td>
<td><p><strong>VT_UKNOWN</strong></p>
<p>Read only. <strong>IPortableDeviceValues</strong> object that contains sensor data field names and their associated resolutions. Resolution values represent sensitivity to change in the data field.</p>
<p>Resolution values are expressed by using the same units as the data field, except when otherwise documented.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_SERIAL_NUMBER"></span><span id="sensor_property_serial_number"></span>
<strong>SENSOR_PROPERTY_SERIAL_NUMBER</strong>
(PID = 8)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Read only. Required, static. The sensor serial number.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_STATE"></span><span id="sensor_property_state"></span>
<strong>SENSOR_PROPERTY_STATE</strong>
(PID = 3)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Read only. Required.</p>
<p><a href="https://msdn.microsoft.com/library/windows/desktop/dd318905" data-raw-source="[&lt;strong&gt;SensorState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/dd318905)"><strong>SensorState</strong></a> value that contains the current sensor state.</p>
<div class="alert">
<strong>Note</strong>  To update this property, raise a state-changed event by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545523" data-raw-source="[&lt;strong&gt;ISensorClassExtension::PostStateChange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545523)"><strong>ISensorClassExtension::PostStateChange</strong></a>.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_PROPERTY_TURN_ON_OFF_NMEA"></span><span id="sensor_property_turn_on_off_nmea"></span>
<strong>SENSOR_PROPERTY_TURN_ON_OFF_NMEA</strong>
(PID = 3)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Read/write. If TRUE, an NMEA sentence will be included in data reports. If False, NMEA sentence is not included.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_PROPERTY_TYPE"></span><span id="sensor_property_type"></span>
<strong>SENSOR_PROPERTY_TYPE</strong>
(PID = 2)</td>
<td><p><strong>VT_CLSID</strong></p>
<p>Read only. Required, static. A <strong>GUID</strong> that identifies the sensor type. Platform-defined sensor types are defined in Sensors.h.</p></td>
</tr>
</tbody>
</table>

The following Windows Portable Devices (WPD) property must be supported by all sensors.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="WPD_FUNCTIONAL_OBJECT_CATEGORY"></span><span id="wpd_functional_object_category"></span>
<strong>WPD_FUNCTIONAL_OBJECT_CATEGORY</strong></td>
<td><p><strong>VT_CLSID</strong></p>
<p>Read only. Required, static. Defines the sensor category.</p></td>
</tr>
</tbody>
</table>

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 7</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>None supported</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Sensors.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**GetProperties**](https://msdn.microsoft.com/library/windows/desktop/dd318874)

[**GetProperty**](https://msdn.microsoft.com/library/windows/desktop/dd318876)

[IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=275070)

[**SetProperties**](https://msdn.microsoft.com/library/windows/desktop/dd318899)

 

 






