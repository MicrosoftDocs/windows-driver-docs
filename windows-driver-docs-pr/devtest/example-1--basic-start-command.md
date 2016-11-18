---
title: Example 1 Basic Start Command
description: Example 1 Basic Start Command
ms.assetid: be5abbf0-727d-430b-a427-66cc61f3445c
keywords: ["trace sessions WDK , starting", "start command", "-start command", "starting trace sessions"]
---

# Example 1: Basic Start Command


The following command is an example of the simplest command that starts a standard trace session:

```
tracelog -start MyTrace
```

This command starts a session named "MyTrace". The session has the default values for other session properties, including a log file in the default location, C\\LogFile.etl.

If the command did not include a session name, Tracelog would have started an NT Kernel Logger trace session, which is the default.

Because the command does not include a **-guid** parameter, no providers are enabled for the trace session, but you can use a **tracelog -enable** command to add providers to this session after it starts.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%201:%20Basic%20Start%20Command%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




