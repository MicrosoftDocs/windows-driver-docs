---
title: Accessing the Graphics Adapter
description: Accessing the Graphics Adapter
keywords:
- display driver model WDK Windows 2000 , graphics
- Windows 2000 display driver model WDK , graphics
- display drivers WDK Windows 2000 , graphics
- graphics card access WDK Windows 2000 display
ms.date: 04/20/2017
---

# Accessing the Graphics Adapter


## <span id="ddk_accessing_the_graphics_adapter_gg"></span><span id="DDK_ACCESSING_THE_GRAPHICS_ADAPTER_GG"></span>


To ensure display performance, display drivers can access the graphics card in the following ways:

-   Indirectly--by sending IOCTLs to the video miniport driver of the graphics adapter. See [Communicating IOCTLs to the Video Miniport Driver](communicating-ioctls-to-the-video-miniport-driver.md).

-   Directly--by reading and writing to video memory (the *frame buffer*) or hardware registers. See [Accessing the Frame Buffer and Hardware Registers](accessing-the-frame-buffer-and-hardware-registers.md).

 

 





