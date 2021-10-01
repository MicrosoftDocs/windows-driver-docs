---
title: WIA_DPC_DIGITAL_ZOOM
description: The WIA_DPC_DIGITAL_ZOOM property contains the effective zoom ratio of a digital camera's acquired image, scaled by a factor of 10.
keywords: ["WIA_DPC_DIGITAL_ZOOM Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_DIGITAL_ZOOM
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DPC_DIGITAL_ZOOM

The WIA_DPC_DIGITAL_ZOOM property contains the effective zoom ratio of a digital camera's acquired image, scaled by a factor of 10.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

A WIA_DPC_DIGITAL_ZOOM value of 10 corresponds to the absence of digital zoom (1X), which is the standard scene size that the camera captures. A value of 20 corresponds to a 2X zoom, where the camera captures one-fourth of the standard scene size.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
