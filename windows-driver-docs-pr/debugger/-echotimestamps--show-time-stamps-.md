---
title: .echotimestamps (Show Time Stamps)
description: The .echotimestamps command turns on or turns off the display of time stamp information.
ms.assetid: c70dc71b-83c2-41de-90f3-638e231c0476
keywords: ["Show Time Stamps (.echotimestamps) command", "time stamps", "DbgPrint time stamps", ".echotimestamps (Show Time Stamps) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .echotimestamps (Show Time Stamps)
api_type:
- NA
---

# .echotimestamps (Show Time Stamps)


The **.echotimestamps** command turns on or turns off the display of time stamp information.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.echotimestamps%20%28Show%20Time%20Stamps%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




