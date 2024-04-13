---
title: WIA_DPS_SHEET_FEEDER_REGISTRATION
description: The WIA_DPS_SHEET_FEEDER_REGISTRATION property contains the registration, or alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_SHEET_FEEDER_REGISTRATION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_SHEET_FEEDER_REGISTRATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_SHEET_FEEDER_REGISTRATION

The WIA_DPS_SHEET_FEEDER_REGISTRATION property contains the registration, or alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA_DPS_SHEET_FEEDER_REGISTRATION property indicates how a document is horizontally positioned on the scanning head of a handheld or sheet-fed scanner. The scanner uses the property to predict where a user places a document on the scanning head.

The following table describes the constants that are valid with WIA_DPS_SHEET_FEEDER_REGISTRATION.

| Constant | Description |
|--|--|
| LEFT_JUSTIFIED | The document is positioned to the left with respect to the scanning head. |
| CENTERED | The document is centered on the scanning head. |
| RIGHT_JUSTIFIED | The document is positioned to the right with respect to the scanning head. |

For scanners that support more than one scanning head, the WIA_DPS_SHEET_FEEDER_REGISTRATION property is relative to the topmost scanning head. This property is required for sheet-fed, scroll-fed, and handheld scanners.

## Requirements

**Version:** Obsolete, use the WIA_IPS_SHEET_FEEDER_REGISTRATION property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_SHEET_FEEDER_REGISTRATION**](wia-ips-sheet-feeder-registration.md)
