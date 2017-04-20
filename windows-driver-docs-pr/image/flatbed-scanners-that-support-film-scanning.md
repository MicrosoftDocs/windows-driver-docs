---
title: Flatbed Scanners that Support Film Scanning
author: windows-driver-content
description: Flatbed Scanners that Support Film Scanning
ms.assetid: ee77c2c6-41a2-43dd-90e4-baf902b46f69
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Flatbed Scanners that Support Film Scanning


## <a href="" id="ddk-flatbed-scanners-that-support-film-scanning-si"></a>


The following figure illustrates a possible WIA item tree of a flatbed scanner that supports film scanning by using the flatbed platen as the film scanning surface. The figure also illustrates the physical device and documents.

![diagram illustrating the item tree of a flatbed film scanner with platen-only scanning](images/art-flatbed-film.png)

In the preceding figure, the tree on the left represents the scanner item tree. The curved lines that are drawn to the elements on the right symbolize the physical device and documents that are represented by this item tree.

The film scanner item always represents the entire film scanning surface. The valid values for the extent settings should be restricted to the entire scanning surface so that preview scans always present a single image that represents the entire film scanning area. This single image is useful for applications that show the user a representation of the slides or film that are placed on the scanning surface. The extent settings for the individual frame items are limited to the physical dimensions of the film scanning surface. The bed size properties on the film item [**WIA\_DPS\_HORIZONTAL\_BED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551399) and [**WIA\_DPS\_VERTICAL\_BED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551445) should represent the physical dimensions of the film scanning area. Notice that the extent settings of the film scanning surface start at (0,0) even though it is located in the middle of the flatbed scanning platen. This numbering is because the film scanning surface has its own origin, independent of the flatbed scanning origin.

**Note**   Overlapping frame selection areas are allowed in a film scanning session.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Flatbed%20Scanners%20that%20Support%20Film%20Scanning%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


