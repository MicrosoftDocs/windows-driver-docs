---
title: Example Global Logger Provider
description: Example Global Logger Provider
ms.assetid: 06de4d6f-747c-4cf9-a325-2b697b72a1e9
keywords: ["Global Logger trace session WDK , logging", "boot-time Global Logger trace session WDK , logging", "logs WDK tracing during boot"]
---

# Example: Global Logger Provider


The following screen shot shows the **GlobalLogger** subkey, which contains entries that configure the [Global Logger trace session](global-logger-trace-session.md). Under the **GlobalLogger** subkey is a **ControlGUID** subkey that represents a trace provider that logs to the Global Logger trace session. The **ControlGUID** subkey is selected, and the entries in the subkey appear in the right pane.

![screen shot of a subkey of a trace provider that logs to the global logger trace session on windows xp](images/globallogger.png)

In this example, the **ControlGUID** subkey represents the TraceDrv sample driver. The subkey is named for the Tracedrv [control GUID](control-guid.md), d58c126f-b309-11d1-969e-0000f875a5bc. Because the trace session is running on Windows XP, the GUID is not enclosed in braces.

The [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726) sample driver is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository available on GitHub.

This **ControlGUID** subkey contains a **Flags** entry and a **Level** entry. These entries are optional and their value is defined by the provider.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example:%20Global%20Logger%20Provider%20%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




