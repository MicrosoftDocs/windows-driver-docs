---
title: .echotimestamps (Show Time Stamps)
description: The .echotimestamps command turns on or turns off the display of time stamp information.
ms.assetid: c70dc71b-83c2-41de-90f3-638e231c0476
keywords: ["Show Time Stamps (.echotimestamps) command", "time stamps", "DbgPrint time stamps", ".echotimestamps (Show Time Stamps) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .echotimestamps (Show Time Stamps)
api_type:
- NA
ms.localizationpriority: medium
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

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx**, see [The DbgPrint Buffer](reading-and-filtering-debugging-messages.md#the-dbgprint-buffer) or see the Microsoft Windows Driver Kit (WDK) documentation.

Remarks
-------

When you use the **.echotimestamps** command without parameters, the display of time stamps is turned on or off, and the new state is displayed.

If you turn on this display, the debugger shows time stamps for module loads, thread creations, exceptions, and other events.

The **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx** kernel-mode routines send a formatted string to a buffer on the host computer. The string is displayed in the [Debugger Command window](debugger-command-window.md) (unless you have disabled such printing). You can also display the formatted string by using the [**!dbgprint**](-dbgprint.md) extension command.

When you use **.echotimestamps** to turn on the display of time stamps, the time and date of each comment in the **DbgPrint** buffer is displayed.

 

 





