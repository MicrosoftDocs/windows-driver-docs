---
title: WIA_IPS_PRINTER_ENDORSER_XOFFSET
description: The WIA_IPS_PRINTER_ENDORSER_XOFFSET property is used to configure the horizontal coordinate, in thousandths of an inch (0.001 \ 0034;), of the top-left corner of the imprinting/endorsing region, relative to the top-left corner of the physical document to be scanned and imprinted/endorsed. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_XOFFSET Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_XOFFSET
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_XOFFSET

The **WIA_IPS_PRINTER_ENDORSER_XOFFSET** property is used to configure the horizontal coordinate, in thousandths of an inch (0.001"), of the top-left corner of the imprinting/endorsing region, relative to the top-left corner of the physical document to be scanned and imprinted/endorsed. The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

The WIA minidriver can update the valid range of values and the current value (if it becomes out of range) to the closest available position when the [**WIA_IPS_PRINTER_ENDORSER**](wia-ips-printer-endorser.md) property is changed to a new specific input source (in other words, from flatbed to feeder).

This property is optional for all Imprinter/Endorser data source items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
