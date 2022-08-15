---
title: WIA_IPS_ROTATION
description: The WIA_IPS_ROTATION property contains the current rotation setting for image rotation, if it is implemented. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_ROTATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ROTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPS_ROTATION

The WIA_IPS_ROTATION property contains the current rotation setting for image rotation, if it is implemented. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application sets the WIA_IPS_ROTATION property to inform a driver how much (if at all) to rotate an image before the driver returns it to the application.

The following table describes the rotation constants that are defined for WIA_IPS_ROTATION.

| Constant | Definition                                                 |
|----------|------------------------------------------------------------|
| PORTRAIT | The driver will not rotate the image.                      |
| LANDSCAPE | The driver rotates the image 90 degrees counterclockwise.  |
| ROT180   | The driver rotates the image 180 degrees counterclockwise. |
| ROT270   | The driver rotates the image 270 degrees counterclockwise. |

The WIA minidriver is responsible for rotating image data before sending it back to the application. The application is responsible for checking the image headers to see the newly rotated values.

It can be difficult to understand the effect of rotation on the current image's selection area (which is defined by the [**WIA_IPS_XPOS**](wia-ips-xpos.md), [**WIA_IPS_YPOS**](wia-ips-ypos.md), [**WIA_IPS_XEXTENT**](wia-ips-xextent.md), and [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) properties).

*Selection area* refers to the selected area on the physical scanner bed that an image is be acquired from. The WIA_IPS_ROTATION property does *not* modify the selection area. The driver applies a counterclockwise rotation according to WIA_IPS_ROTATION only after the driver has acquired the appropriate selection area. WIA_IPS_ROTATION *does* affect the dimensions of the output image, so these dimensions must be reflected in the resulting image's data header.

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md) is not related to [**WIA_IPS_ORIENTATION**](wia-ips-orientation.md). WIA_IPS_ORIENTATION describes the orientation of the document to be scanned relative to the direction of the scan; in contrast, WIA_IPS_ROTATION describes the rotation that is to be applied to an image after it is scanned.

WIA_IPS_ORIENTATION can impact the area to be scanned. Not all page sizes are available in both landscape and portrait, and the extents of the image from an change in WIA_IPS_ORIENTATION could crop the image. WIA_IPS_ROTATION does not impact the image extents and is not related to the orientation of the document that is to be scanned.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_ORIENTATION**](wia-ips-orientation.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)
