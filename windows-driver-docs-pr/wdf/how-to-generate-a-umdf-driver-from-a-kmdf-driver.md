---
title: How to convert a KMDF driver to a UMDF 2 driver (and vice-versa)
description: This topic describes how to convert a Kernel-Mode Driver Framework (KMDF) driver into a User-Mode Driver Framework (UMDF) version 2 driver, and vice-versa.
ms.assetid: 69B865CF-65D0-4211-951B-6574E27F10BD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to convert a KMDF driver to a UMDF 2 driver (and vice-versa)


This topic describes how to convert a Kernel-Mode Driver Framework (KMDF) driver into a User-Mode Driver Framework (UMDF) version 2 driver, and vice-versa.

## Driver Conversion using Visual Studio


1.  When switching from KMDF to UMDF, create an empty UMDF project in Visual Studio using the **User Mode Driver, Empty (UMDF V2)** project template. When switching from UMDF to KMDF, create an empty KMDF project in Visual Studio using the **Kernel Mode Driver, Empty (KMDF)** project template.

    Visual Studio creates an empty driver project with the appropriate settings, along with an INF file targeted to the specified framework.

2.  Copy the source code and header files from the previous driver into the new project.
3.  Update your header files. For UMDF, include Windows.h. For KMDF, include Ntddk.h. Wdf.h is common to both KMDF and UMDF, so include it in both types of drivers.

    Optionally, use the **\_KERNEL\_MODE** preprocessor macro to add the right system header conditionally:

    ```cpp
    #ifndef _KERNEL_MODE
    // This is a user-mode driver
    #include <windows.h>

    #else
    // This is a kernel-mode driver
    #include <ntddk.h>
    #define NTSTRSAFE_LIB
    #include <ntstrsafe.h>
    #endif

    // This is a common WDF header (for both KMDF and UMDF)
    #include <wdf.h> 
    ```

4.  Update the source code to either remove or conditionally compile (using the **\_KERNEL\_MODE** macro) any functionality that is not supported in the target driver model. For example:

    -   If your driver uses WPP tracing, update the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro. This macro takes different parameters in user mode and kernel mode.
        ```cpp
        WPP_INIT_TRACING ( DriverObject, RegistryPath ); // KMDF
        WPP_INIT_TRACING ( “<MyDriverNameString>” ); // UMDF
        ```

    -   If you are converting a KMDF driver that calls WDM routines such as [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520), replace these with the corresponding WDF methods, such as [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706). Similarly, if you are converting a UMDF driver that calls user-mode functions, replace these with equivalent kernel-mode routines.
    -   Some methods are supported only in KMDF, while others are supported only in UMDF. For a list of all Windows Driver Frameworks (WDF) methods and their framework applicability, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

 

 





