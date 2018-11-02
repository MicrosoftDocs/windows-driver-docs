---
title: dbgprint
description: The dbgprint extension displays a string that was previously sent to the DbgPrint buffer.
ms.assetid: bf25ac2a-5a07-43df-946b-3b2237b1816b
keywords: ["dbgprint Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dbgprint
api_type:
- NA
ms.localizationpriority: medium
---

# !dbgprint


The **!dbgprint** extension displays a string that was previously sent to the **DbgPrint** buffer.

```dbgcmd
!dbgprint
```

## <span id="ddk__dbgprint_dbg"></span><span id="DDK__DBGPRINT_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx**, see [Sending Output to the Debugger](sending-output-to-the-debugger.md).

Remarks
-------

The kernel-mode routines **DbgPrint**, **KdPrint**, **DbgPrintEx**, and **KdPrintEx** send a formatted string to a buffer on the target computer. The string is automatically displayed in the Debugger Command window on the host computer unless such printing has been disabled.

Generally, messages sent to this buffer are displayed automatically in the Debugger Command window. However, this display can be disabled through the Global Flags (gflags.exe) utility. Moreover, this display does not automatically appear during local kernel debugging. For more information, see [The DbgPrint Buffer](reading-and-filtering-debugging-messages.md#the-dbgprint-buffer).

The **!dbgprint** extension causes the contents of this buffer to be displayed (regardless of whether automatic printing has been disabled). It will not show messages that have been filtered out based on their component and importance level. (For details on this filtering, see [Reading and Filtering Debugging Messages](reading-and-filtering-debugging-messages.md).)

 

 





