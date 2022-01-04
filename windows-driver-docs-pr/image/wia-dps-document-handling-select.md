---
title: WIA_DPS_DOCUMENT_HANDLING_SELECT
description: The WIA_DPS_DOCUMENT_HANDLING_SELECT property contains the current scanner acquisition source and mode.
keywords: ["WIA_DPS_DOCUMENT_HANDLING_SELECT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DOCUMENT_HANDLING_SELECT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_DOCUMENT_HANDLING_SELECT

The WIA_DPS_DOCUMENT_HANDLING_SELECT property contains the current scanner acquisition source and mode.

Property Type: VT_I4

Valid Values: WIA_PROP_FLAG

Access Rights: Read/write

## Remarks

An application reads the WIA_DPS_DOCUMENT_HANDLING_SELECT property to determine the current acquisition source of a scanner, or an application write this property to set the source and mode of the scanner. In addition, applications use this property to enable and disable duplexer functionality. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with WIA_DPS_DOCUMENT_HANDLING_SELECT.

| Value | Definition |
|--|--|
| BACK_FIRST | Scan the back of the document first. This value is valid only when DUPLEX is set. |
| BACK_ONLY | Scan the back *only*. This value is valid only when DUPLEX is set. |
| DUPLEX | Scan by using duplexer operations. |
| FRONT_FIRST | Scan the front of the document first. This value is valid only when DUPLEX is set. |
| FRONT_ONLY | Scan the front *only*. |

The values DUPLEX and FRONT_ONLY are mutually exclusive--set one or the other, but not both.

The following table describes the constants that are valid with this property with Microsoft Windows XP but are obsolete with Windows Vista and later.

| Value | Definition |
|--|--|
| AUTO_ADVANCE | Enable automatic feeding of the next document after a scan. |
| FEEDER | Scan by using the document feeder. |
| FLATBED | Scan by using the flatbed. |
| NEXT_PAGE | Scan the next page of the document. |
| PREFEED | Enable pre-feed mode. Preposition the next document while scanning. |

## Requirements

**Version:** Obsolete, use the [**WIA_IPS_DOCUMENT_HANDLING_SELECT**](wia-ips-document-handling-select.md) property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_DOCUMENT_HANDLING_SELECT**](wia-ips-document-handling-select.md)
