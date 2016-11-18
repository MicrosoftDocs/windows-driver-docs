---
title: How are flag values assigned
description: How are flag values assigned
ms.assetid: de74e2d9-0ebf-4125-9dbb-42f7755010f4
---

# How are flag values assigned?


[Trace flags](trace-flags.md) are defined independently by each [trace provider](trace-provider.md). As a result, the flag values for one provider can mean something completely different from the flag values for another provider. To interpret the values, you need to understand the provider.

Typically, trace flags represent increasingly detailed reporting levels.

Flag values are defined in the WPP\_DEFINE\_BIT elements of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro, such as in this example:

```
#define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID(GUIDFriendlyName, (ControlGUID),  \
        WPP_DEFINE_BIT(Error)  \
        WPP_DEFINE_BIT(Unusual)  \
        WPP_DEFINE_BIT(Noise) )
 
```

Windows assigns to each WPP\_DEFINE\_BIT element a consecutive bit value beginning with 1. For example, it would assign 1 to the first bit (Error), 2 to the second bit (Unusual), and 4 to the third bit (Noise).

When you start a [trace session](trace-session.md), use the bit value to represent the flags. For example, the following command uses [Tracelog](tracelog.md) to start a trace session with the [trace provider](trace-provider.md) defined earlier. It sets the flag value to 4 (Noise).

```
tracelog -start MyTrace -guid MyDriver.guid -flags 4
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20are%20flag%20values%20assigned?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




