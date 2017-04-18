---
title: What is the text that precedes each trace message
description: What is the text that precedes each trace message
ms.assetid: bff8eb0b-f571-405f-b930-3003e2c50621
---

# What is the text that precedes each trace message?


[Tracefmt](tracefmt.md) and [TraceView](traceview.md) add a [trace message prefix](trace-message-prefix.md) to each trace message that they format. The prefix is a string composed of data about the trace message. You can view the prefix in the Tracefmt and TraceView output.

The following line shows the default syntax for the trace message prefix:

```
[CPUNumber]ProcessID.ThreadID :: SystemTime [MessageGUIDFriendlyName]
```

where the default value of the *MessageGUIDFriendlyName* is the directory in which the [trace provider](trace-provider.md) was built.

The prefix, with values replacing the variables, appears in the following line from a sample trace log:

```
[0]0C40.0C3C::09/20/2004-14:41:31.625 [tracedrv]Hello, 1 Hi
```

You can add and remove data elements from the prefix by creating or editing the %TRACE\_FORMAT\_PREFIX% environment variable.

For instructions and a list of the data elements that you can include in the value of %TRACE\_FORMAT\_PREFIX%, see [Trace Message Prefix](trace-message-prefix.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20What%20is%20the%20text%20that%20precedes%20each%20trace%20message?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




