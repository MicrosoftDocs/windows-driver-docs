---
title: DirectX Runtime Behavior
description: DirectX Runtime Behavior
ms.assetid: 98cfb09c-74ed-4329-b663-5f813a84debe
keywords:
- DirectX runtime rotation WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectX Runtime Behavior


Various versions of the Microsoft DirectX runtime handle the following rotation situations on behalf of the driver:

-   The Microsoft DirectDraw runtime automatically fails any attempt to display an overlay while the display is rotated.

-   All versions of the DirectX runtime adjust the scan-line values that are returned while the primary surface is rotated so that the scan-line values cover the entire range up to the height of the resolution. Otherwise, an application that attempts beam chasing might stop responding if it waits for a scan-line value that is greater than the width of the display and that the application would otherwise never receive while in portrait mode.

-   All versions of the DirectX runtime handle all accesses to a rotated primary surface that are made by a windowed-mode device that uses various forms of emulation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectX%20Runtime%20Behavior%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




