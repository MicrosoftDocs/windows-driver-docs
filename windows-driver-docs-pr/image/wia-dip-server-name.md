---
title: WIA_DIP_SERVER_NAME
description: The WIA_DIP_SERVER_NAME property contains the name of the server that a WIA minidriver is running on.
keywords: ["WIA_DIP_SERVER_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_SERVER_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DIP_SERVER_NAME

The WIA_DIP_SERVER_NAME property contains the name of the server that a WIA minidriver is running on.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The default value of WIA_DIP_SERVER_NAME is "local". This property should contain the string "local" when an application is connected to a device on the same computer.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
