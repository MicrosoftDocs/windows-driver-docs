---
title: Plotter Driver Components
description: Plotter Driver Components
ms.assetid: 6a976956-c188-4d31-b176-e97e09e8cc0b
keywords:
- Plotter Driver WDK print , components
- MSPlot WDK print , components
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plotter Driver Components





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

 

 




