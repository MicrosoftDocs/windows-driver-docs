---
title: WIA_IPS_ORIENTATION
description: The WIA_IPS_ORIENTATION property describes the current orientation of the document to scan. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_ORIENTATION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_ORIENTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPS_ORIENTATION

The WIA_IPS_ORIENTATION property describes the current orientation of the document to scan. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application sets the WIA_IPS_ORIENTATION property to define the original orientation of a page or image to be acquired. For more information about how to use WIA_IPS_ORIENTATION, see [**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md).

The following table describes the constants that are valid with WIA_IPS_ORIENTATION.

| Value | Definition |
|--|--|
| LANDSCAPE | The orientation is a 90-degree counterclockwise rotation, relative to the PORTRAIT orientation. |
| PORTRAIT | The orientation is at 0 degrees. |
| ROT180 | The orientation is a 180-degree counterclockwise rotation, relative to the PORTRAIT orientation. |
| ROT270 | The orientation is a 270-degree counterclockwise rotation, relative to the PORTRAIT orientation. |

The WIA_IPS_ORIENTATION property describes the orientation of the document to scan. This property affects the current scan frame and available page sizes.

WIA_IPS_ORIENTATIONis different from the [**WIA_IPS_ROTATION**](wia-ips-rotation.md) property, which refers to a rotation that is applied to an image *after* it is scanned. So, a ROT180 value for WIA_IPS_ORIENTATION is different from a ROT180 value for WIA_IPS_ROTATION. For WIA_IPS_ORIENTATION, ROT180 describes the orientation of the physical document to scan, relative to the scan direction, and for WIA_IPS_ROTATION, ROT180 describes the rotation to apply to an image after it is scanned.

The WIA_IPS_ORIENTATION property is required for ADF items and optional for all other image acquisition items.

> [!NOTE]
> The compatibility layer within the WIA service does not add support for WIA_IPS_ORIENTATION to the ADF item that is translated from a Microsoft Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect that an ADF item will always support this property and should always check if WIA_IPS_ORIENTATION is supported at run time.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md)

[**WIA_IPS_ROTATION**](wia-ips-rotation.md)
