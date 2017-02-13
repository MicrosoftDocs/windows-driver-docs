---
title: VGA-Compatible Video Miniport Drivers (Windows 2000 Model)
description: VGA-Compatible Video Miniport Drivers (Windows 2000 Model)
ms.assetid: c3a7bcbc-d9e9-488c-9e97-34ab85489ab9
keywords: ["video miniport drivers WDK Windows 2000 , VGA", "VGA WDK video miniport", "VGA WDK video miniport , about VGA-compatible drivers"]
---

# VGA-Compatible Video Miniport Drivers (Windows 2000 Model)


## <span id="ddk_vga_compatible_video_miniport_drivers_windows_2000_model__gg"></span><span id="DDK_VGA_COMPATIBLE_VIDEO_MINIPORT_DRIVERS_WINDOWS_2000_MODEL__GG"></span>


On x86-based NT-based operating system platforms, there are two kinds of video miniport drivers: nonVGA-compatible miniport drivers and VGA-compatible miniport drivers.

Most miniport drivers are nonVGA-compatible, and are consequently much simpler to implement. NonVGA-compatible video miniport drivers rely on having the system-supplied VGA miniport driver (vga.sys) or another VGA-compatible SVGA miniport driver loaded concurrently. Such a miniport driver is set up to configure itself in the registry with VgaCompatible set to zero (FALSE) and has the following features:

-   It provides no special support for full-screen MS-DOS applications in x86-based machines. Instead, it is loaded along with a system-supplied VGA (or, possibly, with a VGA-compatible SVGA) miniport driver, which provides this support for full-screen MS-DOS applications.

-   In most cases, it either is written for an adapter that has no VGA compatibility mode or for an accelerator that works independently of the VGA.

A VGA-compatible miniport driver is based on the system-supplied VGA miniport driver, with code modified to support adapter-specific features. The system-supplied VGA display drivers use the support provided by VGA-compatible miniport drivers, so the developer of a new miniport driver for a VGA-compatible adapter need not write a new display driver. It provides support for full-screen MS-DOS applications to do I/O directly to the adapter registers. It also functions as a video validator to prevent such applications from issuing any sequence of instructions that would hang the machine.

Self-declared "VGA-compatible" miniport drivers are set up to configure themselves in the registry with VgaCompatible set to one (TRUE).

VGA-compatible miniport drivers in x86-based machines replace the system-supplied VGA miniport driver. Therefore, VGA-compatible miniport drivers must have a set of *SvgaHwIoPortXxx* functions to support full-screen MS-DOS applications as the system-supplied VGA miniport driver does.

The designer of a new VGA-compatible SVGA miniport driver should adapt one of the system-supplied SVGA miniport driver's *SvgaHwIoPortXxx* functions to the adapter's features. Miniport drivers for other types of adapters in x86-based machines can have a set of *SvgaHwIoPortXxx* routines and provide the same support at the discretion of the miniport driver designer or if the miniport driver cannot be loaded while the system VGA miniport driver is loaded.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20VGA-Compatible%20Video%20Miniport%20Drivers%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




