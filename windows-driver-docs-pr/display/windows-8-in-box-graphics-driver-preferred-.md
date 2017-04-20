---
title: Windows 8 in-box graphics driver preferred
description: In this scenario, Windows 8 in-box graphics driver are preferred over Windows 7 or older graphics drivers.
ms.assetid: 77B6F0A3-F8CE-473F-AF17-4C08237DC33C
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="display.windows_8_in-box_graphics_driver_preferred_"></span>Windows 8 in-box graphics driver preferred


In this scenario, Windows 8 in-box graphics driver are preferred over Windows 7 or older graphics drivers.

In a Windows 8 upgrade installation, if the graphics hardware is covered by a Windows 8 in-box driver, the graphics drivers from the previous Windows version is not migrated to Windows 8. This is true even when the older graphics driver is a 4-part match (graphics hardware + pc model specific), and the Windows 8 in-box graphics driver is only a 2-part match (graphics hardware specific only). This is because the Windows 8 in-box driver has a better feature score than any driver in-box or Logoâ€™ed for a previous Windows release. To understand the driver selection criteria, see [Driver matching criteria](driver-matching-criteria.md). If a Windows 8 certified driver was installed on Windows 7 before the Windows 8 upgrade installation, that driver will migrate.

**Note**  
A Windows 7 in-box graphics driver will never migrate to Windows 8, even if there is no Windows 8 in-box coverage for the graphics hardware. In this case, Windows 8 uses the Microsoft Basic Display Driver (MSBDD).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%208%20in-box%20graphics%20driver%20preferred%20%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




