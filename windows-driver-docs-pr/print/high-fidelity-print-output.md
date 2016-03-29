---
title: High-Fidelity Print Output
description: High-Fidelity Print Output
ms.assetid: 37ff186e-d078-40f4-b7dc-9bf75e0b2847
keywords: ["color fidelity WDK XPSDrv", "print fidelity WDK XPSDrv", "high-fidelity print output WDK XPSDrv", "XPSDrv printer drivers WDK , high-fidelity print output"]
---

# High-Fidelity Print Output


XPS-based printers can provide overall improved print and color fidelity. When end users print from applications that are built on Windows Presentation Foundation (WPF) or direct output to XPS-based printers or drivers, the XPS print path reduces or eliminates image data conversions and color space conversions wherever possible, so the print output can retain its original fidelity.

XPS printing provides more faithful rendering of graphics attributes such as gradients and transparency though native support of these attributes in the XPS spool file format. The XAML in the XPS Document format is compatible with WPF XAML. When users print from a WPF application, the Windows operating system removes animations and converts video and three-dimensional (3-D) elements to images. All other graphics data is represented in compatible graphics primitives that are ideal for device consumption. The device or driver directly consumes the printing version of WPF output.

During the automatic conversion of output from Microsoft Win32-based applications to XPS-based devices and drivers, print fidelity is enhanced by optimizing for specific GDI raster operations (ROPs) that are used for transparency simulation by GDI+ and gradients. If an application generates a bitmap instead of using ROPs, this optimization cannot be performed.

Print fidelity from WPF applications that print to non-XPS-based printers is also improved because the XPS-to-GDI conversion path is better than similar implementations in GDI+ that any applications use. The XPS-to-GDI conversion path tries to algebraically remove transparency (that is, alpha channel in colors and images and opacity and opacity mask on Canvas) in WPF graphics as much as possible, without using GDI raster operations and PostScript bitmasks.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20High-Fidelity%20Print%20Output%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




