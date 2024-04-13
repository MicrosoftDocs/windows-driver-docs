---
title: Mirror Driver Installation
description: Mirror Driver Installation
keywords:
- display drivers WDK Windows 2000 , mirror drivers
- mirror drivers WDK Windows 2000 display
ms.date: 04/20/2017
---

# Mirror Driver Installation

> [!NOTE]
>
> Starting with Windows 8, mirror drivers will not install on the system. For more information, see [Mirror Drivers](mirror-drivers.md).

The system installs a mirror driver in response to a Win32 **ChangeDisplaySettings** or **ChangeDisplaySettingsEx** call. You should implement a user-mode service to make one of these calls to install your mirror driver and maintain its settings. Use this application to:

- Ensure that the mirror driver is loaded correctly at boot time. The application should specify the CDS_UPDATEREGISTRY flag to save the settings to the registry, so that the driver will automatically be loaded on subsequent boots with the same [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) information described below.

- Respond appropriately to desktop changes by getting display change notifications through the WM_DISPLAYCHANGE message.

The sample *Mirror.exe*, which you can build from the source code files that ship with the Windows Driver Kit (WDK), implements a subset of the operations a user-mode service should provide to load a mirror driver.

Before the mirror driver is installed, the user-mode application should fill in a [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure that specifies the following display attributes:

- Position (**dmPosition**)
- Size (**dmPelsWidth** and **dmPelsHeight**)
- Format of the mirrored display (**dmBitsPerPel**)

The user-mode application must also set **dmFields** appropriately, by including a flag for each of these structure members to be changed. The mirrored display's position coordinates must be specified in desktop coordinates; as such, they can span more than one device. To directly mirror the primary display, the mirror driver should specify its location to coincide with the primary display's desktop coordinates.

After the DEVMODEW structure members have been set, change the mirrored display settings by passing this structure in a call to the Win32 **ChangeDisplaySettingsEx** function.

After the mirror driver is installed, it will be called by GDI for all rendering operations that intersect the driver's display region. GDI might not send all drawing operations to the mirror driver if the mirror driver overlaps only the primary display in a multiple-monitor system.

See the Microsoft Windows SDK documentation for more information about the **ChangeDisplaySettings** and **ChangeDisplaySettingsEx** functions, and display change desktop notifications.
