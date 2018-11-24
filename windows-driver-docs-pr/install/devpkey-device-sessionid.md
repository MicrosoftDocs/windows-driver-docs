---
title: DEVPKEY_Device_SessionId
description: DEVPKEY_Device_SessionId
ms.assetid: 0e5815b3-0427-4f07-9ec1-a21976d5d933
keywords: ["DEVPKEY_Device_SessionId Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SessionId
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_SessionId


The DEVPKEY_Device_SessionId device property represents a value that indicates the Terminal Services sessions that a device instance can be accessed in.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_SessionId</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-uint32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_UINT32&lt;/strong&gt;](devprop-type-uint32.md)"><strong>DEVPROP_TYPE_UINT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by applications and services.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The Terminal Server feature supports Plug and Play (PnP) device redirection. Device redirection determines whether a device can be accessed by applications and services within all Terminal Services sessions or whether a device can be accessed only within a particular Terminal Services session. The accessibility of a device within a Terminal Services session is determined by the setting of DEVPKEY_Device_SessionId for a device, as follows:

-   If the DEVPKEY_Device_SessionId property does not exist, or the property exists, but the value of the property is not set, the device can be accessed in all active Terminal Services sessions.

-   If the DEVPKEY_Device_SessionId property exists and the value of the property is set to a nonzero Terminal Services l session identifier, the device can be accessed only in the Terminal Services session indicated by the Terminal Services session identifier.

-   If the DEVPKEY_Device_SessionId property exists and the value of the property is set to zero, the device can be accessed only by services. Session zero is a special session in which only services can run.

You can access the DEVPKEY_Device_SessionId property by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163).

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
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 






