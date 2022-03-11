---
title: SetupAPI component
description: SetupAPI
keywords:
- SetupAPI WDK device installations , functions
- SetupAPI functions WDK , about SetupAPI functions
- SetupAPI functions WDK
- Device setup WDK device installations , SetupAPI
- device installations WDK , SetupAPI
- installing devices WDK , SetupAPI
- functions WDK SetupAPI
- device installations WDK , SetupAPI
ms.date: 03/11/2022
---

# SetupAPI

The Setup Application Programming Interface (SetupAPI) is a system component that provides two sets of functions:

-   [General setup functions](using-general-setup-functions.md)

-   [Device installation functions](using-device-installation-functions.md)

Device installation software can use these functions to perform custom operations in [*class installers*](writing-class-installers-and-co-installers.md), [*co-installers*](writing-a-co-installer.md), and [*device installation applications*](writing-a-device-installation-application.md).

> [!NOTE]
> Setupapi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/).  See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

This section contains the following topics, which provide general information about how to use the [general Setup functions](using-general-setup-functions.md) and [device installation functions](using-device-installation-functions.md) that are provided by SetupAPI:

[Using General Setup Functions](using-general-setup-functions.md)

[Using Device Installation Functions](using-device-installation-functions.md)

[Guidelines for Using SetupAPI](guidelines-for-using-setupapi.md)

**Note**  This section describes only a subset of the Setup functions in SetupAPI. For more information about this API, see [Setup API](/windows/desktop/SetupApi/setup-api-portal) .

 

 

