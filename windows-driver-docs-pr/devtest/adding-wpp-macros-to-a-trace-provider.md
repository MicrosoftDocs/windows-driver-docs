---
title: Adding WPP Macros to a Trace Provider
description: Adding WPP Macros to a Trace Provider
ms.assetid: fc6db47c-ef18-4454-a385-adee1858b9d4
keywords:
- Windows software trace preprocessor WDK , macros
- WPP software tracing WDK , macros
- macros WDK WPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding WPP Macros to a Trace Provider


## <span id="ddk_adding_wpp_macros_to_a_driver_tools"></span><span id="DDK_ADDING_WPP_MACROS_TO_A_DRIVER_TOOLS"></span>


To add the default form of WPP software tracing to a [trace provider](trace-provider.md), such as a kernel-mode driver or a user-mode application, add the following C preprocessor directives and WPP macro calls to the provider's source code:

-   An **\#include** directive of the following form to each source file that contains any WPP macros. This statement includes the [trace message header file](trace-message-header-file.md) created by the [WPP preprocessor](wpp-preprocessor.md) for each source file:

    ```
    #include <source-file-name.tmh>
    ```

    The trace message header file must be included in a source file before any WPP macro calls and after defining a [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro.

-   A [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) definition directive to each source file that includes other WPP macros.

    This definition specifies the driver's control GUID and the driver-defined trace flag names. The definition must be added to a source file before the **\#include** statement that includes the file's trace message header file.

-   One [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro call to the driver's source code.

    For drivers, this macro activates software tracing in the driver. This macro is typically called during driver initialization, for example in a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

    For user-mode applications, call this macro at a point in your source code where no tracing attempts have been previously made.

    After initialization, you can use [TraceView](traceview.md) or [Tracelog](tracelog.md) to start a software tracing session and to display trace messages.

-   One [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro call to the [trace provider's](trace-provider.md) source code. This macro deactivates software tracing in the driver.

    For drivers, this macro call is typically added to the driver's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine.

    For user-mode applications, call this macro at a point in your source code after the last tracing attempts has been made.

-   [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro calls to log trace messages.

 

 





