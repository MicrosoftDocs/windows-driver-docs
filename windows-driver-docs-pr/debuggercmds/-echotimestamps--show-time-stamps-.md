---
title: ".echotimestamps (Show Time Stamps)"
description: "The .echotimestamps command turns on or turns off the display of time stamp information."
keywords: ["Show Time Stamps (.echotimestamps) command", "time stamps", "DbgPrint time stamps", ".echotimestamps (Show Time Stamps) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .echotimestamps (Show Time Stamps)
api_type:
- NA
---

# .echotimestamps (Show Time Stamps)


The **.echotimestamps** command turns on or turns off the display of time stamp information.

```dbgcmd
.echotimestamps 0 
.echotimestamps 1 
.echotimestamps 
```

## <span id="ddk_meta_show_time_stamps_dbg"></span><span id="DDK_META_SHOW_TIME_STAMPS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Turns off the display of time stamp information. This is the default behavior of the Debugger.

<span id="_______1______"></span> **1**   
Turns on the display of time stamp information.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For more information about **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx**, see "The DbgPrint Buffer" in [Reading and Filtering Debugging Messages](../debugger/reading-and-filtering-debugging-messages.md).

## Remarks

When you use the **.echotimestamps** command without parameters, the display of time stamps is turned on or off, and the new state is displayed.

If you turn on this display, the debugger shows time stamps for module loads, thread creations, exceptions, and other events.

The **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx** kernel-mode routines send a formatted string to a buffer on the host computer. The string is displayed in the [Debugger Command window](../debugger/debugger-command-window.md) (unless you have disabled such printing). You can also display the formatted string by using the [**!dbgprint**](-dbgprint.md) extension command.

When you use **.echotimestamps** to turn on the display of time stamps, the time and date of each comment in the **DbgPrint** buffer is displayed.

