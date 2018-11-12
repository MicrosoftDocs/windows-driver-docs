---
title: .suspend_ui (Suspend WinDbg Interface)
description: The .suspend_ui command suspends the refresh of WinDbg debugging information windows.
ms.assetid: 7fa6ca5c-f960-49eb-b6f0-a6f2d454984f
keywords: [".suspend_ui (Suspend WinDbg Interface) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .suspend_ui (Suspend WinDbg Interface)
api_type:
- NA
ms.localizationpriority: medium
---

# .suspend\_ui (Suspend WinDbg Interface)


The **.suspend\_ui** command suspends the refresh of WinDbg debugging information windows.

```dbgcmd
.suspend_ui 0 
.suspend_ui 1 
.suspend_ui 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______0______"></span> **0**   
Suspends the refresh of WinDbg debugging information windows.

<span id="_______1______"></span> **1**   
Enables the refresh of WinDbg debugging information windows.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is available only in WinDbg and cannot be used in script files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about debugging information windows, see [Using Debugging Information Windows](using-debugging-information-windows.md).

Remarks
-------

Without any parameters, **.suspend\_ui** displays whether debugging information windows are currently suspended.

By default, debugging information windows are refreshed every time the information they display changes.

Suspending the refresh of these windows can speed up WinDbg during a sequence of quick operations -- for example, when tracing or stepping many times in quick succession.

 

 





