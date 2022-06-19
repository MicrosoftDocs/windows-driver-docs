---
title: DEVPKEY_Numa_Proximity_Domain
description: DEVPKEY_Numa_Proximity_Domain
keywords: ["DEVPKEY_Numa_Proximity_Domain Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Numa_Proximity_Domain
api_location:
- Devpkey.h
api_type:
- HeaderDef
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

 

## Remarks

The value DEVPKEY_Numa_Proximity_Domain is a numeric value that represents a domain ID.

Typically, the operating system sets the value of DEVPKEY_Numa_Proximity_Domain by retrieving the corresponding information from system firmware.

You can retrieve the value of DEVPKEY_Numa_Proximity_Domain by calling **IoGetDevicePropertyData** in a device driver.

You can also call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Numa_Proximity_Domain.

The value of this property is owned by Windows and should be treated as read-only by drivers and applications.

Windows Server 2003, Windows XP, and Windows 2000 do not support this property.

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)
