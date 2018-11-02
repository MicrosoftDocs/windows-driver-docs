---
title: winrterr
description: The winrterr sets the debugger reporting mode for Windows Runtime errors.
ms.assetid: 72E3EF7A-6055-405F-9E24-C9B81C07B8A7
keywords: ["winrterr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- winrterr
api_type:
- NA
ms.localizationpriority: medium
---

# !winrterr


The **!winrterr** sets the debugger reporting mode for Windows Runtime errors.

```dbgcmd
!winrterr Mode
!winrterr
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Mode"></span><span id="mode"></span><span id="MODE"></span>*Mode*  
The following table describes the possible values for *Mode*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="report"></span><span id="REPORT"></span>report</p></td>
<td align="left"><p>When a Windows Runtime error occurs, the error and related text are displayed in the debugger, but execution contunues. This is the default mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="break"></span><span id="BREAK"></span>break</p></td>
<td align="left"><p>When a Windows Runtime error occurs, the error and related text are displayed in the debugger, and execution stops.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="quiet"></span><span id="QUIET"></span>quiet</p></td>
<td align="left"><p>When a Windows Runtime error occurs, nothing is displayed in the debugger, and execution continues.</p></td>
</tr>
</tbody>
</table>

 

If *Mode* is omitted, **!winrterr** displays the current reporting mode. If the debugger has broken in as a result of a Windows Runtime error, the error and related text are also displayed.

## <span id="see_also"></span>See also


[Windows Runtime Debugger Commands](windows-runtime-debugger-commands.md)

[**!hstring**](-hstring.md)

[**!hstring2**](-hstring2.md)

 

 






