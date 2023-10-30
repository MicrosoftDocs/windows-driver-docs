---
title: WIA_IPS_LAMP_AUTO_OFF
description: The WIA_IPS_LAMP_AUTO_OFF property contains the current configuration setting for automatically shutting off a scanner's lamp. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_LAMP_AUTO_OFF Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_LAMP_AUTO_OFF
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_LAMP_AUTO_OFF

The WIA_IPS_LAMP_AUTO_OFF property contains the current configuration setting for automatically shutting off a scanner's lamp. The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_IPS_LAMP_AUTO_OFF property enables the programmatic control of how long a lamp will be kept on when a scanner is not in use; this lamp could be a dedicated lamp (for a transparency adapter) or the main scanner lamp (for dedicated film scanners).

You should implement WIA_IPS_LAMP_AUTO_OFF only if the device supports an automatic lamp-off feature.

The valid values for WIA_IPS_LAMP_AUTO_OFF range from 0 through 4095 seconds.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
