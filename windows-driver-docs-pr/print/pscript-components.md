---
title: Pscript Components
description: Pscript Components
ms.assetid: 9f3bd004-e62c-42b6-99da-045c12e088a3
keywords: ["PostScript Printer Driver WDK print , components", "Pscript WDK print , components"]
---

# Pscript Components


## <a href="" id="ddk-pscript-components-gg"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pscript%20Components%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




