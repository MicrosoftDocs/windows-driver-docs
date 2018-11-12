---
title: Registered Provider
description: Registered Provider
ms.assetid: d16e91d7-40ce-4a35-b3a7-f46f26a810bb
keywords:
- registered providers WDK software tracing
- trace providers WDK
- Event Tracing for Windows WDK , providers
- ETW WDK , providers
- providers WDK ETW
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registered Provider


## <span id="ddk_registered_provider_tools"></span><span id="DDK_REGISTERED_PROVIDER_TOOLS"></span>


A *registered provider* is a [trace provider](trace-provider.md) that registers with Event Tracing for Windows (ETW), which are the tracing components of Windows. As part of the registration, Windows associates the trace provider's [control GUID](control-guid.md) with the GUIDs of its event trace classes. Users can enumerate registered providers and refer to them by name.

Trace providers typically register with ETW when they start, either by calling **RegisterTraceGuids** or by using the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro. They unregister just before they stop, either by calling **UnregisterTraceGuids** or by using the [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro.

Providers are not required to register with Windows, and many do not, so the list of registered providers on the system might not include many of the available trace providers.

Trace providers also can register with Windows Management Instrumentation (WMI) by submitting a Managed Object Format (MOF) file. Registering with WMI does not register a provider with ETW; the registrations are independent. Providers who register with WMI are not considered to be "registered providers."

To display trace messages from a registered provider, use [TraceView](traceview.md). For instructions, see [Creating a trace session for a registered provider](creating-a-trace-session-for-a-registered-provider.md).

For more information about registered providers, see [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) in the Microsoft Windows SDK.

 

 





