---
title: Controlling Variables Through the Watch Window
description: Controlling Variables Through the Watch Window
ms.assetid: bd857442-fbd7-4c00-9743-6077d38ee38e
keywords: ["Watch window, global variables", "Watch window, local variables"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Controlling Variables Through the Watch Window


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


In WinDbg, you can also use the Watch window to display and change global and local variables.

The Watch window can display any list of variables that you want. These variables can include global variables and local variables from any function. At any time, the Watch window displays the values of those variables that match the current function's scope. You can also change the values of these variables through the Watch window.

Unlike the Locals window, the Watch window is not affected by changes to the local context. Only those variables that are defined in the scope of the current program counter can have their values displayed or modified.

 

 





