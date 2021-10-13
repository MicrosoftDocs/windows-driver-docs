---
title: WIA_IPC_THUMBNAIL
description: The WIA_IPC_THUMBNAIL property contains the 24-bits-per-pixel thumbnail data bits. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPC_THUMBNAIL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPC_THUMBNAIL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPC_THUMBNAIL

The WIA_IPC_THUMBNAIL property contains the 24-bits-per-pixel thumbnail data bits. The WIA minidriver creates and maintains this property.

Property Type: VT_UI1 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The thumbnail data that the WIA_IPC_THUMBNAIL property contains must be in uncompressed bitmap data and aligned on 32-bit boundaries. An application reads the values of the [**WIA_IPC_THUMBNAIL_WIDTH**](wia-ipc-thumbnail-width.md) and [**WIA_IPC_THUMBNAIL_HEIGHT**](wia-ipc-thumbnail-height.md) properties and creates a BITMAPINFOHEADER structure (which is described in the Microsoft Windows SDK documentation). The application should be able to read the WIA_IPC_THUMBNAIL property (which represents the actual thumbnail image data) and use this property to write the data directly into the newly created bitmap to create the thumbnail image.

WIA_IPC_THUMBNAIL is used by WIA minidrivers and applications that are running on Microsoft Windows XP, Windows Me, and later versions of the operating system.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPC_THUMBNAIL_HEIGHT**](wia-ipc-thumbnail-height.md)

[**WIA_IPC_THUMBNAIL_WIDTH**](wia-ipc-thumbnail-width.md)
