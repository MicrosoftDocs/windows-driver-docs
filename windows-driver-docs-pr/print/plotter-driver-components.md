---
title: Plotter Driver Components
author: windows-driver-content
description: Plotter Driver Components
ms.assetid: 6a976956-c188-4d31-b176-e97e09e8cc0b
keywords:
- Plotter Driver WDK print , components
- MSPlot WDK print , components
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Plotter Driver Components


## <a href="" id="ddk-plotter-driver-components-gg"></a>


MSPlot components consist of DLLs and binary data files, as illustrated in the following diagram.

![diagram illustrating how the msplot components consist of dlls and binary data files](images/msplot.png)

Components in the diagram include:

<a href="" id="application"></a>**Application**  
A user application that provides users with printing capabilities.

<a href="" id="gdi32-dll"></a>**gdi32.dll**  
User-mode DLL that exports Win32 GDI functions.

<a href="" id="kernel-mode-graphics-engine"></a>**Kernel-Mode Graphics Engine**  
NT-based operating system executive code that implements GDI functionality.

<a href="" id="minidrivers"></a>**Minidrivers**  
MSPlot minidrivers (.pcd files).

<a href="" id="cached--pcd-file-data"></a>**Cached .pcd file data**  
Minidriver data read from .pcd files.

<a href="" id="plotui-dll"></a>**plotui.dll**  
[Plotter driver user interface](plotter-driver-user-interface.md) DLL, providing common UI code for all MSPlot-supported printers.

<a href="" id="compstui-dll"></a>**compstui.dll**  
[CPSUI](common-property-sheet-user-interface.md) user interface for printers.

<a href="" id="plotter-dll"></a>**plotter.dll**  
[Plotter driver renderer](plotter-driver-renderer.md), which renders images and sends the image data stream to the spooler.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Plotter%20Driver%20Components%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


