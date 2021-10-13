---
title: WIA_DIP_WIA_VERSION
description: The WIA_DIP_WIA_VERSION property contains the number (as a string) of the current WIA version that is installed on a computer. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_WIA_VERSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_WIA_VERSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DIP_WIA_VERSION

The WIA_DIP_WIA_VERSION property contains the number (as a string) of the current WIA version that is installed on a computer. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads WIA_DIP_WIA_VERSION to determine the version of WIA that is installed on the computer.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
