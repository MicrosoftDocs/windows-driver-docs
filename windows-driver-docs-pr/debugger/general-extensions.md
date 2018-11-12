---
title: General Extensions
description: General Extensions
ms.assetid: 99ff4111-9f65-4e3d-beb3-0aa49f35a015
keywords: ["extension commands ( commands), general extensions", "exts.dll (general extensions)", "dbghelp.dll (general extensions)", "general extensions (exts.dll - dbghelp.dll)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# General Extensions


## <span id="ddk_general_extensions_dbg"></span><span id="DDK_GENERAL_EXTENSIONS_DBG"></span>


This section describes extension commands that are frequently used during both user-mode and kernel-mode debugging.

The debugger automatically loads the proper version of these extension commands. Unless you have manually loaded a different version, you do not have to keep track of the DLL versions that are being used. For more information about the default module search order, see [Using Debugger Extension Commands](using-debugger-extension-commands.md). For more information about how to load extension modules, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

Each extension command reference topics lists the DLLs that expose that command. Use the following rules to determine the proper directory to load this extension DLL from:

-   If your target computer is running Microsoft Windows XP or a later version of Windows, use winxp\\kdexts.dll, winxp\\ntsdexts.dll, winxp\\exts.dll, winext\\ext.dll, or dbghelp.dll.

 

 





