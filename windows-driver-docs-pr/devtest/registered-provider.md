---
title: Registered Provider
description: Registered Provider
ms.assetid: d16e91d7-40ce-4a35-b3a7-f46f26a810bb
keywords: ["registered providers WDK software tracing", "trace providers WDK", "Event Tracing for Windows WDK , providers", "ETW WDK , providers", "providers WDK ETW"]
---

# Registered Provider


## <span id="ddk_registered_provider_tools"></span><span id="DDK_REGISTERED_PROVIDER_TOOLS"></span>


A *registered provider* is a [trace provider](trace-provider.md) that registers with Event Tracing for Windows (ETW), which are the tracing components of Windows. As part of the registration, Windows associates the trace provider's [control GUID](control-guid.md) with the GUIDs of its event trace classes. Users can enumerate registered providers and refer to them by name.

Trace providers typically register with ETW when they start, either by calling **RegisterTraceGuids** or by using the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro. They unregister just before they stop, either by calling **UnregisterTraceGuids** or by using the [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro.

Providers are not required to register with Windows, and many do not, so the list of registered providers on the system might not include many of the available trace providers.

Trace providers also can register with Windows Management Instrumentation (WMI) by submitting a Managed Object Format (MOF) file. Registering with WMI does not register a provider with ETW; the registrations are independent. Providers who register with WMI are not considered to be "registered providers."

To display trace messages from a registered provider, use [TraceView](traceview.md). For instructions, see [Creating a trace session for a registered provider](creating-a-trace-session-for-a-registered-provider.md).

For more information about registered providers, see [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) in the Microsoft Windows SDK.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Registered%20Provider%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




