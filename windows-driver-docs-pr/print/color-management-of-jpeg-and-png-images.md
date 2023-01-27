---
title: Color Management of JPEG and PNG Images
description: Color Management of JPEG and PNG Images
keywords:
- JPEG color management WDK print
- PNG color management WDK print
- CHECKJPEGFORMAT
- CHECKPNGFORMAT
- compressed images WDK print
ms.date: 01/26/2023
---

# Color Management of JPEG and PNG Images

[!include[Print Support Apps](../includes/print-support-apps.md)]

For printers that provide hardware support of JPEG and PNG compressed images, color management must be handled by the driver or device and cannot be handled by GDI.

Before an application sends a JPEG or PNG compressed image to a printer, it will call ExtEscape with either the CHECKJPEGFORMAT or CHECKPNGFORMAT escape code. This results in a call to the driver's [**DrvQueryDeviceSupport**](/windows/win32/api/winddi/nf-winddi-drvquerydevicesupport) function, with a query type of either QDS_CHECKJPEGFORMAT or QDS_CHECKPNGFORMAT and a buffer containing the compressed image.

The driver can examine the image data and determine if it can support the image. Supporting the image must include performing color transformations if either the [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) structure's XO_DEVICE_ICM flag or XO_HOST_ICM flag is set, because GDI cannot perform color transformations on such images.

For these compressed images, color space information is typically contained within the image data. One exception is JFIF files, which are YCbCr-encoded and for which the default sRGB space is a good approximation. However, a JFIF file might contain a proprietary APP*x* marker that specifies a color space, in which case the driver must transform the image using the color space.

For more information about supporting JPEG and PNG compressed images, see the Remarks section for [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo).
