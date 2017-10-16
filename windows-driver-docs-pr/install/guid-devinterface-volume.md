---
title: GUID_DEVINTERFACE_VOLUME
description: GUID_DEVINTERFACE_VOLUME
ms.assetid: 34802df4-8a8f-48ea-a146-d2ad4ae4709a
keywords: ["GUID_DEVINTERFACE_VOLUME Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_VOLUME
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# GUID_DEVINTERFACE_VOLUME


The GUID_DEVINTERFACE_VOLUME [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for volume devices.

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
<td align="left"><p>GUID_DEVINTERFACE_VOLUME</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F5630D-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [storage class drivers](https://msdn.microsoft.com/library/windows/hardware/ff559215) register instances of GUID_DEVINTERFACE_VOLUME to notify the operating system and applications of the presence of volume devices. The mount manager uses the Plug and Play (PnP) device interface notification mechanism to signal the arrival or removal of a volume interface.

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include an [Addfilter Storage Filter Tool](http://go.microsoft.com/fwlink/p/?linkid=256076) that uses the obsolete identifier [**VolumeClassGuid**](volumeclassguid.md) to enumerate instances of the GUID_DEVINTERFACE_VOLUME device interface class.

For more information about storage drivers, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976) and [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

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


[**VolumeClassGuid**](volumeclassguid.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_VOLUME%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





