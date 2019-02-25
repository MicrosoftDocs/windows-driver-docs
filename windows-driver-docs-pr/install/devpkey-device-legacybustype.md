---
title: DEVPKEY_Device_LegacyBusType
description: DEVPKEY_Device_LegacyBusType
ms.assetid: 76c2a472-bb05-4f6a-84da-0ae9e7c1fdf1
keywords: ["DEVPKEY_Device_LegacyBusType Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_LegacyBusType
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_LegacyBusType


The DEVPKEY_Device_LegacyBusType device property represents the legacy bus number of a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_LegacyBusType</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_LEGACYBUSTYPE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Windows sets the value of DEVPKEY_Device_LegacyBusType to the value of the LegacyBusType member of the [**PNP_BUS_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559608) structure that a bus driver returns in response to an [**IRP_MN_QUERY_BUS_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff551654) request. The value of DEVPKEY_Device_LegacyBusType is one of [**INTERFACE_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff547839) enumerator values that are defined in Wdm.h and Ntddk.h.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_LegacyBusType.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_LegacyBusType property key. Instead, you can use the corresponding SPDRP_LEGACYBUSTYPE identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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


[**INTERFACE_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff547839)

[**IRP_MN_QUERY_BUS_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff551654)

[**PNP_BUS_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559608)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






