---
title: TraceLogging for Kernel-Mode Drivers and Components
description: This topic describes how to use the TraceLogging API from within kernel-mode drivers and components.
ms.date: 04/20/2017
---

# TraceLogging for kernel-mode drivers and components

This topic describes how to use the [TraceLogging](/windows/desktop/tracelogging/trace-logging-portal) API from within kernel-mode drivers and components.

Prerequisites:

- Windows 10
- Visual Studio 2013 (or later)
- Windows 10 SDK
- Windows Driver Kit (WDK) for Windows 10

## Include the TraceLogging header files

To use the TraceLogging API, include the TraceLogging header file TraceLoggingProvider.h. The other TraceLogging API header file, TraceLoggingActivity.h, is only available for use in user mode drivers written in C++.

```command
#include <wdm.h>
#include <TraceLoggingProvider.h> 
```

> [!NOTE]
> The wdm.h file is required for TraceLoggingProvider.h when developing kernel mode drivers.

## Declare your driver as a TraceLogging provider

1. Add the [**TRACELOGGING\_DECLARE\_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_declare_provider) macro to declare the provider handle variable. The macro has the syntax:

    ```command
    TRACELOGGING_DECLARE_PROVIDER(hProviderVariableName)
    ```

    The following example TraceLogging statement declares the variable named *g\_hProvider*.

    ```command
    TRACELOGGING_DECLARE_PROVIDER(g_hProvider);
    ```

    The variable you declare with [**TRACELOGGING\_DECLARE\_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_declare_provider) becomes the handle to the provider when you call the [**TRACELOGGING\_DEFINE\_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider) macro later in your code.

    > [!NOTE]
    > You might want to put this macro in a header file so that the handle to the TraceLogging provider is available globally.

2. Add the [**TRACELOGGING\_DEFINE\_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider) macro, and specify a name for the trace provider and the trace provider handle. The handle is the variable you declared in step 1. The syntax of the macro is:

    ```command
    TRACELOGGING_DEFINE_PROVIDER(hProviderVariableName, "ProviderName", providerId [,option])
    ```

    For example, the following statement defines a provider called MyTraceLoggingProviderKM and assigns it to the handle g\_hProvider. The providerId parameter is the ETW provider GUID.

    ```command
    TRACELOGGING_DEFINE_PROVIDER(g_hProvider, "MyTraceLoggingProviderKM",
        (0xb3864c38, 0x4273, 0x58c5, 0x54, 0x5b, 0x8b, 0x36, 0x08, 0x34, 0x34, 0x71));
    ```

    The [**TRACELOGGING\_DEFINE\_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider) macro allocates storage for a provider and defines a corresponding variable that is the global handle to the provider. The provider name must be a string literal (not a variable) and must not contain any '\\0' characters. The handle and copies of the handle are valid as long as the original handle is in scope.

    When you first create the handle with the **TRACELOGGING\_DEFINE\_PROVIDER** macro, the provider is in the unregistered state. In this state, the provider will ignore any trace write calls until it is registered.

    > [!NOTE]
    > For kernel-mode, be aware that while provider metadata is explicitly stored into TLG\_METADATA\_SEGMENT (.rdata), the variables you create for the handle (for example, g\_hProvider) and the name of the provider (for example, "MyTraceLoggingProviderKM") are not explicitly assigned a segment and will use the current implicit segments.

The **TRACELOGGING\_DEFINE\_PROVIDER** macro expects the variables passed to it to be in the nonpaged pool. If this is not the case already, the caller must set the data segment via \#pragma data\_seg (for uniqueVarName) or the const segment via \#pragma const\_seg (for g\_hMyProvider) before calling the **TRACELOGGING\_DEFINE\_PROVIDER** macro.

## Register the driver with TraceLogging

In your **DriverEntry** function you must register the TraceLogging provider.
To register the provider with TraceLogging, add the TraceLoggingRegister macro to **DriverEntry**:

```command
// Register the TraceLogging provider in the DriverEntry method.
TraceLoggingRegister(g_hProvider);
```

## Unregister the provider in the driver unload or cleanup routine

In your **DriverUnload** or cleanup function, unregister the TraceLogging provider.

```command
// Stop TraceLogging and unregister the provider
TraceLoggingUnregister(g_hProvider);
```

## Log events in your code

TraceLogging provides macros for logging events.

The basic macro is [**TraceLoggingWrite**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite). This macro has the following syntax:

```command
TraceLoggingWrite(g_hProvider, "EventName", args...)
```

Where g\_hProvider is the handle for the provider you defined and "EventName" is a string literal (not a variable) that you use to identify the specific event. Like **printf** or **DbgPrint**, the **TraceLoggingWrite** macro supports a variable number of additional parameters (up to 99). The parameters (args) must be TraceLogging wrapper macros, such as [**TraceLoggingLevel**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogginglevel), [TraceLoggingInt32](/windows/desktop/tracelogging/tracelogging-wrapper-macros), or [TraceLoggingString](/windows/desktop/tracelogging/tracelogging-wrapper-macros). The TraceLogging wrapper macros are defined in TraceLoggingProvider.h.

> [!NOTE]
> If you are using C++, you can use the [**TraceLoggingValue**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingvalue) wrapper macro to automatically adjust for type. If you are writing your driver in C, you must use the type-specific field macros (for example, **TraceLoggingInt32** or **TraceLoggingUnicodeString**).

The following example logs an event for the provider, g\_hProvider. The event is called "MyDriverEntryEvent." The macro makes use of the TraceLoggingPointer and TraceLoggingUnicodeString wrappers to write the pointer to the driver object and registry path to the trace log. The TraceLoggingUnicodeString wrapper takes an optional name. In this example, "RegPath" is the name of the RegistryPath value. If no name is specified, the value is used as the name.

```command
TraceLoggingWrite(
        g_hProvider,
        "MyDriverEntryEvent",
        TraceLoggingPointer(DriverObject),
        TraceLoggingUnicodeString(RegistryPath, "RegPath")); 
);
```

If you are instrumenting a kernel-mode driver (in C), you link to TraceLoggingProvider.h, and you can use the **TraceLoggingWrite**, **TraceLoggingWriteActivity**, or **TraceLoggingActivityMarker** macros. For examples of trace logging, see [TraceLogging Examples](tracelogging-examples.md).

If you are instrumenting a driver or component that is written in C++, you link to TraceLoggingProvider.h and TraceLoggingActivity.h. When you link to the C++ header, you can log events with the **TraceLoggingWriteStart**, **TraceLoggingWriteStop**, and **TraceLoggingWriteTagged** macros.

For examples of how to capture and view TraceLogging data, see [Capture and view TraceLogging data](capture-and-view-tracelogging-data.md).
