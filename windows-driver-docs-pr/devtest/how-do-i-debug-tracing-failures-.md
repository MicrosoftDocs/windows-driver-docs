---
title: How do I debug tracing failures
description: How do I debug tracing failures
ms.assetid: 9f974482-e19d-4bcc-a884-4425741aa465
---

# How do I debug tracing failures?


To debug problems with your trace-instrumented driver, such as trace messages that are not showing up in trace log files, even when the provider is enabled, add a **WppDebug** macro definition to your source code.

**WppDebug** enables code designed to debug WPP. It traces actions such as registration and enable/disable activity.

Any **WppDebug** definition directive will work. For example:

```
#define WppDebug(a,b) printf b, printf("\n");
```

To call the routine, use the following format:

```
WppDebug(level,(format,...));
```

Do not confuse the **WppDebug** macro, which traces WPP actions, with the **WPP\_DEBUG** macro, which sends trace messages to a debugger.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20debug%20tracing%20failures?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




