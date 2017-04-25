---
title: Color Management of JPEG and PNG Images
author: windows-driver-content
description: Color Management of JPEG and PNG Images
ms.assetid: ece0578d-bf03-4eee-9568-40ef684ba8a7
keywords:
- JPEG color management WDK print
- PNG color management WDK print
- CHECKJPEGFORMAT
- CHECKPNGFORMAT
- compressed images WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Color Management of JPEG and PNG Images


## <a href="" id="ddk-color-management-of-jpeg-and-png-images-gg"></a>


For printers that provide hardware support of JPEG and PNG compressed images, color management must be handled by the driver or device and cannot be handled by GDI.

Before an application sends a JPEG or PNG compressed image to a printer, it will call ExtEscape with either the CHECKJPEGFORMAT or CHECKPNGFORMAT escape code. This results in a call to the driver's [**DrvQueryDeviceSupport**](https://msdn.microsoft.com/library/windows/hardware/ff556260) function, with a query type of either QDS\_CHECKJPEGFORMAT or QDS\_CHECKPNGFORMAT and a buffer containing the compressed image.

The driver can examine the image data and determine if it can support the image. Supporting the image must include performing color transformations if either the [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) structure's XO\_DEVICE\_ICM flag or XO\_HOST\_ICM flag is set, because GDI cannot perform color transformations on such images.

For these compressed images, color space information is typically contained within the image data. One exception is JFIF files, which are YCbCr-encoded and for which the default sRGB space is a good approximation. However, a JFIF file might contain a proprietary APP*x* marker that specifies a color space, in which case the driver must transform the image using the color space.

For more information about supporting JPEG and PNG compressed images, see the Remarks section for [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Color%20Management%20of%20JPEG%20and%20PNG%20Images%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


