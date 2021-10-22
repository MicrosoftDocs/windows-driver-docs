---
title: WIA_DIP_PORT_NAME
description: The WIA_DIP_PORT_NAME property contains an installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_PORT_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_PORT_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DIP_PORT_NAME

The WIA_DIP_PORT_NAME property contains an installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DIP_PORT_NAME property to determine the port name.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
