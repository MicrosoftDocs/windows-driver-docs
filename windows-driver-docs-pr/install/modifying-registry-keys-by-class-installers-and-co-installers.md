---
title: Modifying Registry Keys by Class Installers and Co-installers
description: Modifying Registry Keys by Class Installers and Co-installers
keywords:
- registry WDK device installations , modifying registry keys
- registry WDK device installations , modifying registry keys, class installers
- registry WDK device installations , modifying registry keys, co-installers
- class installers WDK device installations , modifying registry keys
- co-installers WDK device installations , modifying registry keys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Registry Keys by Class Installers and Co-installers


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

Except under certain conditions, *class installers* and *co-installers* should not use the standard registry functions to create, change, or delete registry keys. In most cases, registry keys should only be modified by using directives that are put in [INF files](overview-of-inf-files.md). For more information about these directives, see [Summary of INF Directives](summary-of-inf-directives.md).

The following are exceptions to this rule:

-   When it is necessary, class installers and co-installers can use the standard registry functions to modify registry keys in the **HKLM\\Software** subtree.

    **Note**  We highly recommend that class installers and co-installers save custom device properties as entries within the device's *software keys*.

     

-   Class installers and co-installers are permitted to modify subkeys in the **HKLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers** registry key.

The following guidelines should be followed to safely modify registry keys by class installers or co-installers:

-   Class installers and co-installers must first use [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) or [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) to open handles to the registry keys that will be modified. After a handle has been opened, class installers and co-installers can use the standard registry functions to modify registry keys.

-   Class installers and co-installers must not use [**SetupDiDeleteDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey) to delete *software keys* or *hardware keys* for the device. For more information, see [Deleting the Registry Keys of a Device](deleting-the-registry-keys-of-a-device.md).

For more information about the standard registry functions, see [Registry Functions](/windows/win32/sysinfo/registry-functions).

