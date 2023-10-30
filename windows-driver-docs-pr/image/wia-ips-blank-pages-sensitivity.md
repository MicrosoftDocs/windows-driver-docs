---
title: WIA_IPS_BLANK_PAGES_SENSITIVITY
description: The WIA_IPS_BLANK_PAGES_SENSITIVITY property is used to change the blank page detection trigger to a lower or higher value between the lowest and highest sensitivity supported by the device.
keywords: ["WIA_IPS_BLANK_PAGES_SENSITIVITY Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_BLANK_PAGES_SENSITIVITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/17/2019
---

# WIA\_IPS\_BLANK\_PAGES\_SENSITIVITY

The **WIA\_IPS\_BLANK\_PAGES\_SENSITIVITY** property is used to change the blank page detection trigger to a lower or higher value between the lowest and highest sensitivity supported by the device.

The WIA mini-driver can internally use separate sensitivity values for each [**WIA\_IPA\_DATA\_TYPE**](./wia-ipa-datatype.md) and [**WIA\_IPA\_DEPTH**](./wia-ipa-depth.md) supported color mode combination.

This property is initialized and maintained by the WIA mini-driver.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read-Write

## Remarks

This property is optional and is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER), only when [**WIA\_IPS\_BLANK\_PAGES**](./wia-ips-blank-pages.md) is supported with at least one another value than **WIA\_BLANK\_PAGES\_DETECTION\_DISABLED**.

## Requirements

| &nbsp; | &nbsp; |
| --- |:--- |
| **Header** | Wiadef.h (include Wiadef.h) |
