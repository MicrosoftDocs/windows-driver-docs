---
title: Film Scanner Architecture
author: windows-driver-content
description: Film Scanner Architecture
ms.assetid: fe3a2c23-a520-4701-8178-02f50ac08767
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Film Scanner Architecture


## <a href="" id="ddk-film-scanner-architecture-si"></a>


Scanner devices that support slide or transparency scanning units should implement a film scanner item in their WIA item tree. This WIA item represents a programmable data source. It produces an image or images from film that is placed on the scanner's film scanning surface when a data transfer is requested from this item. The film scanner item should be located directly off the WIA root item and should contain one or more child items (called frames). *Frames* are film items that represent individual selection areas and the location of the selection area on the film scanning surface. The WIA driver determines whether these selections can be added, deleted, resized, or even relocated by setting the valid values of the extent settings.

The following topics describe the two types of film scanners:

[Flatbed Scanners That Support Film Scanning](flatbed-scanners-that-support-film-scanning.md)

[Dedicated Film Scanners](dedicated-film-scanners.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Film%20Scanner%20Architecture%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


