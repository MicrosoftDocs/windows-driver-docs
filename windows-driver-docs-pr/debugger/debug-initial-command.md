---
title: Debug initial command
description: Debug initial command
keywords: ["Debug initial command (global flag)"]
ms.date: 12/22/2021
---

# Debug initial command


## <span id="ddk_debug_initial_command_dtools"></span><span id="DDK_DEBUG_INITIAL_COMMAND_DTOOLS"></span>


The **Debug initial command** flag debugs the Client Server Run-time Subsystem (CSRSS) and the WinLogon process.


> [!NOTE]
> Starting in Windows 10, CSRSS is a protected process and can only be debugged in kernel mode.
>

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>dic</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x4</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

NTSD debugs the processes (using the command **ntsd -d**), but control is redirected to the kernel debugger.

For details on NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Enable debugging of Win32 subsystem](enable-debugging-of-win32-subsystem.md)

 

 





