---
title: WIA\_IPA\_ACCESS\_RIGHTS
description: The WIA\_IPA\_ACCESS\_RIGHTS property contains the access rights for a WIA item.
MS-HAID:
- 'WIA\_PropTable\_d67cce83-68e8-4904-82ac-d2d9ebda1b34.xml'
- 'image.wia\_ipa\_access\_rights'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5bfa9406-2cb6-4c8b-ab25-6f8f55d941d4
keywords: ["WIA_IPA_ACCESS_RIGHTS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ACCESS_RIGHTS
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPA\_ACCESS\_RIGHTS


The WIA\_IPA\_ACCESS\_RIGHTS property contains the access rights for a WIA item.

## <span id="ddk_wia_ipa_access_rights_si"></span><span id="DDK_WIA_IPA_ACCESS_RIGHTS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_FLAG

Access Rights: Read/write or read-only (depending on the item's ability to have its access rights changed)

Remarks
-------

*Access rights* control the ability of an application to delete items in the WIA item tree. The WIA minidriver creates and maintains the WIA\_IPA\_ACCESS\_RIGHTS property.

The following table describes the constants that are valid with WIA\_IPA\_ACCESS\_RIGHTS.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_ITEM_CAN_BE_DELETED</p></td>
<td><p>This WIA item can be deleted.</p></td>
</tr>
<tr class="even">
<td><p>WIA_ITEM_READ</p></td>
<td><p>Access to the item is read-only.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_ITEM_WRITE</p></td>
<td><p>Access to the item is read/write.</p></td>
</tr>
<tr class="even">
<td><p>WIA_ITEM_RD</p></td>
<td><p>WIA_ITEM_READ | WIA_ITEM_CAN_BE_DELETED</p></td>
</tr>
<tr class="odd">
<td><p>WIA_ITEM_RWD</p></td>
<td><p>WIA_ITEM_READ | WIA_ITEM_WRITE | WIA_ITEM_CAN_BE_DELETED</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_ACCESS_RIGHTS%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




