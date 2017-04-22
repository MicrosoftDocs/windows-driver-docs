---
title: Using Theme Manifests
author: windows-driver-content
description: Using Theme Manifests
ms.assetid: 8b3feb56-501b-4f35-937e-0be99338ae01
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Theme Manifests


If you add a theme manifest to your print driver for Windows XP, you can ensure that user interface elements in your driver match the Windows XP visual style.

The visual style in Windows XP is the result of changes in the Shell Common Controls (Comctl32.dll, version 6.0). This version is almost fully backward compatible with version 5.0. However, some problems can occur with drivers that were written for version 5.0 when they run under version 6.0. To avoid such problems, the print system does not force drivers to use Comctl32.dll version 6.0. For a sample theme manifest, see \\src\\print\\oemdll\\ThemeUI\\ThemeUI.Manifest in the WDK.

If you add a theme manifest to your driver that specifies dependency on version 6 of Comctl32.dll, it will work properly on Windows XP and later operating system versions, as well as on Windows 2000. Windows 2000 ignores the manifest; therefore any use of the activation context fails gracefully. Note that because Comctl32.dll version 5.0 is not contained in the global assembly cache (GAC), a manifest that specifies a dependency on this version of the DLL breaks the component. In this case, the call to the Win32 API **LoadLibrary** fails while trying to load Comctl32.dll.

An application can have a global (or application) manifest. If this global manifest contains a redirection to use Comctl32.dll version 6.0, this forces all of the UI that the application creates to use the same theme. One result of this is that printer drivers launched from an application with a global manifest might be forced to use Comctl32.dll version 6.0, regardless of any Comctl32.dll redirection in the driver manifest.

For more information about manifests and assemblies, activation contexts, isolated applications and side-by-side assembly sharing, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20Theme%20Manifests%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


