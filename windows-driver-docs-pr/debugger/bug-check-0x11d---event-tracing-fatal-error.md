---
title: Bug Check 0x11D EVENT_TRACING_FATAL_ERROR
description: The EVENT_TRACING_FATAL_ERROR bug check has a value of 0x0000011D. This bug check indicates that the Event Tracing subsystem has encountered an unexpected fatal error.
keywords: ["Bug Check 0x11D EVENT_TRACING_FATAL_ERROR", "EVENT_TRACING_FATAL_ERROR"]
ms.date: 12/08/2020
topic_type:
- apiref
api_name:
- EVENT_TRACING_FATAL_ERROR
api_type:
- NA
---

# Bug Check 0x11D: EVENT\_TRACING\_FATAL\_ERROR

The EVENT\_TRACING\_FATAL\_ERROR bug check has a value of 0x0000011D. This bug check indicates that the Event Tracing subsystem has encountered an unexpected fatal error.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Resolution

In a kernel debugger, use the [**!analyze -v**](-analyze.md) command to perform the initial bug check analysis. Parameter 1 will list the subtype of the bugcheck.

0x01 : Unable to initialize security.

0x02 : Unable to initialize processor.

0x03 : Kernel mode registration corruption.

0x04 : Invalid handle in unregistration.

0x05 : Data overrun in EventWrite call.

0x06 : Event has been lost.

0x07 : Trace buffer corruption.

0x08 : Unable to allocate cache-aware rundown protection for ETW LoggerContext. Parameter 2 will contain the Logger Id.

0x09 : The reference count of ETW GuidEntry is illegal for the current state of the object. Parameter 2 will contain a pointer to ETW_GUID_ENTRY.


## See also

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)
