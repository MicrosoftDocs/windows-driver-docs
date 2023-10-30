---
title: WIA_IPS_PRINTER_ENDORSER_COUNTER
description: The WIA_IPS_PRINTER_ENDORSER_COUNTER property is used to configure the starting value and incrementing step for the imprinter/endorser counter at the beginning of a new WIA application session. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_COUNTER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_COUNTER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_COUNTER

The **WIA_IPS_PRINTER_ENDORSER_COUNTER** property is used to configure the starting value and incrementing step for the imprinter/endorser counter at the beginning of a new WIA application session. The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

The mandatory default value for the **WIA_IPS_PRINTER_ENDORSER_COUNTER** property is 0 (first page).

The range step value describes the increment value for the printer/endorser counter value (the minidriver increments this value after each document page that gets scanned). This counter step has a different purpose and should not be confused with the step configurable through the [**WIA_IPS_PRINTER_ENDORSER_STEP**](wia-ips-printer-endorser-step.md) property.

This property is required to be supported by all Imprinter/Endorser data source items. The value of 0 (first page) is required.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
