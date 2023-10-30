---
title: WIA_IPS_PRINTER_ENDORSER
description: The WIA_IPS_PRINTER_ENDORSER property is used by the WIA minidriver to list the locations where a printer/endorser device is available, and is used by an application to select one of these locations to enable imprinting/endorsing.
keywords: ["WIA_IPS_PRINTER_ENDORSER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER

The **WIA_IPS_PRINTER_ENDORSER** property is used by the WIA minidriver to list the locations where a printer/endorser device is available, and is used by an application to select one of these locations to enable imprinting/endorsing. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the required values for the **WIA_IPS_PRINTER_ENDORSER** property.

| Value | Definition |
|--|--|
| WIA_PRINTER_ENDORSER_DISABLED | Printing/endorsing is disabled. This is the required default value for the property. |
| WIA_PRINTER_ENDORSER_AUTO | Printing/endorsing is enabled. The location (if there are multiple locations available for this imprinter/endorser) is automatically selected by the device at run time depending on the active scan input source. |

The WIA minidriver is allowed to accept property configuration, but at scan time it ignores requests to enable printing/endorsing to an inactive scan input source.

The following table describes the optional values for the **WIA_IPS_PRINTER_ENDORSER** property.

| Value | Definition |
|--|--|
| WIA_PRINTER_ENDORSER_FLATBED | Printing/endorsing is enabled for the documents scanned on a flatbed scanner. |
| WIA_PRINTER_ENDORSER_FEEDER_FRONT | Printing/endorsing is enabled for the front side of the documents scanned through a feeder (either in simplex or duplex image scan mode). |
| WIA_PRINTER_ENDORSER_FEEDER_BACK | Printing/endorsing is enabled for the back side of the documents scanned through a feeder (either in simplex or duplex image scan mode). |
| WIA_PRINTER_ENDORSER_FEEDER_DUPLEX | Printing/endorsing is enabled for both sides of the documents scanned through a feeder (either in simplex or duplex image scan mode). |

This property must be supported by all Imprinter/Endorser data source items. The required default value is **WIA_PRINTER_ENDORSER_DISABLED**.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
