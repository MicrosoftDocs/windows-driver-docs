---
title: GUID_DEVINTERFACE_CDCHANGER
description: GUID_DEVINTERFACE_CDCHANGER
ms.assetid: 9bcbe3d5-2057-44cb-a495-6edee14a9cbb
keywords: ["GUID_DEVINTERFACE_CDCHANGER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_CDCHANGER
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# GUID_DEVINTERFACE_CDCHANGER


The GUID_DEVINTERFACE_CDCHANGER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for CD-ROM changer devices.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVINTERFACE_CDCHANGER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56312-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied CD-ROM [changer driver](https://msdn.microsoft.com/library/windows/hardware/ff551455) registers instances of GUID_DEVINTERFACE_CDCHANGER to notify the operating system and applications of the presence of CD-ROM changer devices.

For information about the device interface class for CD-ROM devices, see [**GUID_DEVINTERFACE_CDROM**](guid-devinterface-cdrom.md).

For information about storage devices, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

[**CdChangerClassGuid**](cdchangerclassguid.md) is an obsolete identifier for the GUID_DEVINTERFACE_CDCHANGER device interface class; for new instances of this class, use GUID_DEVINTERFACE_CDCHANGER instead.

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
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**CdChangerClassGuid**](cdchangerclassguid.md)

[**GUID_DEVINTERFACE_CDROM**](guid-devinterface-cdrom.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_CDCHANGER%20%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





