---
title: Opening registry keys for a device setup class
description: Provides information about opening registry keys for a device setup class.
keywords:
- registry WDK device installations , opening registry keys for a device setup class
- device setup classes WDK device installations , opening registry keys
ms.date: 08/15/2022
---

# Opening registry keys for a device setup class

Do not directly access the registry keys for device setup classes. As with any registry key, the location and name of these keys might change between different versions of Windows.

To safely open the registry keys of a [device setup class](./overview-of-device-setup-classes.md), use one of the following functions:

- [**CM_Open_Class_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_class_keyw) with the *ulFlags* parameter set to *CM_OPEN_CLASS_KEY_INSTALLER*

- [**SetupDiOpenClassRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey)

- [**SetupDiOpenClassRegKeyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa) with the *Flags* parameter set to DIOCR_INSTALLER
