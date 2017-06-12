---
title: Windows 8 in-box graphics drivers treated as generic drivers
description: Windows 8 in-box graphics drivers, including the MS Basic Display Driver (MSBDD), are all treated like generic drivers by Windows and Windows Update.
ms.assetid: 4920450B-8E77-468C-812A-3794E51AE227
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="display.windows_8_in-box_graphics_drivers_treated_as_generic_drivers_"></span>Windows 8 in-box graphics drivers treated as generic drivers


In this scenario, Windows 8 in-box graphics drivers, including the MS Basic Display Driver (MSBDD), are all treated like generic drivers by Windows and Windows Update.

This means that any newer matching graphics driver package on Windows Update is offered as an *Important* update.

If the default settings for Windows 8 Windows Update are being used, an Important driver update downloads and installs without user intervention, and often without the user noticing that this update occurred.

When Windows 8 ships, the in-box graphics drivers are significantly older than the latest driver updates on Windows Update. This behavior ensures that the user experiences Windows 8 by using the latest/best graphics driver available.

**Note**  
The Windows 8 certified OEM graphics drivers that is provided on new computers sold with Windows 8 pre-installed are not considered generic. A newer, matching graphics driver on Windows Update would be offered as an Optional update in these cases. The user must actively choose to install an Optional driver update.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%208%20in-box%20graphics%20drivers%20treated%20as%20generic%20drivers%20%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




