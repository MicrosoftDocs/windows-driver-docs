---
title: WIA_DPC_UPLOAD_URL
description: The WIA_DPC_UPLOAD_URL property describes a standard Internet URL.
keywords: ["WIA_DPC_UPLOAD_URL Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_UPLOAD_URL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPC_UPLOAD_URL

The WIA_DPC_UPLOAD_URL property describes a standard Internet URL.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read/write

## Remarks

The WIA_DPC_UPLOAD_URL property describes a URL that images or objects, after they are acquired from a device, can be uploaded to in one of the following scenarios:

- A WIA application reads WIA_DPC_UPLOAD_URL and allows a user to automatically upload images to the URL.

- An application sets the URL, and other devices (for example, kiosks) use WIA_DPC_UPLOAD_URL.

The Microsoft Windows operating system does not upload images.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
