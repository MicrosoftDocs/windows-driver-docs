---
title: Desktop Management
description: Desktop Management
ms.assetid: 68ae302b-a39e-4aff-8be7-52081c318c9e
keywords:
- display drivers WDK Windows 2000 , desktop management
- desktop management WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Desktop Management


## <span id="ddk_desktop_management_gg"></span><span id="DDK_DESKTOP_MANAGEMENT_GG"></span>


A display driver must implement [**DrvAssertMode**](https://msdn.microsoft.com/library/windows/hardware/ff556178) and [**DrvGetModes**](https://msdn.microsoft.com/library/windows/hardware/ff556233) to manage desktops.

If the display driver is palette-managed, it will also receive a call to [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) to reset its palette to the correct state.

GDI's mechanism for handling dynamic mode changes has changed significantly in Windows 2000 and later operating system versions. The GDI HDEV assigned to a driver during initialization may differ from the HDEV assigned after the mode change is complete. Display drivers will generally be unaffected by this change for the following reasons:

-   Drivers have always assigned *ppdev-&gt;hdevEng = hdev* in their [**DrvCompletePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556181) implementations.

-   Drivers have always referenced *ppdev-&gt;hdevEng* in any callbacks that require an HDEV.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Desktop%20Management%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




