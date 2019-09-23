---
title: WIA\_IPA\_ITEM\_NAME
description: The WIA\_IPA\_ITEM\_NAME property contains a WIA item name.
ms.assetid: becdd9c6-8202-4c0e-a530-043c1b8421fa
keywords: ["WIA_IPA_ITEM_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ITEM_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_ITEM\_NAME


The WIA\_IPA\_ITEM\_NAME property contains a WIA item name.

## <span id="ddk_wia_ipa_item_name_si"></span><span id="DDK_WIA_IPA_ITEM_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The *item name* is the same as the item name that is specified in a call to the [**wiasCreateDrvItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamdef/nf-wiamdef-wiascreatedrvitem) service utility function.

An application reads the WIA\_IPA\_ITEM\_NAME property to determine which item it is currently using. Each item must have a unique name. The WIA service creates and maintains WIA\_IPA\_ITEM\_NAME.

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


[**IWiaMiniDrvTransferCallback::GetNextStream**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvtransfercallback-getnextstream)

[**wiasCreateDrvItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamdef/nf-wiamdef-wiascreatedrvitem)

 

 






