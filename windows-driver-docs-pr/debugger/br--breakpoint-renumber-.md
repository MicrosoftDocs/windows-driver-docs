---
title: br (Breakpoint Renumber)
description: The br command renumbers one or more breakpoints.
ms.assetid: 1b41eb37-3375-4203-bbf5-f55869383db8
keywords: ["br (Breakpoint Renumber) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- br (Breakpoint Renumber)
api_type:
- NA
ms.localizationpriority: medium
---

# br (Breakpoint Renumber)


The **br** command renumbers one or more breakpoints.

```dbgcmd
br OldID NewID [OldID2 NewID2 ...] 
```

## <span id="ddk_cmd_breakpoint_renumber_dbg"></span><span id="DDK_CMD_BREAKPOINT_RENUMBER_DBG"></span>Parameters


<span id="_______OldID______"></span><span id="_______oldid______"></span><span id="_______OLDID______"></span> *OldID*   
Specifies the current ID number of the breakpoint.

<span id="_______NewID______"></span><span id="_______newid______"></span><span id="_______NEWID______"></span> *NewID*   
Specifies a new number that becomes the ID of the breakpoint.

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

Remarks
-------

You can use the **br** command to renumber any number of breakpoints at the same time. For each breakpoint, list the old ID and the new ID, in that order, as parameters to **br**.

If there is already a breakpoint with an ID equal to *NewID*, the command fails and an error message is displayed.

 

 





