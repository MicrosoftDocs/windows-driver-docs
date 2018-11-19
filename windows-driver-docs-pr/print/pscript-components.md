---
title: Pscript Components
description: Pscript Components
ms.assetid: 9f3bd004-e62c-42b6-99da-045c12e088a3
keywords:
- PostScript Printer Driver WDK print , components
- Pscript WDK print , components
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript Components





Pscript components consist of DLLs, plus text and binary data files, as illustrated in the following diagram:

![diagram illustrating that pscript components consist of dlls, plus text and binary data files](images/pscript5.png)

Components in the diagram include:

<a href="" id="application"></a>**Application**  
A user application, such as a word processor, that provides users with printing capabilities.

<a href="" id="gdi32-dll"></a>**gdi32.dll**  
User-mode DLL that exports Win32 GDI functions.

<a href="" id="kernel-mode-graphics-engine"></a>**Kernel-Mode Graphics Engine**  
NT-based operating system executive code that implements GDI functionality.

<a href="" id="minidriver-text-files"></a>**Minidriver Text Files**  
Text-based [Pscript minidrivers](pscript-minidrivers.md), created using [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) files.

<a href="" id="binary-data-files"></a>**Binary Data Files**  
Temporary files (with a .bpd extension) that Pscript creates after parsing information contained in minidriver text files.

<a href="" id="ps5ui-dll"></a>**ps5ui.dll**  
[Pscript user interface](pscript-user-interface.md) DLL, providing common UI code for all Pscript-supported printers.

<a href="" id="user-interface-plug-in"></a>**User Interface Plug-In**  
Optional, printer-specific, [user interface plug-in](user-interface-plug-ins.md).

<a href="" id="compstui-dll"></a>**compstui.dll**  
[CPSUI](common-property-sheet-user-interface.md) user interface for printers.

<a href="" id="pscript5-dll"></a>**pscript5.dll**  
[Pscript renderer](pscript-renderer.md), which handles text output and renders images, then sends the text and image data to the print spooler.

<a href="" id="rendering-plug-in"></a>**Rendering Plug-In**  
Optional, printer-specific, [rendering plug-in](rendering-plug-ins.md).

 

 




