---
title: Where are the tracing samples
description: Where are the tracing samples
ms.assetid: 68882242-4956-4492-b3ac-e93b67a993a2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Where are the tracing samples?


[TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726) is a sample driver that was designed to demonstrate WPP software tracing. TraceDrv is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507 ) repository on GitHub.

The TraceDrv sample also includes TraceCtl, an application that starts TraceDrv and causes it to generate trace messages.

[Toaster](http://go.microsoft.com/fwlink/p/?linkid=256195), the general sample driver in the WDK, is also instrumented for [WPP software tracing](wpp-software-tracing.md). It is also available from [Windows hardware development samples](http://go.microsoft.com/fwlink/p/?LinkId=618052).

[Eventdrv](http://go.microsoft.com/fwlink/p/?LinkId=617724) is a sample that demonstrates how to implement [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) in a driver. The ETW kernel-mode API was introduced with Windows Vista and is not supported in earlier operating systems.

 

 





