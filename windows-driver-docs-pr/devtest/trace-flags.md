---
title: Trace Flags
description: Trace Flags
ms.assetid: a94159ab-ce21-4604-beb8-ee01e333505e
keywords:
- trace flags WDK
- flags WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Flags


Trace flags are properties of a [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application. These flags determine which events the trace provider generates. The provider interprets the flags as conditions for generating the message.

Typically, flags represent increasingly detailed reporting levels, but the provider can use the flags to represent any condition for generating the trace message.

The trace provider defines each flag in a WPP\_DEFINE\_BIT element of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) structure. The Windows Software Trace Preprocessor (WPP) assigns bit values to the elements in the order that they appear in the structure, beginning with 1.

When running a [trace session](trace-session.md), you can use the trace flags to determine which messages will be generated during the session. [Trace consumers](trace-consumer.md), such as [Tracelog](tracelog.md) and [TraceView](traceview.md), let users set parameters and options to select the trace flags and [trace level](trace-level.md) for each provider in a trace session.

You can change the trace flags while a trace session is running by reenabling the trace provider.

 

 





