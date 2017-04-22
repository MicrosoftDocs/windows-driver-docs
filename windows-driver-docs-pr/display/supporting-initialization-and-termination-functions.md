---
title: Supporting Initialization and Termination Functions
description: Supporting Initialization and Termination Functions
ms.assetid: 306be966-be23-4680-aeda-32e9cb1ac4a9
keywords:
- drawing WDK GDI , initialization
- drawing WDK GDI , initialization, about
- initializing graphics drivers WDK Windows 2000 display
- initializing graphics drivers WDK Windows 2000 display , about
- GDI WDK Windows 2000 display , initialization
- GDI WDK Windows 2000 display , initialization, about
- graphics drivers WDK Windows 2000 display , initialization
- graphics drivers WDK Windows 2000 display , initialization, about
- GDI WDK Windows 2000 display , termination
- graphics drivers WDK Windows 2000 display , termination
- drawing WDK GDI , termination
- terminating graphics drivers WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Initialization and Termination Functions


## <span id="ddk_supporting_initialization_and_termination_functions_gg"></span><span id="DDK_SUPPORTING_INITIALIZATION_AND_TERMINATION_FUNCTIONS_GG"></span>


A graphics driver can support multiple devices and multiple concurrent use of each device. Therefore, initialization and termination occur in three distinct layers, with each layer having its own timing. Initialization occurs in the following order:

1.  [Driver initialization](driver-initialization-and-cleanup.md)

2.  [PDEV initialization](pdev-initialization-and-cleanup.md)

3.  [Surface initialization](enabling-and-disabling-the-surface.md)

Termination occurs in the reverse order.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Initialization%20and%20Termination%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




