---
title: What is the performance cost of software tracing
description: What is the performance cost of software tracing
ms.assetid: 4337a619-58aa-4ad2-8873-6cbf5d84d074
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20What%20is%20the%20performance%20cost%20of%20software%20tracing?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




