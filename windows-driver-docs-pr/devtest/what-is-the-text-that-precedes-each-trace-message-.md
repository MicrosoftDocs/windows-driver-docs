---
title: What is the Text that Precedes Each Trace Message
description: What is the text that precedes each trace message
ms.date: 04/20/2017
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
