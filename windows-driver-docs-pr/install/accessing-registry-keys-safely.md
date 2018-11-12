---
title: Accessing Registry Keys Safely
description: Accessing Registry Keys Safely
ms.assetid: 81203790-66CB-42ee-82F8-2F0FFF04DF10
keywords:
- registry WDK device installations , accessing registry keys safely
- accessing registry keys safely WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Registry Keys Safely


Customer problems have frequently been traced to external components, such as third-party [device installation applications](writing-a-device-installation-application.md), that do the following:

-   Delete critical registry keys.

-   Modify the access permissions of critical registry keys.

Many of the problems seen with external components are caused by using the KEY_ALL_ACCESS access permission for registry keys. Starting with Windows Server 2003, [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973) grants only KEY_READ and KEY_WRITE access permissions and not KEY_ALL_ACCESS. Starting with Windows Vista, additional KEY_ALL_ACCESS restrictions are enforced.

Follow these guidelines to safely access registry keys:

-   Use the [SetupAPI](setupapi.md) functions only to open registry keys, especially the [*hardware keys*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key) and [*software keys*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) for a device.

    These functions address common problems that result from restrictions on access permissions.

-   The location and format of registry keys might change between different versions of Windows. Do not make assumptions about the location, format, or meaning of registry keys or values that are used for device and driver installation.

    For more information about registry keys and trees, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

-   Do not use the registry to directly access or modify the internal settings of the device.

-   Request only the minimal access permissions that are required for each task, such as the following:

    -   KEY_SET_VALUE

    -   KEY_CREATE_SUB_KEY

    -   KEY_QUERY_VALUE

    -   KEY_ENUMERATE_SUB_KEYS

-   Do not directly open the device setup class keys in the registry. As with any registry key, the location and name of device setup class keys might change between versions of Windows.

    To open device setup class keys safely, follow these guidelines:

    -   Use [**SetupDiOpenClassRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552065).

    -   Use [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) and set DIOCR_INSTALLER in the *Flags* parameter.

-   Do not directly open device interface class keys in the registry. As with any registry key, the location and name of device interface class keys might change between versions of Windows.

    To open device interface class keys safely, use [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) and set DIOCR_INSTALLER in the *Flags* parameter.

-   Use only INF directives to modify registry keys that are reserved for use by the operating system. For more information, see [Summary of INF Directives](summary-of-inf-directives.md).

-   [*Class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) and [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) cannot call registry functions to create, change, or delete registry values that are reserved for use by the operating system.

    For more information, see [Accessing the Registry by Class Installers and Co-Installers](accessing-the-registry-by-class-installers-and-co-installers.md).

For more information about the access permissions of registry keys, see [Registry Key Security and Access Rights](http://go.microsoft.com/fwlink/p/?linkid=194542).

 

 





