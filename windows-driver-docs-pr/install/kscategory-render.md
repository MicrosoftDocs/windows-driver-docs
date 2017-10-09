---
title: KSCATEGORY\_RENDER
description: KSCATEGORY\_RENDER
ms.assetid: 467e3192-46c4-4ef4-88cf-0a870efc1725
keywords: ["KSCATEGORY_RENDER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_RENDER
api_location:
- Ks.h
api_type:
- HeaderDef
---

# KSCATEGORY\_RENDER


The KSCATEGORY\_RENDER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that renders wave and MIDI data streams.

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
<td align="left"><p>KSCATEGORY_RENDER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{65E8773E-8F56-11D0-A3B9-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS audio adapter devices register an instance of KSCATEGORY\_RENDER to indicate that the devices support the KSCATEGORY\_RENDER functional category.

For information about how to register this functional category in an INF file, see the INF file *Ac97smpl.inf* that is included with the [AC'97 sample driver](http://go.microsoft.com/fwlink/p/?linkid=256075) in the WDK.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](https://msdn.microsoft.com/library/windows/hardware/ff536813) and [**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799).

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
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSCATEGORY_RENDER%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




