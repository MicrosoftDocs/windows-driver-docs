---
title: What is the performance cost of software tracing
description: What is the performance cost of software tracing
ms.assetid: 4337a619-58aa-4ad2-8873-6cbf5d84d074
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What is the performance cost of software tracing?


In general, the performance cost of software tracing is very small. The code is minimized, the buffers are managed efficiently, and the messages are written in binary format. Also, formatting trace messages, which is a big performance drain, is deferred until the user chooses to format and display the trace messages.

When you use [WPP software tracing](wpp-software-tracing.md) macros to add software tracing to a driver, there is almost no performance cost at all, unless the provider is enabled for a trace session.

The WPP macros amounts to three conditional checks within an If statement to the software tracing code. These checks prevent any trace messages from being generated unless the provider is enabled. The WPP macros generate code in the following form:

```
If (WPP_CHECK_INIT && WPP_LEVEL_FLAGS_ENABLED) {
    Call trace_message_routine
}
```

In this generated code, WPP\_CHECK\_INIT consists of one conditional check. WPP\_LEVEL\_FLAGS\_ENABLED consists of one conditional check, if you have only one level or flag filter. Otherwise, WPP\_LEVEL\_FLAGS\_ENABLED consists of two conditional checks.

For more information about how to exclude the WPP\_CHECK\_INIT check for better performance, see [Can I optimize the conditional checks that the WPP macros produce before the tracing?](can-i-optimize-the-conditional-checks-that-the-wpp-macros-produce-befo.md).

**Note**  There might be some performance cost if you use methods other than WPP software tracing to implement software tracing in your driver. The effect depends on the implementation method.

 

 

 





