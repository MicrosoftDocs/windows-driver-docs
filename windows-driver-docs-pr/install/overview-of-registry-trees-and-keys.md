---
title: Registry Trees for Devices and Drivers
description: Registry Trees for Devices and Drivers
keywords:
- hardware keys WDK device installations
- registry WDK device installations
- software keys WDK device installations
- device installations WDK , registry
- installing devices WDK , registry
- Device setup WDK device installations , registry
- debugging device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Trees for Devices and Drivers





The following trees in the registry are of particular interest to driver writers (where **HKLM** represents **HKEY_LOCAL_MACHINE**):

-   [HKLM\\SYSTEM\\CurrentControlSet\\Services Registry Tree](hklm-system-currentcontrolset-services-registry-tree.md)

-   [HKLM\\SYSTEM\\CurrentControlSet\\Control Registry Tree](hklm-system-currentcontrolset-control-registry-tree.md)

-   [HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree](hklm-system-currentcontrolset-enum-registry-tree.md)

-   [HKLM\\SYSTEM\\CurrentControlSet\\HardwareProfiles Registry Tree](hklm-system-currentcontrolset-hardwareprofiles-registry-tree.md)

For information on accessing registry keys from WDF (KMDF or UMDF) drivers, see [Introduction to Registry Keys for Drivers](../wdf/introduction-to-registry-keys-for-drivers.md).

For information on accessing registry keys from WDM drivers, see [Plug and Play Registry Routines](../kernel/plug-and-play-registry-routines.md).
 

 

 





