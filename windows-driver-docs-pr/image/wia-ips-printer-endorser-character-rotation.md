---
title: WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION
description: The WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION property is used to configure the rotation of the individual characters in the printed or endorsed text.
keywords: ["WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION

The **WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION** property is used to configure the rotation of the individual characters in the printed or endorsed text. If supported, individual character rotation can be done in addition to the rotation of the current imprinted or endorsed region that is described by the [**WIA_IPS_ROTATION**](wia-ips-rotation.md) property. This feature is available with Windows 8 and later versions of Windows.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read-Write

## Remarks

Valid values for the **WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION** property are the same as the existing values for the **WIA_IPS_ROTATION** property.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
