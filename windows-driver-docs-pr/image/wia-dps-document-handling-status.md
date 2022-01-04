---
title: WIA_DPS_DOCUMENT_HANDLING_STATUS
description: The WIA_DPS_DOCUMENT_HANDLING_STATUS property contains the current state of a scanner's installed flatbed, document feeder, or duplexer.
keywords: ["WIA_DPS_DOCUMENT_HANDLING_STATUS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DOCUMENT_HANDLING_STATUS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_DOCUMENT_HANDLING_STATUS

The WIA_DPS_DOCUMENT_HANDLING_STATUS property contains the current state of a scanner's installed flatbed, document feeder, or duplexer.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DPS_DOCUMENT_HANDLING_STATUS property to determine whether a scanner device is ready to use. Reading this property is an ideal way to check whether paper is in the feeder before a user acquires an image. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with Windows 8 and later versions of Windows.

| Value | Definition |
|--|--|
| IMPRINTER_READY | The imprinter capabilities of an imprinter/endorser are enabled and ready for use. |
| ENDORSER_READY | The endorser capabilities of an imprinter/endorser are enabled and ready for use. |
| BARCODE_READER_READY | The barcode reader is enabled and ready for use. |
| PATCH_CODE_READER_READY | The patch code reader is enabled and ready for use. |
| MICR_READER_READY | The MICR reader is enabled and ready for use. |

The following table describes the constants that are valid with both Windows Vista and Windows XP.

| Value | Definition |
|--|--|
| DUP_READY | The duplexer is enabled and ready to use. |
| FEED_READY | The document feeder has a page loaded and is ready for use. |
| FLAT_COVER_UP | The flatbed cover is up. |
| FLAT_READY | The flatbed is ready for use. |
| PAPER_JAM | A document is stuck in the document feeder. |
| PATH_COVER_UP | The paper path is covered and is preventing proper operation. |

The following table describes the constants that are valid with Windows Vista only.

| Value | Definition |
|--|--|
| FILM_TPA_READY | A transparency adapter is installed and ready for use. |
| STORAGE_READY | A storage device is installed and ready for use. |
| STORAGE_FULL | The storage is full; no upload operations are possible. |
| MULTIPLE_FEED | A multiple feed occurred; this type of feed usually occurs with a PAPER_JAM value. |
| DEVICE_ATTENTION | There is an error that requires user intervention on the scanner. |
| LAMP_ERR | The scanner has a problem with the lamp and is not ready. |

> [!NOTE]
> There are no custom-defined base definitions. You cannot create custom extensions for status flag values. If you need custom status reporting, you should define a custom property.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
