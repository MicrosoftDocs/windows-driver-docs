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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_ITEM_SIZE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




