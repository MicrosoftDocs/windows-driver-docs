---
title: TraceLogging for kernel-mode drivers and components
description: This topic describes how to use the TraceLogging API from within kernel-mode drivers and components.
ms.assetid: 6AF8DD2C-400F-4E9D-A6DF-40A847BCBD76
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="devtest.tracelogging_for_kernel-mode_drivers_and_components"></span>TraceLogging for kernel-mode drivers and components


This topic describes how to use the [TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636) API from within kernel-mode drivers and components.

Prerequisites:

-   Windows 10
-   Visual Studio 2013 (or later)
-   Windows 10 SDK
-   Windows Driver Kit (WDK) for Windows 10

## <span id="Include_the_TraceLogging_header_files"></span><span id="include_the_tracelogging_header_files"></span><span id="INCLUDE_THE_TRACELOGGING_HEADER_FILES"></span>Include the TraceLogging header files


To use the TraceLogging API, include the TraceLogging header file TraceLoggingProvider.h. The other TraceLogging API header file, TraceLoggingActivity.h, is only available for use in user mode drivers written in C++.

```
#include <wdm.h>
#include <TraceLoggingProvider.h> 
```

**Note**  The wdm.h file is required for TraceLoggingProvider.h when developing kernel mode drivers.



## <span id="Declare_your_driver_as_a_TraceLogging_provider"></span><span id="declare_your_driver_as_a_tracelogging_provider"></span><span id="DECLARE_YOUR_DRIVER_AS_A_TRACELOGGING_PROVIDER"></span>Declare your driver as a TraceLogging provider


1.  Add the [**TRACELOGGING\_DECLARE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904623) macro to declare the provider handle variable. The macro has the syntax:

    ```
    TRACELOGGING_DECLARE_PROVIDER(hProviderVariableName)
    ```

    The following example TraceLogging statement declares the variable named *g\_hProvider*.

    ```
    TRACELOGGING_DECLARE_PROVIDER(g_hProvider);
    ```

    The variable you declare with [**TRACELOGGING\_DECLARE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904623) becomes the handle to the provider when you call the [**TRACELOGGING\_DEFINE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904624) macro later in your code.

    **Tip**  You might want to put this macro in a header file so that the handle to the TraceLogging provider is available globally.



2.  Add the [**TRACELOGGING\_DEFINE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904624) macro, and specify a name for the trace provider and the trace provider handle. The handle is the variable you declared in step 1. The syntax of the macro is:

    ```
    TRACELOGGING_DEFINE_PROVIDER(hProviderVariableName, "ProviderName", providerId [,option])
    ```

    For example, the following statement defines a provider called MyTraceLoggingProviderKM and assigns it to the handle g\_hProvider. The providerId parameter is the ETW provider GUID.

    ```
    TRACELOGGING_DEFINE_PROVIDER(g_hProvider, "MyTraceLoggingProviderKM", 
        (0xb3864c38, 0x4273, 0x58c5, 0x54, 0x5b, 0x8b, 0x36, 0x08, 0x34, 0x34, 0x71));
    ```

    The [**TRACELOGGING\_DEFINE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904624) macro allocates storage for a provider and defines a corresponding variable that is the global handle to the provider. The provider name must be a string literal (not a variable) and must not contain any '\\0' characters. The handle and copies of the handle are valid as long as the original handle is in scope.

    When you first create the handle with the [**TRACELOGGING\_DEFINE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904624) macro, the provider is in the unregistered state. In this state, the provider will ignore any trace write calls until it is registered.

    **Note**  Note: For kernel-mode, be aware that while provider metadata is explicitly stored into TLG\_METADATA\_SEGMENT (.rdata), the variables you create for the handle (for example, g\_hProvider) and the name of the provider (for example, "MyTraceLoggingProviderKM") are not explicitly assigned a segment and will use the current implicit segments.




The [**TRACELOGGING\_DEFINE\_PROVIDER**](https://msdn.microsoft.com/library/windows/desktop/dn904624) macro expects the variables passed to it to be in the nonpaged pool. If this is not the case already, the caller must set the data segment via \#pragma data\_seg (for uniqueVarName) or the const segment via \#pragma const\_seg (for g\_hMyProvider) before calling the **TRACELOGGING\_DEFINE\_PROVIDER** macro.


## <span id="Register_the_driver_with_TraceLogging"></span><span id="register_the_driver_with_tracelogging"></span><span id="REGISTER_THE_DRIVER_WITH_TRACELOGGING"></span>Register the driver with TraceLogging


In your **DriverEntry** function you must register the TraceLogging provider.
To register the provider with TraceLogging, add the TraceLoggingRegister macro to **DriverEntry**:

```
// Register the TraceLogging provider in the DriverEntry method.
TraceLoggingRegister(g_hProvider);
```

## <span id="Unregister_the_provider_in_the_driver_unload_or_cleanup_routine"></span><span id="unregister_the_provider_in_the_driver_unload_or_cleanup_routine"></span><span id="UNREGISTER_THE_PROVIDER_IN_THE_DRIVER_UNLOAD_OR_CLEANUP_ROUTINE"></span>Unregister the provider in the driver unload or cleanup routine


In your **DriverUnload** or cleanup function, unregister the TraceLogging provider.
```
// Stop TraceLogging and unregister the provider
TraceLoggingUnregister(g_hProvider);
```

## <span id="Log_events_in_your_code"></span><span id="log_events_in_your_code"></span><span id="LOG_EVENTS_IN_YOUR_CODE"></span>Log events in your code


TraceLogging provides macros for logging events.

The basic macro is [**TraceLoggingWrite**](https://msdn.microsoft.com/library/windows/desktop/dn904617). This macro has the following syntax:

```
TraceLoggingWrite(g_hProvider, "EventName", args...)
```

Where g\_hProvider is the handle for the provider you defined and "EventName" is a string literal (not a variable) that you use to identify the specific event. Like **printf** or **DbgPrint**, the [**TraceLoggingWrite**](https://msdn.microsoft.com/library/windows/desktop/dn904617) macro supports a variable number of additional parameters (up to 99). The parameters (args) must be TraceLogging wrapper macros, such as [**TraceLoggingLevel**](https://msdn.microsoft.com/library/windows/desktop/dn933288), TraceLoggingInt32 , or TraceLoggingString. The TraceLogging wrapper macros are defined in TraceLoggingProvider.h.

**Note**  If you are using C++, you can use the [**TraceLoggingValue**](https://msdn.microsoft.com/library/windows/desktop/dn933292) wrapper macro to automatically adjust for type. If you are writing your driver in C, you must use the type-specific field macros (for example, TraceLoggingInt32 or TraceLoggingUnicodeString).



The following example, logs an event for the provider, g\_hProvider. The event is called "MyDriverEntryEvent." The macro makes use of the TraceLoggingPointer and TraceLoggingUnicodeString wrappers to write the pointer to the driver object and registry path to the trace log. The TraceLoggingUnicodeString wrapper takes an optional name. In this example, "RegPath" is the name of the RegistryPath value. If no name is specified, the value is used as the name.

```
TraceLoggingWrite(
        g_hProvider,
        "MyDriverEntryEvent",
        TraceLoggingPointer(DriverObject),
        TraceLoggingUnicodeString(RegistryPath, "RegPath")); 
);
```

If you are instrumenting a kernel-mode driver (in C), you link to TraceLoggingProvider.h, and you can use the TraceLoggingWrite, TraceLoggingWriteActivity, or TraceLoggingActivityMarker macros. For examples of trace logging, see [TraceLogging Examples](tracelogging-examples.md).

If you are instrumenting a driver or component that is written in C++, you link to TraceLoggingProvider.h and TraceLoggingActivity.h. When you link to the C++ header, you can log events with the TraceLoggingWriteStart, TraceLoggingWriteStop, and TraceLoggingWriteTagged macros.

For examples of how to capture and view TraceLogging data, see [Capture and view TraceLogging data](capture-and-view-tracelogging-data.md).









