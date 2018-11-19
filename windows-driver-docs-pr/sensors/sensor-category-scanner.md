---
title: SENSOR\_CATEGORY\_SCANNER
description: The SENSOR\_CATEGORY\_SCANNER category contains sensors that provide information that is obtained by scanning.
ms.assetid: ba7a44d0-1d89-4a6c-b046-c7cd02c457b3
keywords: ["SENSOR_CATEGORY_SCANNER Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_SCANNER
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_SCANNER


The SENSOR\_CATEGORY\_SCANNER category contains sensors that provide information that is obtained by scanning.

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
<td><p>SENSOR_TYPE_BARCODE_SCANNER</p></td>
<td><p>Sensors that use optical scanning to read bar codes.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_TYPE_RFID_SCANNER</p></td>
<td><p>Radio-frequency ID scanning sensors.</p></td>
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
<td><p>SENSOR_DATA_TYPE_RFID_TAG_40_BIT</p></td>
<td><p><strong>VT_UI8</strong></p></td>
<td><p>40-bit radio frequency ID tag value.</p></td>
</tr>
</tbody>
</table>

 

**Important**   Each platform-defined scanner data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_SCANNER\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

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

 

 





