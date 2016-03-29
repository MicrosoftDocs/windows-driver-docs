---
title: Unidrv Components
description: Unidrv Components
ms.assetid: 358eed9e-05e3-4670-b6b1-d5413c46edf0
keywords: ["Unidrv, components", "Unidrv WDK print"]
---

# Unidrv Components


## <a href="" id="ddk-unidrv-components-gg"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv%20Components%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




