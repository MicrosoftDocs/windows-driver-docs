---
title: WIA_IPS_BARCODE_READER
description: The WIA_IPS_BARCODE_READER property is used by the WIA minidriver to list the available barcode reader location (one/fixed or multiple) and by the application client to select one of these locations and enable barcode detection.
keywords: ["WIA_IPS_BARCODE_READER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_BARCODE_READER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_BARCODE_READER

The **WIA_IPS_BARCODE_READER** property is used by the WIA minidriver to list the available barcode reader location (one/fixed or multiple) and by the application client to select one of these locations and enable barcode detection.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the required values for the **WIA_IPS_BARCODE_READER** property.

| Value | Definition |
|--|--|
| WIA_BARCODE_READER_DISABLED | Barcode detection is disabled. This is the required default value. |
| WIA_BARCODE_READER_AUTO | Barcode detection is enabled. The barcode reader location is automatically selected by the device at run time depending on the active scan input source. |

The following table describes the optional values for the **WIA_IPS_BARCODE_READER** property.

| Value | Definition |
|--|--|
| WIA_BARCODE_READER_FLATBED | Barcode detection is enabled for the documents scanned on the scanner flatbed. |
| WIA_BARCODE_READER_FEEDER_FRONT | Barcode detection is enabled for the front side of the documents scanned on the scanner feeder. |
| WIA_BARCODE_READER_FEEDER_BACK | Barcode detection is enabled for the front side of the documents scanned on the scanner feeder. |
| WIA_BARCODE_READER_FEEDER_DUPLEX | Barcode detection is enabled. The barcode reader location is automatically selected by the device at run time depending on the active scan input source. |

The WIA minidriver is allowed to accept property configuration for the optional values but at scan time ignore requests to enable barcode detection to an inactive scan input source.

This property is required for all Barcode Reader items. The WIA_BARCODE_READER_DISABLED and WIA_BARCODE_READER_AUTO values are required. WIA_BARCODE_READER_DISABLED is the required default value.

The [**WIA_IPA_FORMAT**](wia-ipa-format.md) property is also required for all Barcode Reader items.

The following table describes the required values for the [**WIA_IPA_FORMAT**](wia-ipa-format.md) property when it is implemented on a Barcode Reader item.

| Value | Definition |
|--|--|
| WiaImgFmt_XmlBar | Barcode metadata is transferred as an XML file whose content is compliant with the WIA Barcode Metadata Schema. |
| WiaImgFmt_RawBar | Barcode metadata is transferred as a WIA Barcode Metadata Raw Format file. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
