---
title: WIA_IPS_PATCH_CODE_READER
description: The WIA_IPS_PATCH_CODE_READER property is used to enable patch code detection. This property is required for all Patch code Reader items.
keywords: ["WIA_IPS_PATCH_CODE_READER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PATCH_CODE_READER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PATCH_CODE_READER

The **WIA_IPS_PATCH_CODE_READER** property is used to enable patch code detection. This property is required for all Patch code Reader items.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the required values for the **WIA_IPS_PATCH_CODE_READER** property.

| Value | Definition |
|--|--|
| WIA_PATCH_CODE_READER_DISABLED | Patch code detection is disabled. This is the required default value. |
| WIA_PATCH_CODE_READER_AUTO | Patch code detection is enabled. The patch code reader location is automatically selected by the device at runtime depending on the active scan input source. |

The [**WIA_IPA_FORMAT**](wia-ipa-format.md) property is also required for all Patch Code Reader items.

The following table describes the required values for the [**WIA_IPA_FORMAT**](wia-ipa-format.md) property when it is implemented on a Patch Code Reader item.

| Value | Definition |
|--|--|
| WiaImgFmt_XmlPat | Patch code metadata is transferred as an XML file whose content is compliant with the WIA Patch Code Metadata Schema. |
| WiaImgFmt_RawPat | Patch code metadata is transferred as a WIA Patch Code Metadata Raw Format file. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
