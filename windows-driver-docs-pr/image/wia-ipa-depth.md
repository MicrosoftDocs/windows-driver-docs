---
title: WIA_IPA_DEPTH
description: The WIA_IPA_DEPTH property contains the bit depth setting of an image. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_DEPTH Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_DEPTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
---

# WIA_IPA_DEPTH

The WIA_IPA_DEPTH property contains the bit depth setting of an image. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application reads the WIA_IPA_DEPTH property to determine the bit depth setting of an image. An application may also set this property to the desired bit depth, or to the WIA_DEPTH_AUTO value.

If you can set the device to only a single value, create a WIA_PROP_LIST type and place the valid value in it.

The WIA_DEPTH_AUTO value (defined as 0 bits per pixel) is valid for all programmable image data source items, including the Flatbed and Feeder. When this value is supported by the WIA mini-driver the WIA application client can set **WIA_IPA_DEPTH** to this value in order to enable automatic color detection at the device.

When the **WIA_IPA_DEPTH** property is set to WIA_DEPTH_AUTO, the WIA mini-driver must update the [**WIA_IPA_DATATYPE**](wia-ipa-datatype.md) property on the same item to WIA_DATA_AUTO (which must be a supported value if the device supports automatic color). When the **WIA_IPA_DATATYPE** value WIA_DATA_AUTO is supported, the **WIA_IPA_DEPTH** value WIA_DEPTH_AUTO is no longer optional and becomes a required value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
