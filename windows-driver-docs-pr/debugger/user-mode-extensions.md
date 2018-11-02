---
title: User-Mode Extensions
description: User-Mode Extensions
ms.assetid: 83b0aca1-ad08-4384-a035-3d7bd2c1b4fe
keywords: ["extension commands ( commands), user-mode extensions", "ntsdexts.dll (user-mode extensions)", "uext.dll (user-mode extensions)", "user-mode extensions (ntsdexts.dll and uext.dll)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# User-Mode Extensions


## <span id="ddk_user_mode_extensions_dbg"></span><span id="DDK_USER_MODE_EXTENSIONS_DBG"></span>


This section of the reference describes extension commands that are primarily used during user-mode debugging.

The debugger will automatically load the proper version of these extension commands. Unless you have manually loaded a different version, you do not have to keep track of the DLL versions being used. See [Using Debugger Extension Commands](using-debugger-extension-commands.md) for a description of the default module search order. See [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md) for an explanation of how to load extension modules.

Each extension command reference page lists the DLLs that expose that command. Use the following rules to determine the proper directory from which to load this extension DLL:

-   If your target application is running on Windows XP or a later version of Windows, use winxp\\Ntsdexts.dll.

In addition, user-mode extensions that are not specific to any single operating system can be found in winext\\Uext.dll.

 

 





