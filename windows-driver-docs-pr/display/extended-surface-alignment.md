---
title: Extended Surface Alignment
description: Extended Surface Alignment
ms.assetid: 3a91a826-7f57-4cad-b236-b41178ac3b17
keywords: ["drawing extended surface alignment WDK DirectDraw", "DirectDraw extended surface alignment WDK Windows 2000 display", "surfaces WDK DirectDraw , extended alignment", "extended surface alignment WDK DirectDraw", "heaps WDK DirectDraw", "alignment WDK DirectDraw extended surface"]
---

# Extended Surface Alignment


## <span id="ddk_extended_surface_alignment_gg"></span><span id="DDK_EXTENDED_SURFACE_ALIGNMENT_GG"></span>


Microsoft DirectDraw supports surface alignment requirements on a per-heap basis. This support was introduced in Microsoft DirectX 5.0. The driver can specify X and Y alignments for rectangular heaps, and pitch and start-offset alignments for linear heaps. These alignments can vary for different surface types.

Some display hardware cannot set its start-of-display offset in an atomic operation. At the beginning of a display period, it is possible for such hardware to latch a new start-of-display offset when the driver is only halfway through setting the value. DirectDraw now allows the driver to specify alignment requirements for visible back buffers. Some hardware may be able to express alignment requirements for potentially visible back buffers that force the start-of-display offset to be a value that requires only one register write. This technique can help avoid the occasional flicker that would otherwise be visible when the primary surface is flipped at a high frequency.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extended%20Surface%20Alignment%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




