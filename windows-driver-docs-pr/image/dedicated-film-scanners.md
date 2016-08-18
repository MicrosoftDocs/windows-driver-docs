---
title: Dedicated Film Scanners
author: windows-driver-content
description: Dedicated Film Scanners
MS-HAID:
- 'WIA\_scanner\_tree\_24c59805-c15f-4655-bf67-defacc4cd265.xml'
- 'image.dedicated\_film\_scanners'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1f8b73eb-a81a-4db3-b5be-b0a01a12696a
---

# Dedicated Film Scanners


## <a href="" id="ddk-dedicated-film-scanners-si"></a>


A *dedicated* film scanner is a scanner that performs only film scanning. This device has only a film scanning surface from which to scan and has the same requirements as a flatbed scanner with film scanning capabilities. That is, the film scanner item must exist and must contain the physical dimensions of the scanning area. This area can be a single scanning frame for film-feeder scanners or a template area.

The following figure illustrates the WIA item tree of a dedicated film scanner with a multiframe scan and shows the physical device and documents.

![diagram illustrating the item tree of a dedicated film scanner with multiframe scanning](images/art-scanner-film.png)

In the preceding figure, the tree on the left represents the scanner item tree. The curved lines that are drawn to the elements on the right symbolize the physical device and documents that are represented by this item tree.

The following figure illustrates the WIA item tree of a dedicated film scanner with a single frame scan and shows the physical device and documents.

![diagram illustrating the item tree of a dedicated film scanner with single-frame scanning](images/art-scanner-film2.png)

In the preceding figure, the tree on the left represents the scanner item tree. The curved lines that are drawn to the elements on the right symbolize the physical device and documents that are represented by this item tree.

It is important to note that the film item must be able to return a representation of the film scanning surface. Applications that are written for Microsoft Windows XP or Windows Me that have no knowledge of film scanning should still be able to scan by using a dedicated film scanner.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Dedicated%20Film%20Scanners%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


