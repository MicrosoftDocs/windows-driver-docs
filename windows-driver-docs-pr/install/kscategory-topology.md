---
title: KSCATEGORY\_TOPOLOGY
description: KSCATEGORY\_TOPOLOGY
ms.assetid: 20c4ccf1-81bb-4209-9842-4de295fe3a00
keywords: ["KSCATEGORY_TOPOLOGY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_TOPOLOGY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSCATEGORY\_TOPOLOGY


The KSCATEGORY\_TOPOLOGY [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for the internal topology of an audio device.

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
<td align="left"><p>KSCATEGORY_TOPOLOGY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{DDA54A40-1E4C-11D1-A050-405705C10000}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS audio adapter devices register instances of KSCATEGORY\_TOPOLOGY to indicate to the operating system that the devices support the KSCATEGORY\_TOPOLOGY functional category.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](https://msdn.microsoft.com/library/windows/hardware/ff536813).

The [AC'97 sample driver](http://go.microsoft.com/fwlink/p/?linkid=256075) that is provided in the WDK enumerates instances of the KSCATEGORY\_TOPOLOGY device interface class.

The sysfx sample in the WDK registers instances of this device interface class. The sysfx sample is located in the *src\\audio\\sysfx directory* of the WDK.

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
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSCATEGORY_TOPOLOGY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




