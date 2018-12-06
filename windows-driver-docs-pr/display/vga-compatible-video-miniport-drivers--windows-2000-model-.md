---
title: VGA-Compatible Video Miniport Drivers (Windows 2000 Model)
description: VGA-Compatible Video Miniport Drivers (Windows 2000 Model)
ms.assetid: c3a7bcbc-d9e9-488c-9e97-34ab85489ab9
keywords:
- video miniport drivers WDK Windows 2000 , VGA
- VGA WDK video miniport
- VGA WDK video miniport , about VGA-compatible drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





