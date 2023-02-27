---
title: WIA_IPS_THRESHOLD
description: The WIA_IPS_THRESHOLD property contains the current hardware threshold setting for a device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_THRESHOLD Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_THRESHOLD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPS_THRESHOLD

The WIA_IPS_THRESHOLD property contains the current hardware threshold setting for a device. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

You should map values for the WIA_IPS_THRESHOLD property in a range from 0 through 255. The default value is 128.

An application sets WIA_IPS_THRESHOLD to change the hardware threshold value. This value is valid only if the [**WIA_IPA_DATATYPE**](wia-ipa-datatype.md) property is equal to WIA_DATA_THRESHOLD. If a device does not allow WIA_DATA_THRESHOLD to be changed, it should report the default value of 128.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_DATATYPE**](wia-ipa-datatype.md)
