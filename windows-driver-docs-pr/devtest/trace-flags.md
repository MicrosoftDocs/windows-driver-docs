---
title: Trace Flags
description: Trace Flags
ms.assetid: a94159ab-ce21-4604-beb8-ee01e333505e
keywords: ["trace flags WDK", "flags WDK software tracing"]
---

# Trace Flags


Trace flags are properties of a [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application. These flags determine which events the trace provider generates. The provider interprets the flags as conditions for generating the message.

Typically, flags represent increasingly detailed reporting levels, but the provider can use the flags to represent any condition for generating the trace message.

The trace provider defines each flag in a WPP\_DEFINE\_BIT element of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) structure. The Windows Software Trace Preprocessor (WPP) assigns bit values to the elements in the order that they appear in the structure, beginning with 1.

When running a [trace session](trace-session.md), you can use the trace flags to determine which messages will be generated during the session. [Trace consumers](trace-consumer.md), such as [Tracelog](tracelog.md) and [TraceView](traceview.md), let users set parameters and options to select the trace flags and [trace level](trace-level.md) for each provider in a trace session.

You can change the trace flags while a trace session is running by reenabling the trace provider.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Flags%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




