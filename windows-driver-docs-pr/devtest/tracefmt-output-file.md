---
title: Tracefmt Output File
description: Tracefmt Output File
ms.assetid: 55c8964c-992f-468c-83ea-0316fcb12110
keywords: ["Tracefmt WDK , output files", "output files WDK Tracefmt", "files WDK Tracefmt", ".out files", "out files"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tracefmt%20Output%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




