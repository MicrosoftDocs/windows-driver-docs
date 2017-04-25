---
title: Mirror Driver Installation
description: Mirror Driver Installation
ms.assetid: 13b0ce22-f833-482c-815b-a596098ee6bc
keywords:
- display drivers WDK Windows 2000 , mirror drivers
- mirror drivers WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mirror Driver Installation


## <span id="ddk_mirror_driver_installation_gg"></span><span id="DDK_MIRROR_DRIVER_INSTALLATION_GG"></span>


The system installs a mirror driver in response to a Win32 **ChangeDisplaySettings** or **ChangeDisplaySettingsEx** call. You should implement a user-mode service to make one of these calls to install your mirror driver and maintain its settings. Use this application to:

-   Ensure that the mirror driver is loaded correctly at boot time. The application should specify the CDS\_UPDATEREGISTRY flag to save the settings to the registry, so that the driver will automatically be loaded on subsequent boots with the same [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) information described below.

-   Respond appropriately to desktop changes by getting display change notifications through the WM\_DISPLAYCHANGE message.

The sample *Mirror.exe*, which you can build from the source code files that ship with the Windows Driver Kit (WDK), implements a subset of the operations a user-mode service should provide to load a mirror driver.

Before the mirror driver is installed, the user-mode application should fill in a [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure that specifies the following display attributes:

-   Position (**dmPosition**)

-   Size (**dmPelsWidth** and **dmPelsHeight**)

-   Format of the mirrored display (**dmBitsPerPel**)

The user-mode application must also set **dmFields** appropriately, by including a flag for each of these structure members to be changed. The mirrored display's position coordinates must be specified in desktop coordinates; as such, they can span more than one device. To directly mirror the primary display, the mirror driver should specify its location to coincide with the primary display's desktop coordinates.

After the DEVMODEW structure members have been set, change the mirrored display settings by passing this structure in a call to the Win32 **ChangeDisplaySettingsEx** function.

After the mirror driver is installed, it will be called by GDI for all rendering operations that intersect the driver's display region. GDI might not send all drawing operations to the mirror driver if the mirror driver overlaps only the primary display in a multiple-monitor system.

See the Microsoft Windows SDK documentation for more information about the **ChangeDisplaySettings** and **ChangeDisplaySettingsEx** functions, and display change desktop notifications.

**Note**  Starting with Windows 8, mirror drivers will not install on the system. For more information, see [Mirror Drivers](mirror-drivers.md).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Mirror%20Driver%20Installation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




