---
title: WIA_DPC_PICTURES_REMAINING
description: The WIA_DPC_PICTURES_REMAINING property contains the number of pictures that a user can take by using a camera device, given the current property settings. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPC_PICTURES_REMAINING Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_PICTURES_REMAINING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPC_PICTURES_REMAINING

The WIA_DPC_PICTURES_REMAINING property contains the number of pictures that a user can take by using a camera device, given the current property settings. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

If the WIA_DPC_PICTURES_REMAINING property settings change and the changes affect the size of the images that the camera device produces, the WIA minidriver should update the number of remaining pictures.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
