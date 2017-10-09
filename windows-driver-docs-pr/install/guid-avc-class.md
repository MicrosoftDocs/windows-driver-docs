---
title: GUID\_AVC\_CLASS
description: GUID\_AVC\_CLASS
ms.assetid: 1aa323d3-7d68-4c50-af68-01bda3792fec
keywords: ["GUID_AVC_CLASS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_AVC_CLASS
api_location:
- Avc.h
api_type:
- HeaderDef
---

# GUID\_AVC\_CLASS


The GUID\_AVC\_CLASS [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for audio video control (AV/C) devices that are supported by the [AVStream](https://msdn.microsoft.com/library/windows/hardware/ff554240) architecture.

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
<td align="left"><p>GUID_AVC_CLASS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{095780C3-48A1-4570-BD95-46707F78C2DC}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [AV/C client driver](https://msdn.microsoft.com/library/windows/hardware/ff556367) [Avc.sys](https://msdn.microsoft.com/library/windows/hardware/ff568667) registers an instance of GUID\_AVC\_CLASS to represent an external AV/C unit on a 1394 bus.

For information about the device interface class for virtual AV/C devices, see [**GUID\_VIRTUAL\_AVC\_CLASS**](guid-virtual-avc-class.md).

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
<td align="left"><p>Available in Windows Vista, Windows Server 2003, Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Avc.h (include Avc.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_VIRTUAL\_AVC\_CLASS**](guid-virtual-avc-class.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_AVC_CLASS%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





