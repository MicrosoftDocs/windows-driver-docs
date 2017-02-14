---
title: Display Memory
description: Display Memory
ms.assetid: 92092bf2-dc31-4781-82c6-3365df77af99
keywords: ["display memory WDK DirectDraw , about display memory", "drawing memory WDK DirectDraw , about display memory", "DirectDraw memory WDK Windows 2000 display , about memory", "memory WDK DirectDraw , about memory", "drawing memory WDK DirectDraw", "DirectDraw memory WDK Windows 2000 display", "memory WDK DirectDraw", "display memory WDK DirectDraw"]
---

# Display Memory


## <span id="ddk_display_memory_gg"></span><span id="DDK_DISPLAY_MEMORY_GG"></span>


In general, allocating as much display memory as possible to DirectDraw increases display performance and allows games and other DirectDraw applications to run faster, with a better quality visual image.

Usually, display cards have the pitch set to the width of the display so that no memory is wasted to the right (conceptually) of the front buffer. This leaves one scratch area at the conceptual bottom that can be used for other surfaces. Memory access is very straightforward in this case because one pointer can reference the entire area of accessible display memory.

If the pitch is greater than the width of the primary surface, memory to the conceptual right of the front buffer is wasted. This has to be reclaimed as a separate rectangular heap, regardless of whether the memory on the card is linear or rectangular. (Even if the memory is linear, some display drivers fix the pitch to speed up the blitter. Rather than rewrite the driver, the memory can simply be reclaimed as a separate heap.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Display%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




