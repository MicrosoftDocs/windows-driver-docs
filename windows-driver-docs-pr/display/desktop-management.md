---
title: Desktop Management
description: Desktop Management
keywords:
- display drivers WDK Windows 2000 , desktop management
- desktop management WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Desktop Management


## <span id="ddk_desktop_management_gg"></span><span id="DDK_DESKTOP_MANAGEMENT_GG"></span>


A display driver must implement [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode) and [**DrvGetModes**](/windows/win32/api/winddi/nf-winddi-drvgetmodes) to manage desktops.

If the display driver is palette-managed, it will also receive a call to [**DrvSetPalette**](/windows/win32/api/winddi/nf-winddi-drvsetpalette) to reset its palette to the correct state.

GDI's mechanism for handling dynamic mode changes has changed significantly in Windows 2000 and later operating system versions. The GDI HDEV assigned to a driver during initialization may differ from the HDEV assigned after the mode change is complete. Display drivers will generally be unaffected by this change for the following reasons:

-   Drivers have always assigned *ppdev-&gt;hdevEng = hdev* in their [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev) implementations.

-   Drivers have always referenced *ppdev-&gt;hdevEng* in any callbacks that require an HDEV.

 

