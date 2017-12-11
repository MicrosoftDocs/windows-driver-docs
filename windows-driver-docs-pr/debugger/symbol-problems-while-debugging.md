---
title: Symbol Problems While Debugging
description: Symbol Problems While Debugging
ms.assetid: 2713c371-9683-4d0d-a8ab-8a4c897ba0ab
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Symbol%20Problems%20While%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




