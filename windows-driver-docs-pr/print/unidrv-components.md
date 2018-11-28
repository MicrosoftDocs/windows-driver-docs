---
title: Unidrv Components
description: Unidrv Components
ms.assetid: 358eed9e-05e3-4670-b6b1-d5413c46edf0
keywords:
- Unidrv, components
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unidrv Components





Unidrv components consist of DLLs, plus text and binary data files, as illustrated in the following diagram:

![diagram illustrating how unidrv components consist of dlls, plus text and binary data files](images/unidrvcm.png)

Components in the diagram include:

<a href="" id="application"></a>**Application**  
A user application, such as a word processor, that provides users with printing capabilities.

<a href="" id="gdi32-dll"></a>**gdi32.dll**  
User-mode DLL that exports Win32 GDI functions.

<a href="" id="kernel-mode-graphics-engine-------"></a>Kernel-Mode Graphics Engine   
NT executive code that implements GDI functionality.

<a href="" id="minidriver-text-files"></a>**Minidriver Text Files**  
Text-based [Unidrv minidrivers](unidrv-minidrivers.md) that describe printers by using [GPD file entries](gpd-file-entries.md).

<a href="" id="binary-data-files"></a>**Binary Data Files**  
Temporary files (with a .bud extension) that Unidrv creates after parsing information contained in minidriver text files.

<a href="" id="unidrvui-dll"></a>**unidrvui.dll**  
[Unidrv user interface](unidrv-user-interface.md) DLL, providing common UI code for all Unidrv-supported printers.

<a href="" id="user-interface-plug-in"></a>**User Interface Plug-In**  
Optional, printer-specific, [user interface plug-in](user-interface-plug-ins.md).

<a href="" id="compstui-dll"></a>**compstui.dll**  
[CPSUI](common-property-sheet-user-interface.md) user interface for printers.

<a href="" id="unidrv-dll"></a>**unidrv.dll**  
[Unidrv renderer](unidrv-renderer.md), which renders images and sends the image data stream to the print spooler.

<a href="" id="rendering-plug-in"></a>**Rendering Plug-In**  
Optional, printer-specific, [rendering plug-in](rendering-plug-ins.md).

 

 




