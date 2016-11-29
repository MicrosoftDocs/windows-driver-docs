---
title: How do I initialize WPP software tracing in a user-mode DLL
description: How do I initialize WPP software tracing in a user-mode DLL
ms.assetid: 386ed1ba-8a6e-469d-9a03-c8879efd2613
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20initialize%20WPP%20software%20tracing%20in%20a%20user-mode%20DLL?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




