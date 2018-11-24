---
title: High-Fidelity Print Output
description: High-Fidelity Print Output
ms.assetid: 37ff186e-d078-40f4-b7dc-9bf75e0b2847
keywords:
- color fidelity WDK XPSDrv
- print fidelity WDK XPSDrv
- high-fidelity print output WDK XPSDrv
- XPSDrv printer drivers WDK , high-fidelity print output
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# High-Fidelity Print Output


XPS-based printers can provide overall improved print and color fidelity. When end users print from applications that are built on Windows Presentation Foundation (WPF) or direct output to XPS-based printers or drivers, the XPS print path reduces or eliminates image data conversions and color space conversions wherever possible, so the print output can retain its original fidelity.

XPS printing provides more faithful rendering of graphics attributes such as gradients and transparency though native support of these attributes in the XPS spool file format. The XAML in the XPS Document format is compatible with WPF XAML. When users print from a WPF application, the Windows operating system removes animations and converts video and three-dimensional (3-D) elements to images. All other graphics data is represented in compatible graphics primitives that are ideal for device consumption. The device or driver directly consumes the printing version of WPF output.

During the automatic conversion of output from Microsoft Win32-based applications to XPS-based devices and drivers, print fidelity is enhanced by optimizing for specific GDI raster operations (ROPs) that are used for transparency simulation by GDI+ and gradients. If an application generates a bitmap instead of using ROPs, this optimization cannot be performed.

Print fidelity from WPF applications that print to non-XPS-based printers is also improved because the XPS-to-GDI conversion path is better than similar implementations in GDI+ that any applications use. The XPS-to-GDI conversion path tries to algebraically remove transparency (that is, alpha channel in colors and images and opacity and opacity mask on Canvas) in WPF graphics as much as possible, without using GDI raster operations and PostScript bitmasks.

 

 




