---
title: Registry Trees for Devices and Drivers
description: Registry Trees for Devices and Drivers
ms.assetid: 74dc1889-26a9-47ba-8c8d-3cd6ed95cb68
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

**Note**  The keys under **HKLM\\SYSTEM\\CurrentControlSet** are a safe place to preserve data that is important to your driver because the data is stored in the system hive. The system takes additional precautions to protect the system hive (for example, keeping multiple copies).

 

 

 





