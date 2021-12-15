---
title: Opening Registry Keys for a Device Setup Class
description: Opening Registry Keys for a Device Setup Class
keywords:
- registry WDK device installations , opening registry keys for a device setup class
- device setup classes WDK device installations , opening registry keys
ms.date: 04/20/2017
---

# Opening Registry Keys for a Device Setup Class


Do not directly access the registry keys for device setup classes. As with any registry key, the location and name of these keys might change between different versions of Windows.

To safely open the registry keys of a [device setup class](./overview-of-device-setup-classes.md), use one of the following [SetupAPI](setupapi.md) functions:

-   [**SetupDiOpenClassRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey)
-   [**SetupDiOpenClassRegKeyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa) with the *Flags* parameter set to DIOCR_INSTALLER

 

