---
title: WIA_IPS_DOCUMENT_HANDLING_SELECT
description: The WIA_IPS_DOCUMENT_HANDLING_SELECT property contains the current scanner acquisition source and mode.
keywords: ["WIA_IPS_DOCUMENT_HANDLING_SELECT Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_DOCUMENT_HANDLING_SELECT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_DOCUMENT_HANDLING_SELECT

> [!IMPORTANT]
> Some information contained in this article applies to obsolete Windows operating systems.

The WIA_IPS_DOCUMENT_HANDLING_SELECT property contains the current scanner acquisition source and mode.

Property Type: VT_I4

Valid Values: WIA_PROP_FLAG

Access Rights: Read/write

## Remarks

An application reads the WIA_IPS_DOCUMENT_HANDLING_SELECT property to determine the current acquisition source of a scanner, or the application writes this property to set the source and mode of the scanner. In addition, applications use this property to enable and disable duplexer functionality. The WIA minidriver creates and maintains this property.

The following table describes a constant that is valid with Windows Vista and later only.

| Value | Definition |
|--|--|
| ADVANCED_DUPLEX | Scan by using individual configuration settings for each child feeder item (WIA_CATEGORY_FEEDER_FRONT and WIA_CATEGORY_FEEDER_BACK). This flag cannot be set together with DUPLEX.<br><br>A device that supports different scan settings for the front and back items should implement the optional ADF front and back items and it should support both DUPLEX and ADVANCED_DUPLEX. |

The following table describes the constants that are valid with Windows Vista and Windows XP.

| Value | Definition |
|--|--|
| BACK_FIRST | Scan the back of the document first. This value is valid only when DUPLEX is set. |
| BACK_ONLY | Scan the back *only*. This value is valid only when DUPLEX is set. |
| DUPLEX | Scan by using duplexer operations. |
| FRONT_FIRST | Scan the front of the document first. This value is valid only when DUPLEX is set. |
| FRONT_ONLY | Scan the front *only*. |

The values DUPLEX and FRONT_ONLY are mutually exclusive--set one or the other, but not both.

A WIA 2.0 minidriver must set the initial value of this property to its default value, FRONT_ONLY. Failure to observe this requirement might make the minidriver incompatible with the WIA 1.0 common scan dialog and with some WIA 1.0 applications.

The following table describes the constants that are valid with Windows XP but are obsolete with Windows Vista and later.

| Value | Definition |
|--|--|
| AUTO_ADVANCE | Enable automatic feeding of the next document after a scan. |
| FEEDER | Scan by using the document feeder. |
| FLATBED | Scan by using the flatbed. |
| NEXT_PAGE | Scan the next page of the document. |
| PREFEED | Enable pre-feed mode. Position the next document while scanning. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_DOCUMENT_HANDLING_SELECT**](wia-dps-document-handling-select.md)
