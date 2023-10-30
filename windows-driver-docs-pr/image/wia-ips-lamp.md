---
title: WIA_IPS_LAMP
description: The WIA_IPS_LAMP property contains the current configuration setting for a scanner's lamp. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_LAMP Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_LAMP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_LAMP

The WIA_IPS_LAMP property contains the current configuration setting for a scanner's lamp. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The WIA_IPS_LAMP property enables the programmatic control of the scanner lamp; this lamp could be a dedicated lamp (for a transparency adapter) or the main scanner lamp (for dedicated film scanners).

The following table describes the constants that are valid with WIA_IPS_LAMP.

| Value | Definition |
|--|--|
| WIA_LAMP_ON | The lamp is on. |
| WIA_LAMP_OFF | The lamp is off. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
