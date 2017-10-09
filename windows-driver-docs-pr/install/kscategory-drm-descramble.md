---
title: KSCATEGORY\_DRM\_DESCRAMBLE
description: KSCATEGORY\_DRM\_DESCRAMBLE
ms.assetid: 3bb6887f-4fc9-452e-bceb-35fe26844ac5
keywords: ["KSCATEGORY_DRM_DESCRAMBLE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_DRM_DESCRAMBLE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSCATEGORY\_DRM\_DESCRAMBLE


The KSCATEGORY\_DRM\_DESCRAMBLE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that unscrambles a DRM-protected wave stream.

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
<td align="left"><p>KSCATEGORY_DRM_DESCRAMBLE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{FFBB6E3F-CCFE-4D84-90D9-421418B03A8E}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY\_DRM\_DESCRAMBLE to indicate to the operating system that the devices support the KSCATEGORY\_DRM\_DESCRAMBLE functional category.

For more information about this functional category, see [Installing Device Interfaces for an Audio Adapter](https://msdn.microsoft.com/library/windows/hardware/ff536813).

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
<td align="left"><p>Available in Windows Vista, Windows Server 2003, Windows XP, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSCATEGORY_DRM_DESCRAMBLE%20%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




