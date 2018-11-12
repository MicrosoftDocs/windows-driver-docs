---
title: Kernel-Mode Extensions
description: Kernel-Mode Extensions
ms.assetid: e8e1e692-d991-427f-a2e7-b9eb1893fe83
keywords: ["extension commands ( commands), kernel-mode extensions", "kdextx86.dll (kernel-mode extensions)", "kdexts.dll (kernel-mode extensions)", "kext.dll (kernel-mode extensions)", "kernel-mode extensions (kdext .dll and kext.dll)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Kernel-Mode Extensions


## <span id="ddk_kernel_mode_extensions_dbg"></span><span id="DDK_KERNEL_MODE_EXTENSIONS_DBG"></span>


This section of the reference describes extension commands that are primarily used during kernel-mode debugging.

The debugger will automatically load the proper version of these extension commands. Unless you have manually loaded a different version, you do not have to keep track of the DLL versions being used. See [Using Debugger Extension Commands](using-debugger-extension-commands.md) for a description of the default module search order. See [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md) for an explanation of how to load extension modules.

Each extension command reference page lists the DLLs that expose that command. Use the following rules to determine the proper directory from which to load this extension DLL:

-   If your target computer is running Windows XP or a later version of Windows, use winxp\\Kdexts.dll.

In addition, kernel-mode extensions that are not specific to any single operating system can be found in winext\\kext.dll.

 

 





