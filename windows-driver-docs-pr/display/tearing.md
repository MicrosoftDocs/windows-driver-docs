---
title: Tearing
description: Tearing
ms.assetid: b4c21592-cbdf-4dd6-9457-71d53b9f7b32
keywords: ["tears WDK DirectDraw", "drawing page flips WDK DirectDraw , tearing", "DirectDraw flipping WDK Windows 2000 display , tearing", "page flipping WDK DirectDraw , tearing", "flipping WDK DirectDraw , tearing", "surfaces WDK DirectDraw , flipping"]
---

# Tearing


## <span id="ddk_tearing_gg"></span><span id="DDK_TEARING_GG"></span>


As discussed in the [Flipping](flipping.md) section, a flip essentially changes a memory pointer so that it points to a new region of display memory (see the Permedia2 sample code). The surface being flipped away from must be finished being displayed before the application can lock, blt, or alter that memory, or a tear may result (as shown in the following figure).

![diagram illustrating tearing and no tearing](images/ddfig8.png)

A tear may also occur if the surface being flipped to is having data written to it during the flip. Tearing is universal and may happen any time an image is being drawn and displayed at the same time. Faster frame rates do not solve this problem. Because primary surfaces, overlays, and textures are all DirectDraw surfaces, they can be flipped the same way to prevent tearing.

A tear occurs when a page flip or blt happens at the wrong time. For example, if a page flips while the monitor scan line is in the middle of displaying a surface, as represented by the dashed line in the preceding figure, a tear occurs. The tear can be avoided by timing the flip to occur only after the entire surface has been displayed (as in the lower example of the figure). A tear can also occur when blitting to a surface that is in the process of being displayed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Tearing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




