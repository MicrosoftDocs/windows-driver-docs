---
title: GUID\_DEVINTERFACE\_DISK
description: GUID\_DEVINTERFACE\_DISK
ms.assetid: 47782789-4504-4705-8c32-4d2bc508a7e2
keywords: ["GUID_DEVINTERFACE_DISK Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_DISK
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# GUID\_DEVINTERFACE\_DISK


The GUID\_DEVINTERFACE\_DISK [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for hard disk [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969).

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
<td align="left"><p>GUID_DEVINTERFACE_DISK</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56307-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied storage class drivers register an instance of GUID\_DEVINTERFACE\_DISK for a hard disk storage device.

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include the [disk class driver](http://go.microsoft.com/fwlink/p/?linkid=256103) sample and the [Addfilter Storage Filter Tool](http://go.microsoft.com/fwlink/p/?linkid=256076). The disk class driver sample uses the obsolete identifier [**DiskClassGuid**](diskclassguid.md) to register instances of the GUID\_DEVINTERFACE\_DISK device interface class. The sample Addfilter application uses DiskClassGuid to enumerate instances of GUID\_DEVINTERFACE\_DISK device interface class.

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


[**DiskClassGuid**](diskclassguid.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_DISK%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





