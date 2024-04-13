---
title: WIA_IPS_SUPPORTED_BARCODE_TYPES
description: The WIA_IPS_SUPPORTED_BARCODE_TYPES property is used by the WIA minidriver to list all barcode types supported (understood) by the Barcode Reader.
keywords: ["WIA_IPS_SUPPORTED_BARCODE_TYPES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_SUPPORTED_BARCODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_SUPPORTED_BARCODE_TYPES

The **WIA_IPS_SUPPORTED_BARCODE_TYPES** property is used by the WIA minidriver to list all barcode types supported (understood) by the Barcode Reader. The supported barcode types are reported in a VT_VECTOR array as a single value that contains multiple entries.

Property Type: VT_I4 | VT_VECTOR

Valid Values: WIA_PROP_NONE (single array/vector value)

Access Rights: Read-only

## Remarks

The following table describes the valid values for the **WIA_IPS_SUPPORTED_BARCODE_TYPES** property.

| Value | Definition |
|--|--|
| WIA_BARCODE_UPCA | Universal Product Code UPC-A |
| WIA_BARCODE_UPCE | Universal Product Code UPC-E |
| WIA_BARCODE_CODABAR | Codabar code |
| WIA_BARCODE_NONINTERLEAVED_2OF5 | Two-out-of-five code |
| WIA_BARCODE_INTERLEAVED_2OF5 | Interleaved 2 of 5 code |
| WIA_BARCODE_CODE39 | Code 39 |
| WIA_BARCODE_CODE39_MOD43 | Code 39 mod 43 |
| WIA_BARCODE_CODE39_FULLASCII | Full ASCII Code 39 |
| WIA_BARCODE_CODE93 | Code 93 |
| WIA_BARCODE_CODE128 | Code 128 |
| WIA_BARCODE_CODE128A | Code 128A |
| WIA_BARCODE_CODE128B | Code 128B |
| WIA_BARCODE_CODE128C | Code 128C |
| WIA_BARCODE_GS1128 | GS1-128 (formerly known as UCC/EAN-128) |
| WIA_BARCODE_GS1DATABAR WIA_BARCODE_ITF14 | GS1 DataBar code |
| WIA_BARCODE_ITF14 | ITF-14 code |
| WIA_BARCODE_EAN8 | EAN-8 code |
| WIA_BARCODE_EAN13 | EAN-13 code |
| WIA_BARCODE_POSTNETA | POSTNET (Postal Numeric Encoding Technique) "A" code |
| WIA_BARCODE_POSTNETB | POSTNET (Postal Numeric Encoding Technique) "B" code |
| WIA_BARCODE_POSTNETC | POSTNET (Postal Numeric Encoding Technique) "C" code |
| WIA_BARCODE_POSTNET_DPBC | POSTNET (Postal Numeric Encoding Technique) DPBC (Delivery Point Bar Code) code |
| WIA_BARCODE_PLANET | Postal Alpha Numeric Encoding Technique (PLANET) code |
| WIA_BARCODE_INTELLIGENT_MAIL | Intelligent Mail Barcode (replaces POSTNET and PLANET barcodes) |
| WIA_BARCODE_POSTBAR | PostBar (also known as CPC 4-State) |
| WIA_BARCODE_RM4SCC | RM4SCC barcode |
| WIA_BARCODE_HIGH_CAPACITY_COLOR | Microsoft High Capacity Color Barcode (HCCB) |
| WIA_BARCODE_MAXICODE | MaxiCode |
| WIA_BARCODE_PDF417 | PDF417 |
| WIA_BARCODE_CPCBINARY | CPC Binary Barcode (Canada Post) |
| WIA_BARCODE_FIM | Face Identification Mark (FIM) barcode (USPS) |
| WIA_BARCODE_PHARMACODE | Pharmaceutical Binary Code (Pharmacode) |
| WIA_BARCODE_PLESSEY | Plessey Code |
| WIA_BARCODE_MSI | MSI (Modified Plessey) code |
| WIA_BARCODE_JAN | Japanese Article Number (JAN) code |
| WIA_BARCODE_TELEPEN | Telepen code |
| WIA_BARCODE_AZTEC | Aztec Code |
| WIA_BARCODE_SMALLAZTEC | Small Aztec Code |
| WIA_BARCODE_DATAMATRIX | Data Matrix code |
| WIA_BARCODE_DATASTRIP | Datastrip code (Cauzin Softstrip) |
| WIA_BARCODE_EZCODE | Ezcode |
| WIA_BARCODE_QRCODE | QR Code |
| WIA_BARCODE_SHOTCODE | ShotCode |
| WIA_BARCODE_SPARQCODE | SPARQCode |
| WIA_BARCODE_CUSTOM_BASE + N | WIA_BARCODE_CUSTOM_BASE is the offset to all custom barcode values that the WIA minidriver may add. N is a positive integer. |

The WIA minidriver can extend this list with additional custom values defined as WIA_BARCODE_CUSTOM_BASE + N, where N is a positive integer.

This property is required for all Barcode Reader items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
