---
title: SENSOR\_CATEGORY\_ALL
description: The SENSOR\_CATEGORY\_ALL category represents the set of all platform-defined sensor categories.
ms.assetid: 9a4524d2-055c-46e0-9650-66e6f2872fbc
keywords: ["SENSOR_CATEGORY_ALL Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_ALL
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

# SENSOR\_CATEGORY\_ALL


The SENSOR\_CATEGORY\_ALL category represents the set of all platform-defined sensor categories.

### <span id="platform_defined_property_keys"></span><span id="PLATFORM_DEFINED_PROPERTY_KEYS"></span>Platform-defined Property Keys

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
<td><p>SENSOR_DATA_TYPE_TIMESTAMP</p></td>
<td><p><strong>VT_FILETIME</strong></p></td>
<td><p>Required for all data reports. Marks each data report with the time the data report was created. Use Universal Coordinated Time (UTC).</p></td>
</tr>
</tbody>
</table>

 

**Important**   Each platform-defined common data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_COMMON\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20SENSOR_CATEGORY_ALL%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




