---
title: Developing a WIA Scanner Driver
description: Developing a WIA Scanner Driver
ms.assetid: befe7e36-cb42-48da-88b4-d8983876266f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing a WIA Scanner Driver





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

 

 




