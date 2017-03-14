---
title: Accessing the Frame Buffer and Hardware Registers
description: Accessing the Frame Buffer and Hardware Registers
ms.assetid: 6f735f33-0bb7-45b8-ac01-f34ec4937a8b
keywords: ["frame buffers WDK Windows 2000 display", "reduce display driver size WDK Windows 2000", "size WDK Windows 2000 display", "display drivers WDK Windows 2000 , size reduction", "video hardware registers WDK Windows 2000 display", "hardware registers WDK Windows 2000 display", "banks WDK Windows 2000 display", "banked memory WDK Windows 2000 display", "linear frame buffers WDK Windows 2000 display"]
---

# Accessing the Frame Buffer and Hardware Registers


## <span id="ddk_accessing_the_frame_buffer_and_hardware_registers_gg"></span><span id="DDK_ACCESSING_THE_FRAME_BUFFER_AND_HARDWARE_REGISTERS_GG"></span>


There are several ways to reduce display driver size. For example, you can implement only those functions that the display driver can perform faster than GDI, and then specify GDI to perform all other operations. GDI often performs a substantial amount of the drawing to [*linear frame buffers*](https://msdn.microsoft.com/library/windows/hardware/ff556305#wdkgloss-linear-frame-buffer) to reduce the size of the driver. GDI cannot access [*banked memory*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-banked-memory) directly; therefore, when the frame buffer is not linearly addressable, the display driver must divide the frame buffer into a series of [*banks*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bank) and provide a means for GDI to perform its draw operations to the appropriate bank. See [Supporting Banked Frame Buffers](supporting-banked-frame-buffers.md) for details.

The display driver has direct access to I/O-mapped and memory-mapped video registers. This access allows a display driver to achieve high performance. For example, the driver might need to access video hardware registers to send line-drawing commands at high throughput.

Similarly, for graphics cards, such as the S3, many of the innermost loops in the graphics engine code require reads and writes of several video controller ports (for example, text output in graphics mode, bit block transfers, and line drawing). Rather than requiring the display driver to send an IOCTL to the miniport driver for each request, the display driver is permitted to access the video hardware directly.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Accessing%20the%20Frame%20Buffer%20and%20Hardware%20Registers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




