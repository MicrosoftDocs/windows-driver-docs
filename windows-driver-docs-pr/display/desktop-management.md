---
title: Desktop Management
description: Desktop Management
ms.assetid: 68ae302b-a39e-4aff-8be7-52081c318c9e
keywords:
- display drivers WDK Windows 2000 , desktop management
- desktop management WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Desktop Management


## <span id="ddk_desktop_management_gg"></span><span id="DDK_DESKTOP_MANAGEMENT_GG"></span>


A display driver must implement [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178) and [**DrvGetModes**](https://msdn.microsoft.com/library/windows/hardware/ff556233) to manage desktops.

If the display driver is palette-managed, it will also receive a call to [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) to reset its palette to the correct state.

GDI's mechanism for handling dynamic mode changes has changed significantly in Windows 2000 and later operating system versions. The GDI HDEV assigned to a driver during initialization may differ from the HDEV assigned after the mode change is complete. Display drivers will generally be unaffected by this change for the following reasons:

-   Drivers have always assigned *ppdev-&gt;hdevEng = hdev* in their [**DrvCompletePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556181) implementations.

-   Drivers have always referenced *ppdev-&gt;hdevEng* in any callbacks that require an HDEV.

 

 





