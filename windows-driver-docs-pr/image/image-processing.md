---
title: Image Processing
author: windows-driver-content
description: Image Processing
MS-HAID:
- 'WIA\_arch\_3233beea-55c0-4871-af2d-019dd1f4817f.xml'
- 'image.image\_processing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 84e10fcc-3998-434c-922a-65b42dccbdaf
---

# Image Processing


## <a href="" id="ddk-image-processing-si"></a>


Some minidrivers, in particular scanner minidrivers, require an image processing layer. This layer is mandatory only if the data acquired from the still image device requires some manipulation before being passed on to the application.

If the raw data acquired from the device needs no further processing, then the image processing layer can be omitted.

Microsoft recommends the use of GDI+ in the WIA minidriver if any image manipulation is required.

### Using GDI+ in a WIA Driver

GDI+ is a library that provides two-dimensional image manipulation routines. The library provides mechanisms for modifying image attributes, as well as for rotation and resizing.

To use GDI+ in the WIA minidriver, make sure that GDI+ is properly initialized. GDI+ can be initialized when the WIA minidriver is created and loaded. Also, make sure that the WIA driver includes *Gdiplus.h* and links to the *Gdiplus.lib* library.

For more information about GDI+, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Image%20Processing%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


