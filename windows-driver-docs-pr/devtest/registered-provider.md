---
title: Registered Provider
description: Registered Provider
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

A *registered provider* is a [trace provider](trace-provider.md) that registers with [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md). Users can enumerate registered providers and refer to them by name.

Trace providers must register with ETW when they start, either by calling **EventRegister** or by using register macros or functions provided by a tracing framework, such as the [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro provided by WPP. They unregister just before they stop, either by calling **EventUnregister** or by using the framework unregister macro or function. Trace providers that do not register themselves cannot be enabled, and no events will be collected from them.

To display events from a registered provider, use [TraceView](traceview.md). For instructions, see [Creating a trace session for a registered provider](creating-a-trace-session-for-a-registered-provider.md).

For more information about registered providers, see [Event Tracing](/windows/desktop/ETW/event-tracing-portal) in the Microsoft Windows SDK.
