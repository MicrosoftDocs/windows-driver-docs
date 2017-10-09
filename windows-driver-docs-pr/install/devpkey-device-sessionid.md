---
title: DEVPKEY\_Device\_SessionId
description: DEVPKEY\_Device\_SessionId
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
---

# DEVPKEY\_Device\_SessionId


The DEVPKEY\_Device\_SessionId device property represents a value that indicates the Terminal Services sessions that a device instance can be accessed in.

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
<td align="left"><p>[<strong>DEVPROP_TYPE_UINT32</strong>](devprop-type-uint32.md)</p></td>
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

The Terminal Server feature supports Plug and Play (PnP) device redirection. Device redirection determines whether a device can be accessed by applications and services within all Terminal Services sessions or whether a device can be accessed only within a particular Terminal Services session. The accessibility of a device within a Terminal Services session is determined by the setting of DEVPKEY\_Device\_SessionId for a device, as follows:

-   If the DEVPKEY\_Device\_SessionId property does not exist, or the property exists, but the value of the property is not set, the device can be accessed in all active Terminal Services sessions.

-   If the DEVPKEY\_Device\_SessionId property exists and the value of the property is set to a nonzero Terminal Services l session identifier, the device can be accessed only in the Terminal Services session indicated by the Terminal Services session identifier.

-   If the DEVPKEY\_Device\_SessionId property exists and the value of the property is set to zero, the device can be accessed only by services. Session zero is a special session in which only services can run.

You can access the DEVPKEY\_Device\_SessionId property by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Device_SessionId%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





