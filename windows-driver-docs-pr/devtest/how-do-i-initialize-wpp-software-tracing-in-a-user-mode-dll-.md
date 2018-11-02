---
title: How do I initialize WPP software tracing in a user-mode DLL
description: How do I initialize WPP software tracing in a user-mode DLL
ms.assetid: 386ed1ba-8a6e-469d-9a03-c8879efd2613
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I initialize WPP software tracing in a user-mode DLL?


Starting with Windows XP, you can initialize WPP tracing in a user-mode DLL by calling the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro to initialize WPP software tracing.

To avoid errors, use the following method.

-   Call the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro in the [DllMain](http://go.microsoft.com/fwlink/p/?linkid=179361) function of the DLL.

-   If your DLL is written in C, add a **\#define** statement for **WPP\_OLDCC** to your source code. Put the definition before the **\#include** statement for the [trace message header (.tmh) file](trace-message-header-file.md). The **WPP\_OLDCC** definition is required only for C code. It is not required for C++.

    For example:

    ```
    #define WPP_OLDCC
    #include "init.tmh"
    ```

You cannot initialize WPP software tracing in a **DllMain** function on Microsoft Windows 2000. Because WPP runs as part of a service on Windows 2000, initializing software tracing generates a remote procedure call, which is prohibited during DLL initialization.

 

 





