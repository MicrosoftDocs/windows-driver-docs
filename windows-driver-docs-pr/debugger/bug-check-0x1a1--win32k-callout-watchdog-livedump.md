---
title: Bug Check 1A1 WIN32K_CALLOUT_WATCHDOG_LIVEDUMP
description: The WIN32K_CALLOUT_WATCHDOG_LIVEDUMP has a value of 0x000001A1.
keywords: ["Bug Check 0x1A1 WIN32K_CALLOUT_WATCHDOG_LIVEDUMP", "WIN32K_CALLOUT_WATCHDOG_LIVEDUMP"]
ms.date: 07/19/2021
topic_type:
- apiref
ms.topic: reference
api_name:
- WIN32K_CALLOUT_WATCHDOG_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1A1: WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP

The WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP live dump has a value of 0x000001A1. A callout to Win32k did not return promptly.

## WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP Parameters

The following parameters are displayed on the blue screen.

| Parameter |                        Description                    |
|-----------|-------------------------------------------------------|
|     1     | Thread blocking prompt return from a Win32k callout.  |
|     2     | Reserved.                                             |
|     3     | Reserved.                                             |
|     4     | Reserved.                                             |

## Cause

A callout to Win32k did not return promptly.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## Remarks

For general information about working with threads, see:

[Controlling Processes and Threads](controlling-processes-and-threads.md)

[Windows Kernel-Mode Process and Thread Manager](../kernel/windows-kernel-mode-process-and-thread-manager.md)

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
