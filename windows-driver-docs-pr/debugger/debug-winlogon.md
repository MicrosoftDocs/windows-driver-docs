---
title: Debug WinLogon
description: Debug WinLogon
ms.assetid: c30e6b83-685a-4e4e-88bf-1e05776ac87a
keywords: ["Debug WinLogon (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debug WinLogon


## <span id="ddk_debug_winlogon_dtools"></span><span id="DDK_DEBUG_WINLOGON_DTOOLS"></span>


The **Debug WinLogon** flag debugs the WinLogon service.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>dwl</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x04000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND_EX</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

NTSD debugs Winlogon (by using the command **ntsd -d -g -x**), but control is redirected to the kernel debugger.

For details on NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Debug initial command](debug-initial-command.md), [Enable debugging of Win32 subsystem](enable-debugging-of-win32-subsystem.md)

 

 





