---
title: WIA_IPA_FULL_ITEM_NAME
description: The WIA_IPA_FULL_ITEM_NAME property contains the full item name (the item name with path information).
keywords: ["WIA_IPA_FULL_ITEM_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_FULL_ITEM_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
---

# WIA_IPA_FULL_ITEM_NAME

The WIA_IPA_FULL_ITEM_NAME property contains the full item name (the item name with path information).

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The *full item name* is the same as the *bstrFullItemName* parameter of the [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem) service utility function. An application reads the WIA_IPA_FULL_ITEM_NAME property to determine which item it is currently using and where that item is located in the WIA item tree. Each item should have a unique name. Applications commonly use the full item name to search for items in the WIA item tree. The WIA service creates and maintains WIA_IPA_FULL_ITEM_NAME.

An application reads WIA_IPA_FULL_ITEM_NAME to determine the format of the image that it is about to receive. An application writes this property to set the format. WIA_IPA_FULL_ITEM_NAME depends on the [**WIA_IPA_TYMED**](wia-ipa-tymed.md) property. The WIA minidriver creates and maintains WIA_IPA_FULL_ITEM_NAME.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**IWiaMiniDrvTransferCallback::GetNextStream**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvtransfercallback-getnextstream)

[**WIA_IPA_TYMED**](wia-ipa-tymed.md)

[**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem)
