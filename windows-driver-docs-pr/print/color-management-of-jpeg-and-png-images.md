---
title: Color Management of JPEG and PNG Images
description: Color Management of JPEG and PNG Images
ms.assetid: ece0578d-bf03-4eee-9568-40ef684ba8a7
keywords:
- JPEG color management WDK print
- PNG color management WDK print
- CHECKJPEGFORMAT
- CHECKPNGFORMAT
- compressed images WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Color Management of JPEG and PNG Images





For printers that provide hardware support of JPEG and PNG compressed images, color management must be handled by the driver or device and cannot be handled by GDI.

Before an application sends a JPEG or PNG compressed image to a printer, it will call ExtEscape with either the CHECKJPEGFORMAT or CHECKPNGFORMAT escape code. This results in a call to the driver's [**DrvQueryDeviceSupport**](https://msdn.microsoft.com/library/windows/hardware/ff556260) function, with a query type of either QDS\_CHECKJPEGFORMAT or QDS\_CHECKPNGFORMAT and a buffer containing the compressed image.

The driver can examine the image data and determine if it can support the image. Supporting the image must include performing color transformations if either the [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) structure's XO\_DEVICE\_ICM flag or XO\_HOST\_ICM flag is set, because GDI cannot perform color transformations on such images.

For these compressed images, color space information is typically contained within the image data. One exception is JFIF files, which are YCbCr-encoded and for which the default sRGB space is a good approximation. However, a JFIF file might contain a proprietary APP*x* marker that specifies a color space, in which case the driver must transform the image using the color space.

For more information about supporting JPEG and PNG compressed images, see the Remarks section for [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835).

 

 




