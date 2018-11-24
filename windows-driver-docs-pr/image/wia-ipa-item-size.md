---
title: WIA\_IPA\_ITEM\_SIZE
description: The WIA\_IPA\_ITEM\_SIZE property contains the current size, in bytes, of the data that is associated with a WIA item. The WIA minidriver creates and maintains this property.
ms.assetid: af019c00-715b-43d1-ba14-f20c01871f35
keywords: ["WIA_IPA_ITEM_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ITEM_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_ITEM\_SIZE


The WIA\_IPA\_ITEM\_SIZE property contains the current size, in bytes, of the data that is associated with a WIA item. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_item_size_si"></span><span id="DDK_WIA_IPA_ITEM_SIZE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value that the WIA\_IPA\_ITEM\_SIZE property contains is the total size of the data that is being transferred. If this value is zero, the WIA minidriver has no information about the exact size of the data. (This situation is common for compressed data.)

An application reads WIA\_IPA\_ITEM\_SIZE to determine the size of the data before it is transferred. The WIA service reads this property to assist in allocating memory for data transfers. For more information about data transfers, see [Transferring Data to a WIA Application](https://msdn.microsoft.com/library/windows/hardware/ff548473).

If WIA\_IPA\_ITEM\_SIZE is set to zero and TYMED is configured for a file transfer, the WIA service does not allocate any memory for the WIA minidriver.

**Note**   In Windows Vista and later versions of the operating system only set the WIA\_IPA\_ITEM\_SIZE property to 0 for the ADF item when automatic document size detection is enabled.

 

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

 

 





