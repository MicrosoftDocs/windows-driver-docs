---
title: WIA_IPS_PRINTER_ENDORSER_STEP
description: By default the imprinter/endorser imprints or endorses on each document page that is scanned.
keywords: ["WIA_IPS_PRINTER_ENDORSER_STEP Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_STEP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_STEP

By default the imprinter/endorser imprints or endorses on each document page that is scanned. This mandatory default behavior can be changed by the client by using the **WIA_IPS_PRINTER_ENDORSER_STEP** property. For example, the client application can set the current value to 2 to have every other scanned page imprinted/endorsed (0, 2, 4, 6, ...). The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

The mandatory default value for the **WIA_IPS_PRINTER_ENDORSER_STEP** property is 1 (each page). A value of 0 is invalid.

As for most WIA_PROP_RANGE properties, the WIA minidriver can implement a range containing one single value, minimum equal with maximum and a step value of zero.

This property must be supported by all Imprinter/Endorser data source items. The value of 1 (each page) is required.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
