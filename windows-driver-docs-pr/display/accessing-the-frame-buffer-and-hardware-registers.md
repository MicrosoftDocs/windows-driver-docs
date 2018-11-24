---
title: Accessing the Frame Buffer and Hardware Registers
description: Accessing the Frame Buffer and Hardware Registers
ms.assetid: 6f735f33-0bb7-45b8-ac01-f34ec4937a8b
keywords:
- frame buffers WDK Windows 2000 display
- reduce display driver size WDK Windows 2000
- size WDK Windows 2000 display
- display drivers WDK Windows 2000 , size reduction
- video hardware registers WDK Windows 2000 display
- hardware registers WDK Windows 2000 display
- banks WDK Windows 2000 display
- banked memory WDK Windows 2000 display
- linear frame buffers WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the Frame Buffer and Hardware Registers


## <span id="ddk_accessing_the_frame_buffer_and_hardware_registers_gg"></span><span id="DDK_ACCESSING_THE_FRAME_BUFFER_AND_HARDWARE_REGISTERS_GG"></span>


There are several ways to reduce display driver size. For example, you can implement only those functions that the display driver can perform faster than GDI, and then specify GDI to perform all other operations. GDI often performs a substantial amount of the drawing to [*linear frame buffers*](https://msdn.microsoft.com/library/windows/hardware/ff556305#wdkgloss-linear-frame-buffer) to reduce the size of the driver. GDI cannot access [*banked memory*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-banked-memory) directly; therefore, when the frame buffer is not linearly addressable, the display driver must divide the frame buffer into a series of [*banks*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bank) and provide a means for GDI to perform its draw operations to the appropriate bank. See [Supporting Banked Frame Buffers](supporting-banked-frame-buffers.md) for details.

The display driver has direct access to I/O-mapped and memory-mapped video registers. This access allows a display driver to achieve high performance. For example, the driver might need to access video hardware registers to send line-drawing commands at high throughput.

Similarly, for graphics cards, such as the S3, many of the innermost loops in the graphics engine code require reads and writes of several video controller ports (for example, text output in graphics mode, bit block transfers, and line drawing). Rather than requiring the display driver to send an IOCTL to the miniport driver for each request, the display driver is permitted to access the video hardware directly.

 

 





