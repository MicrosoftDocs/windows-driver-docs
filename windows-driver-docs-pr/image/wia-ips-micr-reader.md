---
title: WIA_IPS_MICR_READER
description: The WIA minidriver uses the WIA_IPS_MICR_READER property to report the locations where a Magnetic Ink Character Recognition (MICR) reader is available. The WIA client application can choose one of these locations in which to enable MICR detection.
keywords: ["WIA_IPS_MICR_READER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_MICR_READER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_MICR_READER

The WIA minidriver uses the **WIA_IPS_MICR_READER** property to report the locations where a Magnetic Ink Character Recognition (MICR) reader is available. The WIA client application can choose one of these locations in which to enable MICR detection.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the required values for the **WIA_IPS_MICR_READER** property.

| Value | Definition |
|--|--|
| WIA_MICR_READER_DISABLED | MICR detection is disabled. This is the required default value. |
| WIA_MICR_READER_AUTO | MICR detection is enabled. The MICR reader location is fixed or is automatically selected by the device at run time depending on the active scan input source. |

This property is required for all MICR Reader items. The WIA_MICR_READER_DISABLED and WIA_MICR_READER_AUTO values are required. WIA_MICR_READER_DISABLED is the required default value.

The following table describes the optional values for the **WIA_IPS_MICR_READER** property.

| Value | Definition |
|--|--|
| WIA_MICR_READER_FLATBED | MICR detection is enabled for the documents scanned on the flatbed. |
| WIA_MICR_READER_FEEDER_FRONT | MICR detection is enabled for the front side of the documents scanned through the feeder. |
| WIA_MICR_READER_FEEDER_BACK | MICR detection is enabled for the front side of the documents scanned through the feeder. |
| WIA_MICR_READER_FEEDER_DUPLEX | MICR detection is enabled for both the front side and the back side of the documents scanned through the feeder. |

**Note**  The WIA minidriver is allowed to accept property configuration for the optional values but at scan time ignore requests to enable MICR detection to an inactive scan input source.

The [**WIA_IPA_FORMAT**](wia-ipa-format.md) property is also required for all MICR Reader items.

The following table describes the required values for the [**WIA_IPA_FORMAT**](wia-ipa-format.md) property when it is implemented on a MICR Reader item.

| Value | Definition |
|--|--|
| WiaImgFmt_XmlMic | MICR metadata is transferred as an XML file whose content is compliant with the WIA MICR Metadata Schema. |
| WiaImgFmt_RawMic | MICR metadata is transferred as a WIA MICR Metadata Raw Format file. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
