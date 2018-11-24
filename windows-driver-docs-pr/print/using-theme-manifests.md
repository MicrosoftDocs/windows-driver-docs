---
title: Using Theme Manifests
description: Using Theme Manifests
ms.assetid: 8b3feb56-501b-4f35-937e-0be99338ae01
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Theme Manifests


If you add a theme manifest to your print driver for Windows XP, you can ensure that user interface elements in your driver match the Windows XP visual style.

The visual style in Windows XP is the result of changes in the Shell Common Controls (Comctl32.dll, version 6.0). This version is almost fully backward compatible with version 5.0. However, some problems can occur with drivers that were written for version 5.0 when they run under version 6.0. To avoid such problems, the print system does not force drivers to use Comctl32.dll version 6.0. For a sample theme manifest, see \\src\\print\\oemdll\\ThemeUI\\ThemeUI.Manifest in the WDK.

If you add a theme manifest to your driver that specifies dependency on version 6 of Comctl32.dll, it will work properly on Windows XP and later operating system versions, as well as on Windows 2000. Windows 2000 ignores the manifest; therefore any use of the activation context fails gracefully. Note that because Comctl32.dll version 5.0 is not contained in the global assembly cache (GAC), a manifest that specifies a dependency on this version of the DLL breaks the component. In this case, the call to the Win32 API **LoadLibrary** fails while trying to load Comctl32.dll.

An application can have a global (or application) manifest. If this global manifest contains a redirection to use Comctl32.dll version 6.0, this forces all of the UI that the application creates to use the same theme. One result of this is that printer drivers launched from an application with a global manifest might be forced to use Comctl32.dll version 6.0, regardless of any Comctl32.dll redirection in the driver manifest.

For more information about manifests and assemblies, activation contexts, isolated applications and side-by-side assembly sharing, see the Microsoft Windows SDK documentation.

 

 




