---
title: Linear Memory-Space Segments
description: Linear Memory-Space Segments
ms.assetid: c937eb39-b9ec-454e-98c5-7f5274328226
keywords:
- memory segments WDK display , linear memory-space segments
- linear memory-space segments WDK display
- memory-space segments WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Linear Memory-Space Segments


## <span id="ddk_linear_memory_space_segments_gg"></span><span id="DDK_LINEAR_MEMORY_SPACE_SEGMENTS_GG"></span>


A linear memory-space segment is the classical type of segment that display hardware uses. The linear memory-space segment conforms to the following model:

-   Virtualizes video memory located on the graphics adapter.

-   Is accessed directly by the GPU (that is, without redirection through page mapping).

-   Is managed linearly in a one-dimensional address space.

The driver sets the **Flags** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure to 0 to specify a linear memory-space segment. However, the driver can set the following bit-field flags to indicate additional segment support:

-   **CpuVisible** to indicate that the segment is CPU-accessible.

-   **UseBanking** to indicate that the segment is divided into banks.

The following figure shows a visual representation of a linear memory-space segment.

![diagram illustrating a linear memory-space segment](images/memspac.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Linear%20Memory-Space%20Segments%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




