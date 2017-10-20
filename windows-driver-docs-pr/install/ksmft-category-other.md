---
title: KSMFT_CATEGORY_OTHER
description: KSMFT_CATEGORY_OTHER
ms.assetid: db50ab63-9c6d-4345-8b1c-377a2645dde3
keywords: ["KSMFT_CATEGORY_OTHER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSMFT_CATEGORY_OTHER
api_location:
- Ks.h
api_type:
- HeaderDef
---

# KSMFT_CATEGORY_OTHER


The KSMFT_CATEGORY_OTHER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [Kernel Streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842) (KS) functional category for a device that does not belong in other KS functional categories.

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
<td align="left"><p>KSMFT_CATEGORY_OTHER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{90175d57-b7ea-4901-aeb3-933a8747756f}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

AVStream drivers that have MFT codec support register instances of this device interface class to indicate to the operating system that the devices support the KSMFT_CATEGORY_OTHER functional category.

For more information about device interface classes for AVStream devices with hardware codec support, see [Getting Started with Hardware Codec Support in AVStream](https://msdn.microsoft.com/library/windows/hardware/gg299325).

For more information about how to register this functional category in an INF file, see the *Hiddigi.inf* file, which is included with the *src\\input\\hiddigi* sample drivers in the WDK.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSMFT_CATEGORY_OTHER%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




