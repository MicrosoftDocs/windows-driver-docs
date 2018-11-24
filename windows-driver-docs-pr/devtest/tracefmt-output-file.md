---
title: Tracefmt Output File
description: Tracefmt Output File
ms.assetid: 55c8964c-992f-468c-83ea-0316fcb12110
keywords:
- Tracefmt WDK , output files
- output files WDK Tracefmt
- files WDK Tracefmt
- .out files
- out files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracefmt Output File


The Tracefmt output (.out) file is a text file displaying the trace messages from a trace log or real-time trace session in human-readable format. Each trace message is preceded by a customizable [trace message prefix](trace-message-prefix.md).

The Tracefmt output file is optional. You can direct Tracefmt to display the trace messages, but not create an output file, or to both display the trace messages and record them in an output file.

Tracefmt output files are often used as input to other programs that analyze and filter trace messages.

The following is an excerpt of the content of a Tracefmt output file of a trace session with Tracedrv, a sample driver instrumented for software tracing. [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726), a sample driver that was designed for software tracing, is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

```
EventTrace
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]IOCTL = 1
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]Hello, 1 Hi
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]Hello, 2 Hi
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]Hello, 3 Hi
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]Hello, 4 Hi
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]Hello, 5 Hi
[0]0888.0D60::10/23/2003-12:27:40.173 [tracedrv]Hello, 6 Hi
```

 

 





