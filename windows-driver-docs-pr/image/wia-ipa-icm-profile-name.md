---
title: WIA_IPA_ICM_PROFILE_NAME
description: The WIA_IPA_ICM_PROFILE_NAME property contains the image color management (ICM) profile name that is needed to properly decode an image.
keywords: ["WIA_IPA_ICM_PROFILE_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ICM_PROFILE_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPA_ICM_PROFILE_NAME

The WIA_IPA_ICM_PROFILE_NAME property contains the image color management (ICM) profile name that is needed to properly decode an image.

Property Type: VT_BSTR

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application reads the WIA_IPA_ICM_PROFILE_NAME property to determine the ICM profile to use when processing the image. The WIA service creates and maintains this property based on the ICMProfiles entry in the driver installation file.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
