---
title: SENSOR\_CATEGORY\_MECHANICAL
description: The SENSOR\_CATEGORY\_MECHANICAL category contains sensors that provide information related to mechanisms.
ms.assetid: 0ae66a5b-6564-4e2c-a6a1-c88c7e853a38
keywords: ["SENSOR_CATEGORY_MECHANICAL Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_MECHANICAL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_MECHANICAL


The SENSOR\_CATEGORY\_MECHANICAL category contains sensors that provide information related to mechanisms.

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
<td><p>SENSOR_TYPE_BOOLEAN_SWITCH</p></td>
<td><p>Two-state switches (off or on).</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_FORCE</p></td>
<td><p>Force sensors.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_MULTIVALUE_SWITCH</p></td>
<td><p>Multiple-position switches.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_PRESSURE</p></td>
<td><p>Pressure sensors.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_TYPE_SCALE</p></td>
<td><p>Weight sensors.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_STRAIN</p></td>
<td><p>Strain sensors.</p></td>
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
<td><p>SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Absolute pressure, in pascals.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE</p></td>
<td><p><strong>VT_BOOL</strong></p></td>
<td><p>State field for SENSOR_TYPE_BOOLEAN_SWITCH.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_FORCE_NEWTONS</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Force, in newtons.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Relative gauge pressure, in pascals.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>State field for SENSOR_TYPE_MULTIVALUE_SWITCH.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_DATA_TYPE_STRAIN</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Strain.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS</p></td>
<td><p><strong>VT_R8</strong></p></td>
<td><p>Weight, in kilograms.</p></td>
</tr>
</tbody>
</table>

 

**Important**   Each platform-defined mechanical data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_MECHANICAL\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

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

 

 





