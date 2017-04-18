---
title: Example 2 Basic Start Command with Provider
description: Example 2 Basic Start Command with Provider
ms.assetid: 86730943-107e-441a-a860-4df540bc0426
keywords: ["trace sessions WDK , starting", "start command", "-start command", "guid parameter", "-guid parameter", "starting trace sessions"]
---

# Example 2: Basic Start Command with Provider


The following start command is identical to the command in Example 1, except that it uses the **-guid** parameter to enable a provider for the trace session:

```
tracelog -start MyTrace -guid #d58c126f-b309-11d1-969e-0000f875a5bc
```

The command starts a trace session named "My Trace". It uses the **-guid** parameter to specify the control GUID of the trace provider. The GUID is preceded by a number sign (**\#**) to indicate that it is a GUID and not a GUID file name.

In response, Tracelog starts the MyTrace trace log session and enables the provider specified by the GUID. It uses the default values for other properties of the session, including creating a log file in C:\\LogFile.etl.

If you do not specify the name of the trace session (in this case, "MyTrace"), Tracelog starts an NT Kernel Logger trace session, which is the default.

If you do not specify flags or levels, some providers might not generate trace messages, even when they are enabled.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%202:%20Basic%20Start%20Command%20with%20Provider%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




