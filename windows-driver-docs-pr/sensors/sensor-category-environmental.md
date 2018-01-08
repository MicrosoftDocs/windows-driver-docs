---
title: SENSOR\_CATEGORY\_ENVIRONMENTAL
description: The SENSOR\_CATEGORY\_ENVIRONMENTAL category contains sensors that provide information about the surrounding environment or weather.
ms.assetid: 49839092-0792-4e89-bc3a-7defc4730937
keywords: ["SENSOR_CATEGORY_ENVIRONMENTAL Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_ENVIRONMENTAL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SENSOR\_CATEGORY\_ENVIRONMENTAL


The SENSOR\_CATEGORY\_ENVIRONMENTAL category contains sensors that provide information about the surrounding environment or weather.

### <span id="platform_defined_sensor_types"></span><span id="PLATFORM_DEFINED_SENSOR_TYPES"></span>Platform-defined Sensor Types

This category includes the following platform-defined sensor types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Sensor type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE</p></td>
<td><p>Barometers.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY</p></td>
<td><p>Hygrometers.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE</p></td>
<td><p>Thermometers.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION</p></td>
<td><p>Weather vanes.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED</p></td>
<td><p>Anemometers.</p></td>
</tr>
</tbody>
</table>

 

### <span id="platform_defined_data_fields"></span><span id="PLATFORM_DEFINED_DATA_FIELDS"></span>Platform-defined Data Fields

This category includes the following platform-defined data fields.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Data type</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Atmospheric pressure in atmospheres (bars).</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Temperature in degrees Celsius.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Relative humidity as a percentage.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Wind direction relative to magnetic north, in degrees. North is represented as 0.0 (top of the x-axis), with values increasing in an anticlockwise</p>
<p>rotation. The z-axis points upwards.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Wind speed in meters per second.</p></td>
</tr>
</tbody>
</table>

 

**Important**   Each platform-defined environmental data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_ENVIRONMENTAL\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

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
<td><p>Version</p></td>
<td><p>Available in Windows 7.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Sensors.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20SENSOR_CATEGORY_ENVIRONMENTAL%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




