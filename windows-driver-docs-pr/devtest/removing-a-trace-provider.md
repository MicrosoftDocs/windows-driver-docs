---
title: Removing a Trace Provider
description: Removing a Trace Provider
ms.assetid: 3ea38137-9196-46a6-8cb5-04722cd43086
keywords: ["trace providers WDK", "providers WDK software tracing", "trace sessions WDK , providers", "removing trace providers", "disabling trace providers"]
---

# Removing a Trace Provider


You cannot use the TraceView window to remove or disable a trace provider from a running trace session. However, you can remove a provider while you are creating the trace session and before TraceView has started it.

While you are creating a trace session, use the following procedure to remove a trace provider:

1.  On the **File** menu, click **Create New Log Session**.

2.  In the **Name** list, click the provider you want to remove.

3.  Click **Remove Provider**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

You can also disable a trace provider in a session that TraceView started by typing the following command in a Command Prompt window.

```
traceview -disable SessionName -guid {#GUID | GUIDFile}
```

However, this command causes TraceView to stop the trace session. To continue, use a **traceview -start***SessionName* command to restart the trace session. For more information, see [**TraceView Control Commands**](traceview-control-commands.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Removing%20a%20Trace%20Provider%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




