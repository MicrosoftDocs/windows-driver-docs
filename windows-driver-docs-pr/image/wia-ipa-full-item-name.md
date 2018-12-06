---
title: WIA\_IPA\_FULL\_ITEM\_NAME
description: The WIA\_IPA\_FULL\_ITEM\_NAME property contains the full item name (the item name with path information).
ms.assetid: ba034507-264a-4960-80ab-d5cb0daa5c1a
keywords: ["WIA_IPA_FULL_ITEM_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_FULL_ITEM_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_FULL\_ITEM\_NAME


The WIA\_IPA\_FULL\_ITEM\_NAME property contains the full item name (the item name with path information).

## <span id="ddk_wia_ipa_full_item_name_si"></span><span id="DDK_WIA_IPA_FULL_ITEM_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The *full item name* is the same as the *bstrFullItemName* parameter of the [**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160) service utility function. An application reads the WIA\_IPA\_FULL\_ITEM\_NAME property to determine which item it is currently using and where that item is located in the WIA item tree. Each item should have a unique name. Applications commonly use the full item name to search for items in the WIA item tree. The WIA service creates and maintains WIA\_IPA\_FULL\_ITEM\_NAME.

An application reads WIA\_IPA\_FULL\_ITEM\_NAME to determine the format of the image that it is about to receive. An application writes this property to set the format. WIA\_IPA\_FULL\_ITEM\_NAME depends on the [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md) property. The WIA minidriver creates and maintains WIA\_IPA\_FULL\_ITEM\_NAME.

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

## See also


[**IWiaMiniDrvTransferCallback::GetNextStream**](https://msdn.microsoft.com/library/windows/hardware/jj151551)

[**WIA\_IPA\_TYMED**](wia-ipa-tymed.md)

[**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160)

 

 






