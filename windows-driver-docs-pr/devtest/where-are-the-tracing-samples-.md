---
title: Where are the tracing samples
description: Where are the tracing samples
ms.date: 04/20/2017
---

# Where are the tracing samples?

[TraceDrv](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/tracing/tracedriver) is a sample driver that was designed to demonstrate WPP software tracing. TraceDrv is available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

The TraceDrv sample also includes TraceCtl, an application that starts TraceDrv and causes it to generate trace messages.

[Toaster Sample Driver](/samples/microsoft/windows-driver-samples/toaster-sample-driver/), the general sample driver in the WDK, is also instrumented for [WPP software tracing](wpp-software-tracing.md).

[Eventdrv](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/tracing/evntdrv) is a sample that demonstrates how to implement [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) in a driver. The ETW kernel-mode API was introduced with Windows Vista and is not supported in earlier operating systems.

 

