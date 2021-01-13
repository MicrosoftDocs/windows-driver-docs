---
title: Modifying Registry Values by Class Installers and Co-installers
description: Modifying Registry Values by Class Installers and Co-installers
keywords:
- registry WDK device installations , modifying registry values
- registry WDK device installations , modifying registry values, class installers
- registry WDK device installations , modifying registry values, co-installers
- class installers WDK device installations , modifying registry values
- co-installers WDK device installations , modifying registry values
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Registry Values by Class Installers and Co-installers


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

Except under certain conditions, *class installers* and *co-installers* must not call the standard registry functions to create, change, or delete registry values that are reserved for use by the operating system.

The following are exceptions to this rule:

-   When it is necessary, class installers and co-installers can use the standard registry functions to modify registry values in the **HKLM\\Software** subtree.

    **Note**  We highly recommend that class installers and co-installers save custom device properties as entries within the device's *software keys*.

     

-   Class installers and co-installers can modify the value of the [RunOnce registry key](runonce-registry-key.md). However, this value must consist of only calls to *Rundll32.exe*.

    Class installers and co-installers must follow the restrictions about how to use the [RunOnce registry key](runonce-registry-key.md) in [INF files](overview-of-inf-files.md). In particular, this registry key must be used only for the installation of software-only devices that are enumerated by using the software device enumerator (SWENUM).




-   Class installers and co-installers can modify the **CoInstallers32** and **EnumPropPages32** registry values in the device's *software key* when the installer handles [**DIF_REGISTER_COINSTALLERS**](./dif-register-coinstallers.md) requests.

The following guidelines should be followed to safely modify registry values by class installers or co-installers:

-   Class installers and co-installers must first use [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) or [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) to open handles to the registry keys that will be modified. After a handle has been opened, class installers and co-installers can use the standard registry functions to modify registry values.

-   Class installers and co-installers must not use [**SetupDiDeleteDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey) to delete *software keys* or *hardware keys* for the device.

For more information about the standard registry functions, see [Registry Functions](/windows/win32/sysinfo/registry-functions).
