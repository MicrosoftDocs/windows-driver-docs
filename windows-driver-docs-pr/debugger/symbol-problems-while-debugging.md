---
title: Symbol Problems While Debugging
description: Symbol Problems While Debugging
ms.assetid: 2713c371-9683-4d0d-a8ab-8a4c897ba0ab
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Symbol Problems While Debugging


## <span id="ddk_debugging_user_mode_processes_without_symbols_dbg"></span><span id="DDK_DEBUGGING_USER_MODE_PROCESSES_WITHOUT_SYMBOLS_DBG"></span>


Invalid or missing symbols are one of the most common causes of debugger problems. When you see some sort of problem, you need to find out if you have a symbol issue.

In some cases, the solution involves acquiring the correct symbol files. In other cases, you simply need to reconfigure the debugger to recognize symbol files you already have. But if you are not able to get the correct symbol files, you will need to work around this problem and debug the target in a more limited manner.

This section includes:

[Verifying Symbols](verifying-symbols.md)

[Matching Symbol Names](matching-symbol-names.md)

[Reading Symbols from Paged-Out Headers](reading-symbols-from-paged-out-headers.md)

[Mapping Symbols When the PEB is Paged Out](mapping-symbols-when-the-peb-is-paged-out.md)

[Debugging User-Mode Processes Without Symbols](debugging-user-mode-processes-without-symbols.md)

[Debugging Performance-Optimized Code](debugging-performance-optimized-code.md)

 

 





