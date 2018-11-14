---
title: DEVPKEY_Numa_Proximity_Domain
description: DEVPKEY_Numa_Proximity_Domain
ms.assetid: 384e167b-cb08-4264-a7b1-3cea2dda0d46
keywords: ["DEVPKEY_Numa_Proximity_Domain Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Numa_Proximity_Domain
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Numa_Proximity_Domain


The DEVPKEY_Numa_Proximity_Domain device property represents the proximity domain of a Non-Uniform Memory Architecture (NUMA).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Numa_Proximity_Domain</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers; read and write access by a device driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value DEVPKEY_Numa_Proximity_Domain is a numeric value that represents a domain ID.

Typically, the operating system sets the value of DEVPKEY_Numa_Proximity_Domain by retrieving the corresponding information from system firmware.

You can retrieve the value of DEVPKEY_Numa_Proximity_Domain by calling **IoSetDevicePropertyData** or **IoGetDevicePropertyData** in a device driver.

You can also call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Numa_Proximity_Domain.

The value of this property is owned by Windows and should be treated as read-only by drivers and applications.

Windows Server 2003, Windows XP, and Windows 2000 do not support this property.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting with Windows Vista.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

 

 





