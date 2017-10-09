---
title: KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION
description: KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION
ms.assetid: 0af3159c-8c44-4c42-8141-944bb734623c
keywords: ["KSCATEGORY_BDA_TRANSPORT_INFORMATION Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_BDA_TRANSPORT_INFORMATION
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION


The KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for a transport information filter (TIF) in the [broadcast driver architecture](https://msdn.microsoft.com/library/windows/hardware/ff556573) (BDA).

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
<td align="left"><p>KSCATEGORY_BDA_TRANSPORT_INFORMATION</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{A2E3074F-6C3D-11d3-B653-00C04F79498E}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for BDA devices register instances of KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION to indicate to the operating system that the devices support a BDA transport information filter.

For more information about the KS functional category for BDA transport information filters, see [BDA Filter Category GUIDs](https://msdn.microsoft.com/library/windows/hardware/ff556521).

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
<td align="left"><p>Available in Windows XP, Windows 2000 with DirectX 9.0A installed, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSCATEGORY_BDA_TRANSPORT_INFORMATION%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




