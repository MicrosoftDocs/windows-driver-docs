---
title: GUID\_DEVINTERFACE\_FLOPPY
description: GUID\_DEVINTERFACE\_FLOPPY
ms.assetid: 07d47168-a179-40ef-843b-c1efa6acb395
keywords: ["GUID_DEVINTERFACE_FLOPPY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_FLOPPY
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# GUID\_DEVINTERFACE\_FLOPPY


The GUID\_DEVINTERFACE\_FLOPPY [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for floppy disk [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969).

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
<td align="left"><p>GUID_DEVINTERFACE_FLOPPY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56311-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied storage class driver for floppy disk storage devices registers an instance of GUID\_DEVINTERFACE\_FLOPPY for a floppy disk storage device.

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include a [floppy driver](http://go.microsoft.com/fwlink/p/?linkid=256192) sample that uses the obsolete identifier [**FloppyClassGuid**](floppyclassguid.md) to register an instance of the GUID\_DEVINTERFACE\_FLOPPY device interface class.

For information about storage drivers, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**FloppyClassGuid**](floppyclassguid.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_FLOPPY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





