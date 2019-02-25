---
title: Opening Registry Keys for a Device Setup Class
description: Opening Registry Keys for a Device Setup Class
ms.assetid: B747EB2B-892C-4465-98E0-245FF7BC1E70
keywords:
- registry WDK device installations , opening registry keys for a device setup class
- device setup classes WDK device installations , opening registry keys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening Registry Keys for a Device Setup Class


Do not directly access the registry keys for device setup classes. As with any registry key, the location and name of these keys might change between different versions of Windows.

To safely open the registry keys of a [device setup class](device-setup-classes.md), use one of the following [SetupAPI](setupapi.md) functions:

-   [**SetupDiOpenClassRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552065)
-   [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) with the *Flags* parameter set to DIOCR_INSTALLER

 

 





