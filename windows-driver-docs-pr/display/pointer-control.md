---
title: Pointer Control
description: Pointer Control
ms.assetid: 70e80be0-28f8-40a7-9018-fab71d80c8f6
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- passing pointer information WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pointer Control


## <span id="ddk_pointer_control_gg"></span><span id="DDK_POINTER_CONTROL_GG"></span>


Every application must be able to control a pointer that moves around a windowed display in response to a pointing device, such as a mouse. The display driver, GDI, or the video miniport driver can [draw the pointer](pointer-drawing.md). Refer also to [Controlling the Pointer](controlling-the-pointer--drvsetpointershape.md) and [Moving the Pointer](moving-the-pointer--drvmovepointer.md).

GDI can directly handle all pointer drawing for a display that uses a linearly addressable buffer. For a device that is not a [*linear frame buffer*](https://msdn.microsoft.com/library/windows/hardware/ff556305#wdkgloss-linear-frame-buffer), GDI uses [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182) for pointer drawing. However, pointer code supported by hardware and implemented in the display driver is much faster.

Display drivers can sometimes choose which kinds of pointers they will draw and which kind they will allow GDI to handle. For example, a device might support monochrome pointers in hardware but fail the color pointer calls, allowing GDI to handle them instead.

The display driver can control the pointer in situations for which the processor does not have to be owned exclusively and the pointer does not have to be drawn off an interrupt, such as the vertical synchronization interrupt. In these special cases, the miniport driver must draw and control the pointer because certain kernel-mode callbacks (which are only available in the video miniport driver) are required. This can adversely affect performance because it requires IOCTLs to communicate with the miniport driver for each pointer operation.

To write a display driver and miniport driver pair, you must include IOCTLs for passing pointer information between the two drivers, and to allow the miniport driver to assume the drawing of any or all pointers, if necessary.

 

 





