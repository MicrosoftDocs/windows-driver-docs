---
title: KSCATEGORY\_DATATRANSFORM
description: KSCATEGORY\_DATATRANSFORM
ms.assetid: 2e5ff89a-6ec4-4bdf-b935-675c2a337efb
keywords: ["KSCATEGORY_DATATRANSFORM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_DATATRANSFORM
api_location:
- Ks.h
api_type:
- HeaderDef
---

# KSCATEGORY\_DATATRANSFORM


The KSCATEGORY\_DATATRANSFORM [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that transforms audio data streams.

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
<td align="left"><p>KSCATEGORY_DATATRANSFORM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{2EB07EA0-7E70-11D0-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY\_DATATRANSFORM to indicate to the operating system that the devices support the KSCATEGORY\_DATATRANSFORM functional category.

For an example of how to register this functional category in an INF file, see the *Ddksynth.inf* INF file that is included with the software synthesizer sample in the *src\\audio\\ddksynth* directory of the WDK.

For more information about this functional category, see [Installing Device Interfaces for an Audio Adapter](https://msdn.microsoft.com/library/windows/hardware/ff536813), [**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799), and [Requirements for a GFX Filter Factory](https://msdn.microsoft.com/library/windows/hardware/ff537839).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSCATEGORY_DATATRANSFORM%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




