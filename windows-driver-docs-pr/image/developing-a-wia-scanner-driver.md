---
title: Developing a WIA Scanner Driver
description: Developing a WIA Scanner Driver
MS-HAID:
- 'WIA\_drv\_scan\_d253061d-730b-4871-a2bb-b1545e8329d6.xml'
- 'image.developing\_a\_wia\_scanner\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: befe7e36-cb42-48da-88b4-d8983876266f
---

# Developing a WIA Scanner Driver


## <a href="" id="ddk-developing-a-wia-scanner-driver-si"></a>


A WIA scanner driver developer can create either a WIA microdriver or a WIA minidriver.

### Microdriver

A microdriver is a small driver that supports a simple flatbed scanner. This driver type can be developed more quickly than a minidriver, but has the following restrictions:

-   Microdrivers are limited to flatbed scanners only.

-   Microdrivers provide only minimal document feeder support (no duplex operations).

-   Microdrivers provide a limited number of resolutions in dots per inch (dpi): 75, 100, 150, 200, 300, and 600.

-   Microdrivers support only the WiaImgFmt\_BMP and WiaImgFmt\_MEMORYBMP image formats. For more information about these image formats, see the Microsoft Windows SDK.

-   Microdrivers do not support three-pass scanning (used by older color scanners to capture a color image using color filters).

For more information about developing microdrivers, see [Creating a WIA Microdriver](creating-a-wia-microdriver.md).

### Minidriver

A minidriver is a full WIA minidriver. See [Creating a WIA Minidriver](creating-a-wia-minidriver.md) section for more information.

This section contains additional information about the following topics:

[WIA Scanner Item Tree Layout](wia-scanner-item-tree-layout.md)

[Adding Document Feeder Support](adding-document-feeder-support.md)

[Page Size and Orientation](page-size-and-orientation.md)

[TWAIN Compatibility](twain-compatibility.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Developing%20a%20WIA%20Scanner%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




