---
title: Drivers That Assume State Information
description: Drivers That Assume State Information
ms.assetid: c4dfb701-c547-4e94-8fd8-05571508137c
keywords:
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , state information
- DirectDraw blitting WDK Windows 2000 display , state information
- blitting WDK DirectDraw , state information
- blt WDK DirectDraw , state information
- states WDK DirectDraw
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Drivers That Assume State Information


## <span id="ddk_drivers_that_assume_state_information_gg"></span><span id="DDK_DRIVERS_THAT_ASSUME_STATE_INFORMATION_GG"></span>


Most display drivers set up the state of the blitter when they do an operation. However, some display drivers expect the blitter to be in a known state. For example, some display drivers assume that the origin is set to do a standard blt rather than a transparent blt, and so on. In these cases, the state has to be reset after DirectDraw uses it.

Blts between two surfaces can be accomplished either with a fixed origin or with a separate origin for source and destination surfaces. If the display driver expects the origin to remain constant and DirectDraw changes it to access a secondary surface, the old pointer must be saved and restored when the operation is finished.

If this forces DirectDraw to wait while operations are being done so it can restore registers to their previous state, performance suffers. This is because DirectDraw's speed comes from being asynchronous.

Care must be taken in these cases to minimize the changes being made to the display state. Moving the origin in this scenario also wastes room on the stack that could otherwise be used for passing parameters.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Drivers%20That%20Assume%20State%20Information%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




