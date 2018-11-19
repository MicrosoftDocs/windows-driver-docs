---
title: SENSOR\_CATEGORY\_LIGHT
description: The SENSOR\_CATEGORY\_LIGHT category contains sensors that provide information about characteristics of light.
ms.assetid: 56bb4869-3752-437d-89c9-829e6fb01043
keywords: ["SENSOR_CATEGORY_LIGHT Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_LIGHT
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_LIGHT


The SENSOR\_CATEGORY\_LIGHT category contains sensors that provide information about characteristics of light.

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
<td><p>SENSOR_TYPE_AMBIENT_LIGHT</p></td>
<td><p>Ambient light sensors.</p></td>
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
<td><p>SENSOR_DATA_TYPE_LIGHT_CHROMACITY</p></td>
<td><p><strong>VT_VECTOR</strong>|<strong>VT_UI1</strong></p></td>
<td><p>Chromaticity as a counted array of float values.</p>
<p>Data for vector types is always serialized as VT_UI1 (an array of unsigned, one-byte characters). This data field must contain each value as an IEEE four-byte real value (VT_R4).</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Illuminance level, in lux.</p>
<p></p>
<p>Note that device drivers need to also handle this data field with a type of VT_UI4. (This requirement exists for light sensors manufactured before Windows 8.)</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN</p></td>
<td><p><strong>VT_R4</strong></p></td>
<td><p>Color temperature, in kelvin.</p></td>
</tr>
</tbody>
</table>

 

**Important**   Each platform-defined light data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_LIGHT\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

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

 

 





