---
title: First Steps For DirectDraw Drivers
description: First Steps For DirectDraw Drivers
ms.assetid: 0bb00060-7887-447f-a3c9-394ae5ac84db
keywords:
- drawing WDK DirectDraw , DirectDraw driver
- DirectDraw WDK Windows 2000 display , DirectDraw driver
- DirectDraw driver WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# First Steps For DirectDraw Drivers


## <span id="ddk_first_steps_for_directdraw_drivers_gg"></span><span id="DDK_FIRST_STEPS_FOR_DIRECTDRAW_DRIVERS_GG"></span>


A good way to begin implementing DirectDraw functionality is to modify an existing driver. If no driver is available, start with the sample code in the DirectDraw portion of the Windows Driver Kit (WDK) and get driver initialization, lock, and flip working. From that base functionality, more powerful functionality can be added that will improve display performance.

The minimum driver functionality DirectDraw requires is the ability to lock, unlock, and flip a surface. Assuming the hardware supports the related operations, driver support should also be added for blts (including transparent blts, which are important for speed in games), stretching, and overlays, which are critical for video playback.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20First%20Steps%20For%20DirectDraw%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




