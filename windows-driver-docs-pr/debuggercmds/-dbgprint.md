---
title: dbgprint (WinDbg)
description: The dbgprint extension displays a string that was previously sent to the DbgPrint buffer.
keywords: ["dbgprint Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dbgprint
api_type:
- NA
---

# !dbgprint


The **!dbgprint** extension displays a string that was previously sent to the **DbgPrint** buffer.

```dbgcmd
!dbgprint
```

## <span id="ddk__dbgprint_dbg"></span><span id="DDK__DBGPRINT_DBG"></span>


### DLL

Kdexts.dll

 

### Additional Information

For information about **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx**, see [Sending Output to the Debugger](../debugger/sending-output-to-the-debugger.md).

## Remarks

The kernel-mode routines **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx** send a formatted string to a buffer on the target computer. The string is automatically displayed in the Debugger Command window on the host computer unless such printing has been disabled.

Generally, messages sent to this buffer are displayed automatically in the Debugger Command window. However, this display can be disabled through the Global Flags (gflags.exe) utility. Moreover, this display does not automatically appear during local kernel debugging. For more information, see "The DbgPrint Buffer" in [Reading and Filtering Debugging Messages](../debugger/reading-and-filtering-debugging-messages.md).

The **!dbgprint** extension causes the contents of this buffer to be displayed (regardless of whether automatic printing has been disabled). It will not show messages that have been filtered out based on their component and importance level. (For details on this filtering, see [Reading and Filtering Debugging Messages](../debugger/reading-and-filtering-debugging-messages.md).)

 

 





