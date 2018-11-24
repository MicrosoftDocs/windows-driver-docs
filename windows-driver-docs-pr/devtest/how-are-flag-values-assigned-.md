---
title: How are flag values assigned
description: How are flag values assigned
ms.assetid: de74e2d9-0ebf-4125-9dbb-42f7755010f4
ms.date: 04/20/2017
ms.localizationpriority: medium
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









