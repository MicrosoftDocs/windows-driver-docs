---
title: SENSOR\_CATEGORY\_MOTION
description: The SENSOR\_CATEGORY\_MOTION category contains sensors that provide information that is related to physical movement.
ms.assetid: 9189aefc-e92d-483c-80da-f61339b14ebd
keywords: ["SENSOR_CATEGORY_MOTION Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_MOTION
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

# SENSOR\_CATEGORY\_MOTION


The SENSOR\_CATEGORY\_MOTION category contains sensors that provide information that is related to physical movement. Accelerometers measure acceleration of the sensor, including gravitational acceleration. Motion detectors, such as human movement detection in a security system, sense moving objects. Gyrometers sense changes in angular velocity. Speedometers measure velocity.

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
<td><p>SENSOR_TYPE_ACCELEROMETER_1D</p></td>
<td><p>One-axis accelerometers.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_ACCELEROMETER_2D</p></td>
<td><p>Two-axis accelerometers.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_ACCELEROMETER_3D</p></td>
<td><p>Three-axis accelerometers.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_GYROMETER_1D</p></td>
<td><p>One-axis gyrometers.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_GYROMETER_2D</p></td>
<td><p>Two-axis gyrometers.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_GYROMETER_3D</p></td>
<td><p>Three-axis gyrometers.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_MOTION_DETECTOR</p></td>
<td><p>Motion detectors, such as those used in security systems.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_SPEEDOMETER</p></td>
<td><p>Rate-of-motion sensors.</p></td>
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
<td><p>SENSOR_DATA_TYPE_ACCELERATION_X_G</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>X-axis acceleration, in <em>g</em>s.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_ACCELERATION_Y_G</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Y-axis acceleration, in <em>g</em>s.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_ACCELERATION_Z_G</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Z-axis acceleration, in <em>g</em>s.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Gyrometric x-axis acceleration, in degrees per second. squared.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Gyrometric y-axis acceleration, in degrees per second squared.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Gyrometric z-axis acceleration, in degrees per second squared.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Gyrometric x-axis velocity, in degrees per second.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Gyrometric y-axis velocity, in degrees per second.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Gyrometric z-axis velocity, in degrees per second.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_MOTION_STATE</p></td>
<td><p><strong>VT_BOOL</strong></p></td>
<td><p><strong>VARIANT_TRUE</strong> if motion is detected, otherwise <strong>VARIANT_FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Speed in meters per second.</p></td>
</tr>
</tbody>
</table>

 

**Important**   Each platform-defined motion data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_MOTION\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20SENSOR_CATEGORY_MOTION%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




