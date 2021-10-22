---
title: WIA_IPA_ITEM_NAME
description: The WIA_IPA_ITEM_NAME property contains a WIA item name.
keywords: ["WIA_IPA_ITEM_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ITEM_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPA_ITEM_NAME

The WIA_IPA_ITEM_NAME property contains a WIA item name.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The *item name* is the same as the item name that is specified in a call to the [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem) service utility function.

An application reads the WIA_IPA_ITEM_NAME property to determine which item it is currently using. Each item must have a unique name. The WIA service creates and maintains WIA_IPA_ITEM_NAME.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**IWiaMiniDrvTransferCallback::GetNextStream**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvtransfercallback-getnextstream)

[**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem)
