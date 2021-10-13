---
title: Sending Output to the Debugger
description: Sending Output to the Debugger
keywords: ["sending output to the debugger", "OutputDebugString function", "DbgPrint function", "DbgPrintEx function", "KdPrint function", "KdPrintEx function"]
ms.date: 07/20/2020
ms.localizationpriority: medium
---

# Sending Output to the Debugger

User-mode and kernel-mode code use different routines to send output to the debugger.

## User-Mode Output Routines

The **OutputDebugString** routine sends a null-terminated string to the debugger of the calling process. In a user-mode driver, **OutputDebugString** displays the string in the Debugger Command window. If a debugger is not running, this routine has no effect. **OutputDebugString** does not support the variable arguments of a **printf** formatted string.

The prototype for this routine is as follows:

```cpp
VOID OutputDebugString(
   LPCTSTR lpOutputString
   );
```

For complete documentation of this routine, see [Communicating with the Debugger](/windows/win32/debug/communicating-with-the-debugger).

### Kernel-Mode Output Routines

The [**DbgPrint**](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgprint) routine displays output in the debugger window. This routine supports the basic **printf** format parameters. Only kernel-mode drivers can call **DbgPrint**.

The [**DbgPrintEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgprintex) routine is similar to **DbgPrint**, but it allows you to "tag" your messages. When running the debugger, you can permit only those messages with certain tags to be sent. This allows you to view only those messages that you are interested in. For details, see [Reading and Filtering Debugging Messages](reading-and-filtering-debugging-messages.md).


The [**KdPrint**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdprint) and [**KdPrintEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdprintex) macros are identical to **DbgPrint** and **DbgPrintEx**, respectively, when compiled in the checked build environment. When compiled in the free build environment, they have no effect.
