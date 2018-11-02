---
title: DEVPKEY_Device_LocationInfo
description: DEVPKEY_Device_LocationInfo
ms.assetid: c7eba222-20fe-4868-89e2-9dcef9965cec
keywords: ["DEVPKEY_Device_LocationInfo Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_LocationInfo
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_LocationInfo


The DEVPKEY_Device_LocationInfo device property represents the bus-specific physical location of a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_LocationInfo</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_LOCATION_INFORMATION</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Windows sets the value of DEVPKEY_Device_LocationInfo to the value that the bus driver returns for a device instance in response to an [**IRP_MN_QUERY_DEVICE_TEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551674) IRP.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and **SetupDiGetDeviceProperty** to retrieve and set the value of DEVPKEY_Device_LocationInfo.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_LocationInfo property key. Instead, you can use the corresponding SPDRP_LOCATION_INFORMATION identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**IRP_MN_QUERY_DEVICE_TEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551674)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






