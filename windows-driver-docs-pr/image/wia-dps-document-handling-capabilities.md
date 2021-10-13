---
title: WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES
description: The WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES property contains the capabilities of a scanner.
keywords: ["WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES

The WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES property contains the capabilities of a scanner.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES property to determine whether a scanner has a flatbed, document feeder, or duplexer installed. You can also use this property to further define the installed features. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with Windows 8 only.

| Value | Definition |
|--|--|
| IMPRINTER | Imprinter |
| ENDORSER | Endorser |
| BARCODE_READER | Barcode Reader |
| PATCH_CODE_READER | Patch Code Reader |
| MICR_READER | MICR Reader |

The following table describes the constants that are valid with Windows 7 only.

| Value | Definition |
|--|--|
| AUTO_SOURCE | The device supports [auto-configured scanning](auto-configured-scanning.md). |

The following table describes the constants that are valid with Windows 7 and Windows Vista.

| Value | Definition |
|--|--|
| ADVANCED_DUP | The device supports advanced duplex scan configuration, independently on each document size. |
| DETECT_FILM_TPA | The scanner can detect when the transparency or film scanning adapter is ready to scan. |
| DETECT_STOR | The scanner can detect when there is a document in the internal storage. |
| FILM_TPA | The scanner has a transparency or film scanning adapter. |
| STOR | The scanner is equipped with an internal storage device. |

The following table describes the constants that are valid with Windows 7, Windows Vista, and Windows XP.

| Value | Definition |
|--|--|
| DETECT_FEED | The scanner can detect a document in the feeder. |
| DETECT_FLAT | The scanner can detect a document on the flatbed platen. |
| DETECT_SCAN | The scanner can detect a document in the feeder only by scanning. |
| DUP | The scanner has a duplexer. |
| FEED | The scanner has a document feeder installed. |
| FLAT | The scanner has a flatbed platen. |

The following table describes the constants that are obsolete and should not be used.

| Value | Definition |
|--|--|
| DETECT_DUP | The scanner can detect a duplex scan request from a user. |
| DETECT_DUP_AVAIL | The scanner can detect when a duplexer is installed. |
| DETECT_FEED_AVAIL | The scanner can detect when a document feeder is installed. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
